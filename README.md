
[English](README.md) [日本語](README-ja.md)

# MATRICS Corpus
The MATRICS (**M**ultimod**A**l (**T**ask-oriented) g**R**oup d**I**s**C**u**S**sion) corpus is a corpus that recorded verbal and non-verbal behaviors in group meetings. It contains discussions among four Japanese native speakers on three different topics. The corpus contains 29 dialogues by 10 conversation groups. The time length is 9 hours in total.

<img src="./misc/matrics.gif" height="220">


# Data

Due to the privacy issues, audio and video data that can identify the participants are not included in this version of MATRICS corpus. 
Only the data extracted from video and audio without personal information is uploaded to this repository.

The data released in this repository is a part of the entire corpus due to the limited capacity of the storage. Please check [here](#Download-complete-corpus) if you want to access all the data.

A list of the meeting participants' age, gender, self-reported personality traits, and communication skills assessed by external evaluators are available in [this spreadsheet](https://docs.google.com/spreadsheets/d/1xlb-OS3ZGKxv8JRhEivDEije3ebN9YUlptM8EsGHnaY/edit?usp=sharing).

## Directories

Details of each directory are shown below.

|name|description|
|:--|:--|
|utterance|manually identified utterance segment and transcription for each utterance segment|
|speech.prosody|speech pitch, intensity and etc. extracted by `OpenSMILE`|
|speech.mfcc|MFCC of the speech calculated by `OpenSMILE`|
|speech.melspectrogram|melspectrogram of speech calculated by `librosa`|
|OpenFace.csv|facial feature information calculated using `OpenFace`.|
|scripts|scripts used to maintain the corpus data|


For details of each data, please look at [data.md](./data.md).

## Naming convention
File names were determined based on the following rule.

```
<Task>-<Location><Group>-<Participant>-<Utterance>.txt

// example
BP-S3-A-61.txt
```

See the table below for the description of each symbol.

|symbol|defined value|note|
|:--|:--|:--|
|Task|`GS`, `TP`, `BP`|refer [here](#tasks) for more details|
|Location|`S` (Seikei Univ.) or `R` (Ritsumeikan Univ.)|they speak different dialects between east and west area in Japan|
|Group|>= 0|there is a missing number|
|Participant|`A`, `B`, `C`, `D`|(optional symbol)|
|Utterance|>= 0|(optional symbol)|

Therefore `BP-S3-A-61` means: 1) **BP** task, 2) **3**rd group in **S**eikei Univ., 3) data of participant **A**, 4) **61**th utterance．


## Tasks

The following 3 topics were discussed by the participants.

- Celebrity guest selection (GS)
- Travel planning for foreign friends (TP)
- Booth planning for a school festival (BP)

### Celebrity guest selection (GS)

The participants were asked to pretend that they were the executive committee members for a school festival, and were choosing the guest of the festival. Their discussion task was to decide the ranked order of 15 celebrities by considering cost and audience attraction. For the first five minutes, each participant was requested to read the instructions and decide alone (that is, without interacting with other members) the order of the 15 celebrities. Subsequently, the participants were engaged in a discussion to determine the ranked order as a group.

### Travel planning for foreign friends (TP)

The participants were instructed to create a two-day travel plan for foreign friends visiting Japan on vacation. The discussion time allowed was 20 minutes, and there was no time granted to think individually.

### Booth planning for a school festival (BP)

The participants were instructed to discuss and create a plan for a small booth intended to sell food or drinks at the school festival. The participants were given a map that indicated the location of other booths, as well as possible places for opening their own booth. They also had a document that showed data for the distribution of visitors’ age and the number of visitors by time. The participants were instructed to review these documents for five minutes before starting the discussion. Then, based on the data shown in the documents, the participants were allowed to discuss for 20 minutes where to open their booth and the type of goods they would sell.


## Download complete corpus

You can access the entire corpus data at the following URL!

https://drive.google.com/drive/folders/1iwKoInUv_AsTpd9V5uvbRfUL1dmVm_8w?usp=sharing

Enjoy!

# Acknowledgement

To calculate the feature values, we used [OpenSMILE](https://github.com/audeering/opensmile), [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace), [librosa](https://github.com/librosa/librosa). We would like to express our sincere gratitude.

# License

The license of this corpus is [Creative Commons BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).


If you use this corpus in your research and publish your research, please cite one of [the papers below](#Citation).

# Citation

The MATRICS corpus has been published in the following papers
- [Predicting Influential Statements in Group Discussions using Speech and Head Motion Information](https://dl.acm.org/doi/10.1145/2663204.2663248)
- [グループディスカッションコーパスの構築および性格特性との関連性の分析](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=141595&item_no=1&page_id=13&block_id=8)

BibTeX is as follows.

```
@inproceedings{10.1145/2663204.2663248,
author = {Nihei, Fumio and Nakano, Yukiko I. and Hayashi, Yuki and Hung, Hung-Hsuan and Okada, Shogo},
title = {Predicting Influential Statements in Group Discussions Using Speech and Head Motion Information},
year = {2014},
isbn = {9781450328852},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/2663204.2663248},
doi = {10.1145/2663204.2663248},
booktitle = {Proceedings of the 16th International Conference on Multimodal Interaction},
pages = {136–143},
numpages = {8},
keywords = {facilitation, group discussion, nonverbal information, influential statements},
location = {Istanbul, Turkey},
series = {ICMI ’14}
}
```

```
@article{weko_141595_1,
   author	 = "林,佑樹 and 二瓶,芙巳雄 and 中野,有紀子 and 黄,宏軒 and 岡田,将吾",
   title	 = "グループディスカッションコーパスの構築および性格特性との関連性の分析",
   journal	 = "情報処理学会論文誌",
   year 	 = "2015",
   volume	 = "56",
   number	 = "4",
   pages	 = "1217--1227",
   month	 = "apr"
}
```  
