<img width="1147" alt="frontpage" src="https://github.com/orcasound/orca-eye-aye/assets/47680801/11ec2810-b101-48af-99b5-e7dd6abffc9a">    

# orca-eye-aye 👁
_Hi there!_ This repository serves as a hub for the development of visual analysis projects undertaken by the [Orcasound open source community](https://github.com/orcasound), as well as the dissemination of our open-access dataset featuring side-view images of vessels (boats and ships). Our main project documented here is the development of a Real-Time Automated Vessel Detection System Using Side View Images. The goal of the system is to help identify sources of underwater noise monitored through the [Orcasound hydrophone network](https://orcasound.net), especially boats that do not broadcast their identity via the Automated Identification System (AIS) as ships are required to do. For historical context on this effort to study vessel impacts on the endangered Southern Resident killer whales in Washington State (USA), see Orcasound's [Salish Sea vessel research page](https://www.orcasound.net/portfolio/salish-sea-vessel-research/). 

## Real-Time Automated Vessel Detection System Using Side View Images

_Release 1.0: 31 March 2024
_Authors: Ze Cui (mentored by Samantha King, Scott Veirs, and Val Veirs)_   
_If you have any questions, feel free to contact me via E-mail: cuize88@gmail.com_


In the video below of a presentation made to Protected Seas staff in fall 2023, I outline the project's motivation, objectives, and methodology. I discuss the open labeled dataset we developed and preliminary results from a deep learning model trained on the dataset. Finally, I talk about the challenges we faced in the final phase of the project:

[![Watch the video](https://img.youtube.com/vi/uyin-k-F2fI/maxresdefault.jpg)](https://youtu.be/uyin-k-F2fI)

## Methodology
    
Through my internship, I proposed to create an open object detection model for real time vessel monitoring in the marine environment. My project involved two phases, both leveraging an archive of about half a million unlabeled side-view vessel images from a [Marine Monitor (M2) radar-camera system](https://m2marinemonitor.com/) ([more info about M2](#). First, I collaborated with [Protected Seas](https://protectedseas.net) and [Beam Reach](https://beamreach.blue/) to build an 11-class side-view vessel data set using the [Roboflow](Roboflow.com) annotation app. Second, using the labeled data set, we developed an initial vessel detection model using the YOLO algorithm.  

### Phase 1. Generate an open-access labeled data set of side-view vessel images from the Marine Monitor (M2) system located at the Orcasound Lab and publish it under a Creative Commons license. For context, here is the M2 vessel tracking system mounted in a madrona tree at the Orcasound Lab:

It uses radar and AIS to aim a pan-tilt-zoom camera at passing vessels and photograph them (primarily acquiring side-view images). You can explore more [images of the Marine Monitor deployment at Orcasound Lab](https://photos.app.goo.gl/axfEaEMb6aw9acto6). An example vessel image from the system is shown at the top of this README.

Our long-term goal is a dataset of 10,000 samples governed by [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en) license. Easy access and discovery of this training set is accomplished by serving it as part of Orcasound’s open data buckes (via Amazon's S3 service), specifically the “Visual Sandbox”(funded by Beam Reach). The marine vessels are classified into 11 classes (as of release 1):    

    - non-commercial small
    - non-commercial medium
    - non-commercial large
    - non-commercial sailing
    - commercial small
    - commercial large fishing
    - commercial large passenger
    - commercial cargo
    - commercial tug
    - other
    - unknown

We began by manually labeling a subsample of the M2 images (a few days from different seasons). During the labeling process we found that the amount of images was huge, but the quality varied with some images containing no ships or very blurry ones. On one hand, we would like each image to be of high quality (i.e. with outlines and colors of the vessels clearly visible) and the bounding box for each vessel annotation to have a minimum dimension of at least 50 pixels. On the other hand, we also wanted to include the as much information as possible about the actual scene (e.g. to train models on more challenging suites of images), so we added three additional qualifiers to further describe each vessel class when necessary: distant, blurry, and backlit. We defined these categories as：

   1. Distant. The vessel is too small or too far away, resulting in a bounding box with at least one dimension of less than 50 pixels.
   2. Blurry. Unsuccessful camera focus caused blurring of the vessel's outline and details.
   3. Backlit. Overexposure causes loss of the ship's color information.

Using the qualifier, we incorporated some of the otherwise problematic samples into the dataset, which helped to increase the diversity of the dataset as well as balance the classes. Nevertheless, we still had a unbalanced dataset so we filtered the raw M2 imagery to add as many minority-class images as possible. We used the resulting dataset to train a model for detecting each vessels in each images within the Roboflow platform, reducing the time and effort of manual annotation.

Explicit definitions of the vessel classes and image qualifiers can be found in our [Vessel Classification Dictionary](https://docs.google.com/document/d/1Rdn4ziShCNLJWMKf9IGO9VMJalLB41HYNDbFCTLYYYc/edit).

The free open labled dataset is an initial compilation and classification of the accumulated data from the M2 system. Future releases will add images to create a more balanced dataset across a more diverse suite of vesssel classes. Each improved dataset will be crucial for developing deep learning models for vessel detection and classification.    

### Most-recent addition to the labeled dataset

- added on Jul/13/23: **_vesselDetection_071023_**   
This dataset includes 3495 images from July and October 2022 containing vessels from all 11 classes. Here's a Roboflow "health check" that shoes the distribution of labels:
  ![Screen Shot 2024-02-23 at 1 38 21 PM](https://github.com/orcasound/orca-eye-aye/assets/47680801/83c34704-da70-484c-89b8-61eddfc54f4f)


### Phase 2: Train models with the labeled data

For the initial release, we created two automated real-time vessel object detection systems. The first is for detecting vessels in the image. The second is for vessel classification.    

For detecting the existence of vessels, the quality of the training data is not required to be very high, but the outlines still need to be discernible. 

![Blank diagram (1)](https://github.com/orcasound/orca-eye-aye/assets/47680801/9682150b-9de8-4c5e-92e0-313ba7a0c3a5)

We used transfer learning with pre-trained Yolo5-Yolo8 models. The code used to process the labled data sets from the Roboflow annotation app, train the model, and assess its performance is shared via [the VesselDetection_train iPython notebook](VesselDetection_train.ipynb) in this reposistory under the MIT software license.
 
The model is stored alongside the training data within the Visual Sandbox bucket and is freely shared under a Responsible AI Licence (RAIL). The [Orca Aye Eye RAIL](Orca-Eye-Aye-RAIL.md) was customized from boilerplate acquired via the [Responsible AI license generator](https://www.licenses.ai/rail-license-generator). 

## How to access the labeled dataset, models, and weights

Within the 'visual-sandbox/orca-eye-aye/' S3 directory, there are three folders:

1. *data* holds our labeled dataset.
2. *model* stores our most recent model(s).
3. *results* presents inferences based on image data from Orcasound Lab.

Model weights are stored in this repo within the `weights` directory.

You have two options for assessing the data products stored beyond this repository:

- Option 1: via AWS S3 bucket  
  - All prodcuts can be accessed via `aws --no-sign-request s3 sync s3://visual-sandbox/orca-eye-aye/`.  
  - Labeled datasets are archived at `s3://visual-sandbox/orca-eye-aye/data/`  
  - Model versions are stored at `s3://visual-sandbox/orca-eye-aye/model/`  

- Option 2: via Roboflow Universe  
  At Roboflow Universe, you can access our entire collection of labeled datasets, including ongoing projects, [here](https://universe.roboflow.com/cuize/)


## Future work

We took an iterative approach to developing our models using archived data, but our intent is to deploy an open object detection model for marine vessel monitoring in real time. Eventually we hope to associate peaks in real time noise metrics with the class, track, and speed of any passing vessel (AIS or non-AIS).

## More about Marine Monitor (M2)

[Marine Monitor (M2)](https://m2marinemonitor.com/) is a shore-based, multi-sensor platform that integrates X-band marine radar, optical cameras, and other sensors with custom software to autonomously track and report on vessel activity in nearshore areas. By using radar, vessels of all types are tracked by the system, including smaller boats that are typically not required to participate in common tracking systems. M2 also receives and documents vessel information from the Automatic Identification System (AIS) which is primarily used by larger commercial vessels. The camera is dynamically directed to vessel locations, provided by both radar and AIS, throughout its transit, so that images are captured while vessels are within range of the M2 system. M2 was designed by ProtectedSeas as a tool for marine managers to more effectively monitor and document human activities in sensitive marine areas. 

<p align = 'center'>
<img src="https://github.com/orcasound/orca-eye-aye/assets/47680801/e67703cd-214b-4d88-8540-4274cc488125" width='300' length='300'>
</p>

### Acknowledgments

I would like to extend my deepest gratitude to Scott Veirs, Samantha King, and Val Veirs for their invaluable mentorship throughout this project. Their insights and expertise have been instrumental in shaping both the direction and outcomes of this work. I extend my appreciation to them for defining the true spirit of dedication in academic research and practice. _-- Ze Cui_


methodology: process of generating data, training 
adding license
