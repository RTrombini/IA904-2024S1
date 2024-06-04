# Datasheet for dataset "OAK-D Synthetic Pose"

Questions from the [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) paper, v7.

Jump to section:

- [Motivation](#motivation)
- [Composition](#composition)
- [Collection process](#collection-process)
- [Preprocessing/cleaning/labeling](#preprocessingcleaninglabeling)
- [Uses](#uses)
- [Distribution](#distribution)
- [Maintenance](#maintenance)

## Motivation

_The questions in this section are primarily intended to encourage dataset creators
to clearly articulate their reasons for creating the dataset and to promote transparency
about funding interests._

### For what purpose was the dataset created? 

The dataset was created for the 3D body pose keypoints estimation targeting specifically the usage of OAK-D devices. This project originated in the context of the activities of the postgraduate course IA904 - Projeto de Modelos em Computação Visual, offered in the first semester of 2024, at Unicamp, under the supervision of Prof. Dr. Leticia Rittner and Prof. Paula D. Paro Costa, both from the Departamento de Engenharia de Computação e Automação (DCA) of the Faculdade de Engenharia Elétrica e de Computação (FEEC).

### Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?

It was created by the students [Elton Cardoso do Nascimento](https://github.com/EltonCN) and [Leonardo Rener de Oliveira](https://github.com/LeonardoRener), both M.Eng. students at FEEC-Unicamp.

### Who funded the creation of the dataset? 

The dataset was created without funding.

### Any other comments?

## Composition

_Most of these questions are intended to provide dataset consumers with the
information they need to make informed decisions about using the dataset for
specific tasks. The answers to some of these questions reveal information
about compliance with the EU’s General Data Protection Regulation (GDPR) or
comparable regulations in other jurisdictions._

### What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?

The instances within the synthetic dataset represent [3D avatars](https://github.com/Unity-Technologies/com.unity.cv.synthetichumans) generated using the Unity engine. These avatars are artificial digital representations of people.

### How many instances are there in total (of each type, if appropriate)?

Set of 6400 instances, where each instance is composed of 3 images in PNG format with annotations in JSON.

### Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?

The set is a sample of possible instances, as it involves generating data synthetically, there is no limitation on the amount of data that can be obtained.

### What data does each instance consist of? 

Each instance has 3 images, representing the view of each camera; and annotations.

### Is there a label or target associated with each instance?

Each instance has an associated JSON file, containing information about the camera and 3D avatar parameters:

- Cameras
  - Pose
  - Calibration matrix
  - Aperture
  - Sensor size
  - Lens shift
- Avatar
  - Pose
  - Generation metadata (age, height, weight, sex, ...)
  - 2D keypoints in each image
  - 3D keypoints in each image

### Is any information missing from individual instances?

No.

### Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)?

No.

### Are there recommended data splits (e.g., training, development/validation, testing)?

Yes, the following split is recommended:

- Train: Scenario0, Scenario1, Scenario2
- Test: Scenario3, Scenario4

Scenario0 and Scenario4 don't randomize the camera parameters, Scenario1-3 incrementally increases the camera parameters additive randomization.

### Are there any errors, sources of noise, or redundancies in the dataset?

No.

### Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?

The dataset is self-contained.

### Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)?

No.

### Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?

No.

### Does the dataset relate to people? 

No, the generated avatars are not based on real people.

### Does the dataset identify any subpopulations (e.g., by age, gender)?

The randomized avatars are generated with random uniform age, gender and ethnicity.

### Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?

No.

### Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?

No.

### Any other comments?

## Collection process

_\[T\]he answers to questions here may provide information that allow others to
reconstruct the dataset without access to it._

### How was the data associated with each instance acquired?

The data was obtained synthetically.

### What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)?

The Unity game engine was used with the addition of the [Perception package](https://github.com/Unity-Technologies/com.unity.perception/tree/main) to export randomized data and [SyntheticHumans](https://github.com/Unity-Technologies/com.unity.cv.synthetichumans) for generation random avatars..

### If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?

It is not.

### Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?

Master's students, they were not paid for this project.

### Over what timeframe was the data collected?

The data was created during the months of May and June of 2024.

### Were any ethical review processes conducted (e.g., by an institutional review board)?

No, as there is no humans envolved.

### Does the dataset relate to people?

No.

### Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)?

The data was synthetically generated.

### Were the individuals in question notified about the data collection?

Irrelevant, as there is no humans envolved.

### Did the individuals in question consent to the collection and use of their data?

Irrelevant, as there is no humans envolved.

### If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?

Irrelevant, as there is no humans envolved.

### Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted?

Irrelevant, as there is no humans envolved.

### Any other comments?

## Preprocessing/cleaning/labeling

_The questions in this section are intended to provide dataset consumers with the information
they need to determine whether the “raw” data has been processed in ways that are compatible
with their chosen tasks. For example, text that has been converted into a “bag-of-words” is
not suitable for tasks involving word order._

### Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?

The data in this synthetic dataset was not pre-processed, cleaned, or labeled. It was generated directly from the Unity engine without any additional processing steps.

### Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?

Yes.

### Is the software used to preprocess/clean/label the instances available?

Irrelevant, as there is no preprocessing.

### Any other comments?

## Uses

_These questions are intended to encourage dataset creators to reflect on the tasks
for which the dataset should and should not be used. By explicitly highlighting these tasks,
dataset creators can help dataset consumers to make informed decisions, thereby avoiding
potential risks or harms._

### Has the dataset been used for any tasks already?

Yes, for carrying out a 3d pose Estimation experiment, estimating 3D key points of human joints.

### Is there a repository that links to any or all papers or systems that use the dataset?

[IA904-3D_Pose (project repository)](https://github.com/EltonCN/IA904-3D_Pose) and [IA904-2024S1 (course repository)](https://github.com/Disciplinas-FEEC/IA904-2024S1/tree/main/projetos/3DStereoBodyPoseEstimation)

### What (other) tasks could the dataset be used for?

Anything related to identify humans, as detection and segmentation.

### Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?

No.

### Are there tasks for which the dataset should not be used?

No.

### Any other comments?

## Distribution

### Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created? 

Yes, the dataset will be public avaiable.

### How will the dataset will be distributed (e.g., tarball on website, API, GitHub)?

Yes, through Zenodo, with DOI: (TODO: dataset ainda não foi publicado)

### When will the dataset be distributed?

June 2024.

### Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?

Yes, under Creative Commons Attribution 4.0 International license (CC BY 4.0)

### Have any third parties imposed IP-based or other restrictions on the data associated with the instances?

No.

### Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?

No.

### Any other comments?

## Maintenance

_These questions are intended to encourage dataset creators to plan for dataset maintenance
and communicate this plan with dataset consumers._

### Who is supporting/hosting/maintaining the dataset?

There will be no maintenance or support after the project end (June 2024). The hosting is provided by Zenodo.

### How can the owner/curator/manager of the dataset be contacted (e.g., email address)?

They can be contacted via the following email addresses: e233840@dac.unicamp.br and l201270@dac.unicamp.br.

### Is there an erratum?

No.

### Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)?

Yes, the dataset may be updated before the project end (June 2024).

### If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)?

Not related to people.

### Will older versions of the dataset continue to be supported/hosted/maintained?

They will be hosted in Zenodo, without maintenance or support after the project end (June 2024).

### If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?

No, but the license don't restrict copy and redistribution. 

### Any other comments?