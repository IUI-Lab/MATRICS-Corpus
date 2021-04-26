
# About Data
This document describes the detailed explanation about MATRICS corpus.

## ./utterance/
Utterance segments by human annotators and their transcriptions. Note that all participants in the meetings were Japanese native speakers.

Each utterance is an inter-pausal unit (IPU). When a silence longer than 200ms was detected, that was identified as an IPU boundary. 

Utterance transcription may contain special symbols. The explanation of each symbol is given below.

|symbol|description|
|:--|:--|
|`{A}`, `{B}`, `{C}`, `{D}`|Participant's real name mentioned in the utterance is replaced with an alphabet letter.|
|`{LAUGH}`|laughter|

Laughing interval is specified using `{LAUGH}`. A given audio interval is exclusively identified as either laughing interval or speaking a language interval (The data is currently a bit noisy. Some parts do not completely follow the rules, but the data will be cleaned up in the future). Annotation interval is split even if the pause between a laughing interval and a language speaking interval is less than 200ms.


## ./speech.melspectrogram/
Speech melspectrograms from raw audio.

These files were generated using `./script/melspectrogram.py`.

## ./speech.prosody/
Speech prosodic information from raw audio.

These files were generated using `./script/OpenSmile.py` with `./script/OpenSmileConfigs/prosodyShs.conf`.

The `./script/OpenSmileConfigs/prosodyShs.conf` was based on the sample file provided by `OpenSMILE`, but following two points were modified: 1) input/output part, 2) `frameStep`

## ./speech.mfcc/
Speech MFCC from raw audio.

These files were generated using `./script/OpenSmile.py` with `./script/OpenSmileConfigs/MFCC12_0_D_A.conf`.

The `./script/OpenSmileConfigs/MFCC12_0_D_A.conf` was based on the sample file provided by `OpenSMILE`, but following two points were modified: 1) input/output part, 2) `frameStep`

## ./OpenFace.csv/
Output from `OpenFace`.

See `OpenFace.wiki` for more detail.


## [Spread Sheet](https://docs.google.com/spreadsheets/d/1xlb-OS3ZGKxv8JRhEivDEije3ebN9YUlptM8EsGHnaY/edit?usp=sharing)

### `participant` sheet
This sheet shows participants' age, sex, and self-reported Big-5 personality traits.

We used the Japanese version of NEO-FFI questionnaire to measure the subjects’ personality traits. The questionnaire contains 12 questions for each personality trait factor. Each question used 5 point Likert scale. Thus, the score for each personality trait was computed by summing up the scores for 12 questions.


### `skills` sheet
This sheet shows the participants' facilitation skill scores, communication skill scores, and hireability scores. 7 external observers were assessed each participant using 5 point Likert scale. Therefore, the scores for each evaluation perspective were calculated by averaging the ratings reported by the seven observers.

The details of evaluation perspectives are shown below. 
- F1-F7 and FA: Facilitation skill
- C1-C5 and CA: Communication skill
- H1-H3 and HA: Hirebility

|item|description-ja|discription-en|
|:--|:--|:--|
|F1|話し合いの口火を切る|Start a discussion or a new topic|
|F2|始めだけでなく，随所でリードしていく|Lead the discussion at many points|
|F3|話すポイントを提案していく|Propose discussion points|
|F4|出た意見をまとめていく|Aggregate and summarize member opinions|
|F5|論点がずれないように整理し，ずれた場合は軌道修正をする|Attempt to maintain the discussion on topic and restore the discussion to topic if group members digressed|
|F6|起承転結を意識して，時間配分を考える|Be conscious of the structure of the discussion and consider time pressure|
|F7|全員の意見を引き出そうとする|Attempt to elicit opinions from other|
|C1|傾聴する姿勢|Attitude of listening|
|C2|双方向の円滑なコミュニケーション|Smooth two-way communication|
|C3|意見集約力|Ability to opinion gathering|
|C4|情報伝達力|Ability to convey information|
|C5|論理的で明瞭な主張|Ability to logical and clear assertion|
|H1|説得力|Persuasiveness|
|H2|善悪判断力|Ability to judge whether something is good or bad|
|H3|ストレス耐性|Stress tolerance|
|FA|リーダーシップ度|Overall facilitation skill score|
|CA|コミュニケーション能力|Overall communication skill score|
|HA|就職力|Overall hirability score|
