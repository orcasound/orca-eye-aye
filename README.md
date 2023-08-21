<img width="1147" alt="frontpage" src="https://github.com/orcasound/orca-eye-aye/assets/47680801/11ec2810-b101-48af-99b5-e7dd6abffc9a">

# orca-eye-aye 👁
_Here you can find all computer vision-related projects in Orcasound!_
Ongoing projects:  
- Real-Time Automated Vessel Detection System Using Side View Images

## Real-Time Automated Vessel Detection System Using Side View Images
We propose to create an open object detection model for real-time marine vessel monitoring. This project will involve two phases and associated deliverables. First, we will collaborate with Protected Seas and Beam Reach to build a data set using the Roboflow annotation app. Then we will develop an object detection model, beginning with the approach of transfer learning and the pre-trained Yolo model.  

These two phases will include the following related tasks:
Build an open-access vessel image dataset using images from the M2 system and publish it under a Creative Commons license. 
1. Create an open-access side-view vessel image dataset using images from the M2 system and publish it under a Creative Commons license. We classify marine vessels into 11 classes (as of 08/21/2023), including:
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
   
    Definitions on the classification of vessels could be found through [Vessel Classification Dictionary](https://docs.google.com/document/d/1Rdn4ziShCNLJWMKf9IGO9VMJalLB41HYNDbFCTLYYYc/edit).
2.  an automated real-time vessel object detection system.

For task 1, the quality of the images is not required to be very high, but the outlines still need to be discernible. Since there is no open access dataset for vessels, our project extends to task 2: compile a high-quality dataset for vessels (we will continue to discuss whether it is open source or not). This dataset is a compilation and classification of the accumulated data from the M2 system and will be crucial for the future training of deep learning models for vessel detection and classification. We envision a dataset of 10,000 samples governed by a Creative Commons license, specifically the SA-BY license. Easy access and discovery of this training set will be accomplished by serving it as part of Orcasound’s open data registry within Amazon’s open data sponsored S3 bucket called the “Acoustic Sandbox” (for free under AWS open data sponsorship through 2024).
Produce an open object detection model for real-time marine vessel monitoring. 

The definition and details about each of these classes are provided in the vessel classification dictionary. 
Data preparation: Build a fine-grained relatively small dataset for 11-way classification with 250 samples in each class. Currently, the vessel type information of the M2 system is required to be entered manually, and we would like to produce an open object detection model for real-time marine vessel monitoring. We initially identified five vessel types cargo ships, tugboats, speedboats, sailboats, and (cruise ships). (During the labeling process, there can be more than 5 categories, but they are generalized to 5 categories in the subsequent training). 
Every vessel category contains 500 images each labeled with vessel type, bounding box, if loaded or not, AIS or non-AIS, etc.
Retrain Yolo v5. First, we will try to transfer learning to the pre-trained Yolo model. Based on the result, we will decide whether to move on to the next task or train from scratch. Training from scratch would increase the training data to 10000 for each vessel type. 
(the vessel type tags currently in the M2 system)
The code used to process the data sets from the Roboflow annotation app, train the model, assess its performance, and possibly retrain the model will be shared via a public repository within the Orcasound Github organization under this particular permissive open-source software license: MIT.
Publish the model along with the performance assessment. The model (version 1?) will be stored alongside the training data within the Acoustic Sandbox bucket or could be published online in another forum (e.g. Kaggle or Zenodo?). It will be shared under this particular type of machine learning license (link, e.g. to a license you and Tianyi choose with us via this discussion of ML licenses or this discussion of Responsible AI Licenses (RAILs).

All datasets are located in Orcasound's S3 bucket: `s3://visual-sandbox/orca-eye-aye/data/`  
Open data archive could be accessed via e.g. --
`aws --no-sign-request s3 sync s3://visual-sandbox/orca-eye-aye/ .`

### Most Recent Added Dataset
- added on Jul/13/23: **_vesselDetection_071023_**   
note: This dataset includes data from July and October 2022. Includes 2641 vessel images across all classes.

Further notes and definitions on the classification of vessels could be found through [Vessel Classification Dictionary](https://docs.google.com/document/d/1Rdn4ziShCNLJWMKf9IGO9VMJalLB41HYNDbFCTLYYYc/edit).

### About Marine Monitor (M2)
Marine Monitor (M2) is a shore-based, multi-sensor platform that integrates X-band marine radar, optical cameras, and other sensors with custom software to autonomously track and report on vessel activity in nearshore areas. By using radar, vessels of all types are tracked by the system, including smaller boats that are typically not required to participate in common tracking systems. M2 also receives and documents vessel information from the Automatic Identification System (AIS) which is primarily used by larger commercial vessels. The camera is dynamically directed to vessel locations, provided by both radar and AIS, throughout its trip, so that images are captured while vessels are within range of the M2 system. M2 was designed by ProtectedSeas as a tool for marine managers to more effectively monitor and document human activities in sensitive marine areas. 
https://m2marinemonitor.com/hardware-specifications/#package-2
<p align = 'center'>
<img src="https://github.com/orcasound/orca-eye-aye/assets/47680801/e67703cd-214b-4d88-8540-4274cc488125" width='300' length='300'>
</p>



https://universe.roboflow.com/cuize/vesseldetection-dhmgv
link to dictionary
methodology: process of generating data, training 
https://photos.app.goo.gl/axfEaEMb6aw9acto6
adding license
history of 
