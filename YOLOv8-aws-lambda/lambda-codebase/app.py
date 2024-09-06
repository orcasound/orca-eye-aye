import boto3
import json
import base64
from io import BytesIO
from PIL import Image, ImageDraw
from yolo_onnx.yolov8_onnx import YOLOv8

# Initialize S3 client
s3_client = boto3.client('s3')

# Initialize YOLOv8 object detector
yolov8_detector = YOLOv8('./models/yolov8n_20patience_best.onnx')

# Define the source and destination bucket names
source_bucket_name = "visual-sandbox"
destination_bucket_name = "visual-sandbox"

# Define the destination base path
destination_base_path = "orca-eye-aye/live-result"

def main(event, context):
    try:
        # Loop through each record in the event (handles multiple image uploads)
        for record in event['Records']:
            # Get the object key (file path) from the record
            object_key = record['s3']['object']['key']
            
            # Fetch the image from S3
            s3_response = s3_client.get_object(Bucket=source_bucket_name, Key=object_key)
            img_data = s3_response['Body'].read()

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
            detections = yolov8_detector(img, size=size, conf_thres=conf_thres, iou_thres=iou_thres)

            draw = ImageDraw.Draw(img)
            for det in detections:
                x0, y0, x1, y1 = det['bbox']
                # Draw rectangle on the image
                draw.rectangle([int(x0), int(y0), int(x1), int(y1)], outline=(255, 0, 0), width=4)

            # Convert the PIL image back to binary format for uploading to S3
            output_img_data = BytesIO()
            img.save(output_img_data, format="JPEG")
            output_img_data.seek(0)

            # Preserve the folder structure by appending the object_key path minus the base folder
            relative_key_path = object_key.split('/', 1)[-1]
            result_img_key = f"{destination_base_path}/{relative_key_path}"
            result_json_key = f"{destination_base_path}/{relative_key_path}_result.json"

            # Save the processed image to S3
            s3_client.put_object(
                Bucket=destination_bucket_name,
                Key=result_img_key,
                Body=output_img_data.getvalue(),
                ContentType='image/jpeg'
            )

            # Prepare the result JSON data
            result_data = {
                "image": object_key,
                "detections": detections
            }

            # Save detection result as JSON file
            s3_client.put_object(
                Bucket=destination_bucket_name,
                Key=result_json_key,
                Body=json.dumps(result_data),
                ContentType='application/json'
            )

            print(f"Processed and saved results for {object_key}.")

        return {
            "statusCode": 200,
            "body": "Image processed and results saved successfully."
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": f"Error processing image: {str(e)}"
        }
