import boto3
import json
import base64
from io import BytesIO
from PIL import Image, ImageDraw
import requests
from yolo_onnx.yolov8_onnx import YOLOv8

# Initialize S3 client
s3_client = boto3.client("s3")

# Initialize YOLOv8 object detector
yolov8_detector = YOLOv8("./models/yolov8n_20patience_best.onnx")

# Define the source and destination bucket names
source_bucket_name = "visual-sandbox"
destination_bucket_name = "visual-sandbox"

# Define the destination base path
destination_base_path = "orca-eye-aye/live-result"

# Define the API endpoint URL and authorization token
api_endpoint_url = "https://m2mobile.protectedseas.net/api/map/process-classification/"
auth_token = "Z2f9LnHq4VoPUj5b72yRX6vwsiKm1B3Q"


def main(event, context):
    try:
        # Loop through each record in the event (handles multiple image uploads)
        for record in event["Records"]:
            # Get the object key (file path) from the record
            object_key = record["s3"]["object"]["key"]

            # Fetch the image from S3
            s3_response = s3_client.get_object(
                Bucket=source_bucket_name, Key=object_key
            )
            img_data = s3_response["Body"].read()

            # Open image using PIL and convert to RGB
            img = Image.open(BytesIO(img_data)).convert("RGB")

            # Convert image to base64 string (to mimic the original detection method)
            buffered = BytesIO()
            img.save(buffered, format="JPEG")

            # Set detection parameters
            size = 640  # You can adjust this size as needed
            conf_thres = 0.3  # Confidence threshold
            iou_thres = 0.5  # IoU threshold

            # Infer result using YOLOv8
            detections = yolov8_detector(
                img, size=size, conf_thres=conf_thres, iou_thres=iou_thres
            )

            draw = ImageDraw.Draw(img)
            for det in detections:
                x0, y0, x1, y1 = det["bbox"]
                # Draw rectangle on the image
                draw.rectangle(
                    [int(x0), int(y0), int(x1), int(y1)], outline=(255, 0, 0), width=4
                )

            # Convert the PIL image back to binary format for uploading to S3
            output_img_data = BytesIO()
            img.save(output_img_data, format="JPEG")
            output_img_data.seek(0)

            # Preserve the folder structure by appending the object_key path minus the base folder
            relative_key_path = object_key.split("/", 1)[-1]
            result_img_key = f"{destination_base_path}/{relative_key_path}"
            result_json_key = f"{destination_base_path}/{relative_key_path}_result.json"

            # Save the processed image to S3
            s3_client.put_object(
                Bucket=destination_bucket_name,
                Key=result_img_key,
                Body=output_img_data.getvalue(),
                ContentType="image/jpeg",
            )

            # Prepare the result JSON data
            result_data = {"image": object_key, "detections": detections}

            # Extract detection data
            path_parts = object_key.split("/")
            image_filename = path_parts[-1]
            timestamp = image_filename.rpartition(".")[0]
            radar_id = path_parts[2]
            m2_text_id = path_parts[6]
            filename = image_filename
            valid = True if detection else False

            # Hangdle multiple detections or no detections
            transformed_detections = []
            if detections:
                for detection in detections:
                    bbox = detection["bbox"]
                    score = detection["score"]
                    class_id = detection["class_id"]

                    transformed_detection = {
                        "confidence": score,
                        "x1": bbox[0],
                        "y1": bbox[1],
                        "x2": bbox[2],
                        "y2": bbox[3],
                        "class": class_id,
                        "valid": valid,
                        "vessel_type": None,
                        "notes": None,
                        "activity_transit": False,
                        "activity_loiter": False,
                        "activity_overnight": False,
                        "activity_cleanup": False,
                        "activity_fishing": False,
                        "activity_rec_fishing": False,
                        "activity_research": False,
                        "activity_diving": False,
                        "activity_repairs": False,
                        "activity_distress": False,
                        "activity_other": False,
                        "missing_ais": False,
                        "potential_violation": False,
                        "le_contacted": False,
                        "soft_exclusion": False,
                    }
                    transformed_detections.append(transformed_detection)
            else:
                transformed_detection = {
                    "confidence": 0,
                    "x1": 0,
                    "y1": 0,
                    "x2": 0,
                    "y2": 0,
                    "class": "no detections",
                    "vessel_type": None,
                    "notes": "No detections found",
                    "activity_transit": False,
                    "activity_loiter": False,
                    "activity_overnight": False,
                    "activity_cleanup": False,
                    "activity_fishing": False,
                    "activity_rec_fishing": False,
                    "activity_research": False,
                    "activity_diving": False,
                    "activity_repairs": False,
                    "activity_distress": False,
                    "activity_other": False,
                    "missing_ais": False,
                    "potential_violation": False,
                    "le_contacted": False,
                    "soft_exclusion": False,
                }
                transformed_detections.append(transformed_detection)

            payload = {
                "timestamp": timestamp,
                "radar_id": radar_id,
                "m2_text_id": m2_text_id,
                "filename": filename,
                "valid": valid,
                "detections": transformed_detections,
            }

            headers = {"Authorization": auth_token, "Content-Type": "application/json"}
            response = requests.post(api_endpoint_url, json=payload, headers=headers)
            if response.status_code != 200:
                print(f"Failed to send data to API endpoint: {response.text}")
                return {
                    "statusCode": response.status_code,
                    "body": f"Failed to send data to API endpoint: {response.text}",
                }

            # Save detection result as JSON file
            s3_client.put_object(
                Bucket=destination_bucket_name,
                Key=result_json_key,
                Body=json.dumps(result_data),
                ContentType="application/json",
            )

            print(f"Processed and saved results for {object_key}.")

        return {
            "statusCode": 200,
            "body": "Image processed and results saved successfully.",
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {"statusCode": 500, "body": f"Error processing image: {str(e)}"}
