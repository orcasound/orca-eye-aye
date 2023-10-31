<img width="1147" alt="frontpage" src="https://github.com/orcasound/orca-eye-aye/assets/47680801/11ec2810-b101-48af-99b5-e7dd6abffc9a">

# orca-eye-aye 👁
_Here you can find all computer vision-related projects in Orcasound!_
Ongoing projects:  
- Real-Time Automated Vessel Detection System Using Side View Images

## Real-Time Automated Vessel Detection System Using Side View Images

_Author: Ze Cui, Samantha King, Scott Veirs, Val Veirs_  
    
We propose to create an open object detection model for real-time marine vessel monitoring. This project will involve two phases and associated deliverables. First, we will collaborate with [Protected Seas](protectedseas.net) and [Beam Reach](https://beamreach.blue/) to build an 11-class side-view vessel data set using the [Roboflow](Roboflow.com
) annotation app. Then, using this data set, we will develop a vessel detection model using the YOLO algorithm.  

### Phase 1. Generate a labeled data set    
Create an open-access side-view vessel image dataset using images from the M2 system located in the Orcasound Lab (here are some [images of M2 at Orcasound Lab](https://photos.app.goo.gl/axfEaEMb6aw9acto6))and publish it under a Creative Commons license. The marine vessels are classified into 11 classes (as of 08/21/2023), including:
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
   We manually labeled a portion of the images, and during the labeling process we found that the amount of images was huge, but the quality varied. Some samples do not contain ships or are very blurry. On one hand, we would like the dataset to be of high quality: the outlines and colors of the vessels can be clearly seen, and the bounding box with a minimum dimension of at least 50 pixels. On the other hand, we also wanted to include the most information about the actual scene, so we added three additional qualifiers to further describe each vessel class: distant/ blurry/backlit. The three most common causes of poor samples in the actual scene were listed as：
   1. Distant. The vessel is too small or too far away. Result in a bounding box with a dimension smaller than 50 pixels.
   2. Blurry. Blurring of the vessel's outline.
   3. Backlit. Overexposure causes loss of the ship's color information.
      Using the qualifier, we categorized and incorporated some of the otherwise problematic samples into the dataset, which helped to increase the diversity of the dataset as well as balance the classes.
   But despite this, we still face the problem of an unbalanced dataset. For this reason, we intend to quickly filter the raw data of m2 and extract as many minority-class images as possible. We next intend to use the currently available dataset to train a model for detecting the presence of vessels in the images, which will be used to filter the raw data in m2, reducing the time and effort of manual annotation.

   Explicit definitions of the classification of vessels and usage of qualifiers can be found through [Vessel Classification Dictionary](https://docs.google.com/document/d/1Rdn4ziShCNLJWMKf9IGO9VMJalLB41HYNDbFCTLYYYc/edit).

### Most Recent Added Dataset
- added on Jul/13/23: **_vesselDetection_071023_**   
    note: This dataset includes data from July and October 2022. Includes 2641 vessel images across all classes.

    All datasets are located in Orcasound's S3 bucket: `s3://visual-sandbox/orca-eye-aye/data/`  
Open data archive could be accessed via e.g. --
`aws --no-sign-request s3 sync s3://visual-sandbox/orca-eye-aye/ .`



### Phase 2: Train model with labeled data
Create two automated real-time vessel object detection systems. For task 1, the quality of the images is not required to be very high, but the outlines still need to be discernible. Since there is no open access dataset for vessels, our project extends to task 2: compile a high-quality dataset for vessels (we will continue to discuss whether it is open source or not). This dataset is a compilation and classification of the accumulated data from the M2 system and will be crucial for the future training of deep learning models for vessel detection and classification. We envision a dataset of 10,000 samples governed by a Creative Commons license, specifically the SA-BY license. Easy access and discovery of this training set will be accomplished by serving it as part of Orcasound’s open data registry within Amazon’s open data sponsored S3 bucket called the “Acoustic Sandbox”(for free under AWS open data sponsorship through 2024).
Produce an open object detection model for real-time marine vessel monitoring. 
Retrain Yolo v5. First, we will try to transfer learning to the pre-trained Yolo model. Based on the result, we will decide whether to move on to the next task or train from scratch. Training from scratch would increase the training data to 10000 for each vessel type. 
(the vessel type tags currently in the M2 system)
The code used to process the data sets from the Roboflow annotation app, train the model, assess its performance, and possibly retrain the model will be shared via a public repository within the Orcasound Github organization under this particular permissive open-source software license: MIT.
Publish the model along with the performance assessment. The model (version 1?) will be stored alongside the training data within the Acoustic Sandbox bucket or could be published online in another forum (e.g. Kaggle or Zenodo?). It will be shared under this particular type of machine learning license (link, e.g. to a license you and Tianyi choose with us via this discussion of ML licenses or this discussion of Responsible AI Licenses (RAILs).

### About Marine Monitor (M2)
Marine Monitor (M2) is a shore-based, multi-sensor platform that integrates X-band marine radar, optical cameras, and other sensors with custom software to autonomously track and report on vessel activity in nearshore areas. By using radar, vessels of all types are tracked by the system, including smaller boats that are typically not required to participate in common tracking systems. M2 also receives and documents vessel information from the Automatic Identification System (AIS) which is primarily used by larger commercial vessels. The camera is dynamically directed to vessel locations, provided by both radar and AIS, throughout its transit, so that images are captured while vessels are within range of the M2 system. M2 was designed by ProtectedSeas as a tool for marine managers to more effectively monitor and document human activities in sensitive marine areas. 

<p align = 'center'>
<img src="https://github.com/orcasound/orca-eye-aye/assets/47680801/e67703cd-214b-4d88-8540-4274cc488125" width='300' length='300'>
</p>





methodology: process of generating data, training 
adding license
