
[English](README.md) [日本語](README-ja.md)

# MATRICS Corpus
MATRICS (**M**ultimod**A**l (**T**ask-oriented) g**R**oup d**I**s**C**u**S**sion) コーパスはグループ会議における言語・非言語行動を収録したコーパスです．3種類の異なる議題について日本語話者が議論した様子が収録されています．

<img src="./misc/matrics.gif" height="220">


# Data

MATRICS Corpusには会話グループを構成する4名の会話参加者の映像と音声が収録されています．しかし参加者個人を特定するデータ，すなわち映像と音声は公開できません．従って本リポジトリには，映像と音声から抽出できる，参加者個人を特定出来ないデータのみをアップロードします．

このリポジトリで公開されるデータは容量の都合上，コーパス全体の一部です．すべてのデータにアクセスする方法は[こちら](#Download-complete-corpus)を確認してください．

会話参加者の性別，年齢，自己報告の性格特性，外部評価者によるコミュニケーションスキルなどの評価値は[こちらのスプレッドシート](https://docs.google.com/spreadsheets/d/1xlb-OS3ZGKxv8JRhEivDEije3ebN9YUlptM8EsGHnaY/edit?usp=sharing)にて公開しています．


## Directories

各ディレクトリの詳細を以下に示します．

|ディレクトリ名|説明|
|:--|:--|
|Utterance|手動で認定された発話区間と，区間に対応する書き起こし|
|speech.prosody|`OpenSMILE`で計測した音声のピッチ・インテンシティなど|
|speech.mfcc|`OpenSMILE`で計測した音声のMFCC．|
|speech.melspectrogram|`librosa`により計算した音声のメルスペクトログラム|
|OpenFace.csv|`OpenFace`を使用し計算した顔特徴情報|
|scripts|コーパスデータの整備に使用したスクリプト|

各データの詳細は[data.md](./data.md)を参照してください．


## Naming convention
ファイル名の命名は以下の規則に基づいています．

```
<Task>-<Location><Group>-<Participant>-<Utterance>.txt

// 具体例
BP-S3-A-61.txt
```

各シンボルの説明は以下の表を参照してください．

|シンボル|定義値|備考|
|:--|:--|:--|
|Task|`GS`, `TP`, `BP`|[こちら](#tasks)を参照|
|Location|`S` (成蹊大) or `R` (立命館大)|関東と関西の言語には方言により差がある|
|Group|>= 0|欠番あり|
|Participant|`A`, `B`, `C`, `D`|オプションのシンボル|
|Utterance|>= 0|オプションのシンボル|

従って`BP-S3-A-61`は，1) **BP**タスク，2) 成蹊大 (**S**eikei) の**3**番目のグループ，3) 参加者**A**のデータ，4) **61**番目の発話，を意味します．


## Tasks

参加者が議論した議題は以下の3種類です．

- Celebrity guest selection (GS)
- Travel planning for foreign friends (TP)
- Booth planning for a school festival (BP)


### Celebrity guest selection (GS)

会話参加者は学園祭の実行委員という設定で，学園祭での舞台イベントに呼ぶ有名人を決める課題．様々な業界における15名の有名人が記載された資料を渡し，収益や集客を考慮しながら最適だと思われる有名人を順位付けする．初めに5分間各自で資料を読み，個人のランキングを配布したアンケート用紙に記入させる．その後，15分の話し合いでグループのランキングを決定する．

### Travel planning for foreign friends (TP)

外国人の友人が夏に1泊2日で来日するという仮定のもとで，その期間において友人をもてなす旅行計画を立案する課題．議論時間は20分．

### Booth planning for a school festival (BP)

出店可能場所と他店の出店内容が記載された学園祭の会場図，会場エリアの特徴，前年度の年代別来場者数の割合および時間ごとの来場者数が記載された資料に基づき議論する課題．5分間各自で資料に目を通した後，資料内容をふまえて学園祭の出店内容と出店場所を決めるための議論を20分間で実施する．


## Download complete corpus

以下のURLからコーパス全てのデータにアクセスできます．

https://drive.google.com/drive/folders/1iwKoInUv_AsTpd9V5uvbRfUL1dmVm_8w?usp=sharing

# Acknowledgement

特徴値の計算には[OpenSMILE](https://github.com/audeering/opensmile), [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace), [librosa](https://github.com/librosa/librosa)を使用しました．心より感謝申し上げます．

# License

このコーパスのライセンスは[Creative Commons BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)です．

このコーパスを研究で使用した場合は，[以下の文献](#Citation)のいずれかの引用をお願いします．

# Citation

MATRICSコーパスは以下の論文において発表されています．
- [Predicting Influential Statements in Group Discussions using Speech and Head Motion Information](https://dl.acm.org/doi/10.1145/2663204.2663248)
- [グループディスカッションコーパスの構築および性格特性との関連性の分析](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=141595&item_no=1&page_id=13&block_id=8)

BibTeXは以下です．

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
