# CC-SSE
This repository stores the source codes and results of syntactic structure ellispis analysis of inline comments in Java.
You can find more details, analyses, and baseline results in our paper "Towards the Analysis and Completion of Syntactic Structure Ellipsis for Inline Comments".
## Folders Introduction
* [/CC-SSE/step1 data/](https://github.com/Sherww/CC-SSE/tree/main/step1%20data). This folder contains several examples of inline comments and corresponding code. The complete data set can be found in https://drive.google.com/drive/folders/1iHCJap7f8jjNHbwHJ-59uSAuUwEF6C8j. It contains 1,307,457 pairs of <InlineComment, Code>.
* [/CC-SSE/step2 dependency parser/](https://github.com/Sherww/CC-SSE/tree/main/step2%20dependency%20parser). This folder contains the code for the parser analysis and the results. All the results for parser can be found in https://drive.google.com/drive/folders/1p-YLbbrpQPnwU7_aqGTXNQ0TmdMFpS1T. The [./readability/](https://github.com/Sherww/CC-SSE/tree/main/step2%20dependency%20parser/statistics/readability) folder contains the statistical results and calculation methods of different code structures, and the [./manual respection/](https://github.com/Sherww/CC-SSE/tree/main/step2%20dependency%20parser/statistics/manual%20respection) folder contains the data set used in manual review and statistical analysis code. 
* [/CC-SSE/step3 completion/](https://github.com/Sherww/CC-SSE/tree/main/step3%20completion). This folder contains the three models used for syntactic structure ellipsis completion.
* [/CC-SSE/step4 user study/](https://github.com/Sherww/CC-SSE/tree/main/step4%20user%20study). This folder contains each piece of data used for user study and the detailed results.
* [/CC-SSE/step5 abbr/](https://github.com/Sherww/CC-SSE/tree/main/step5%20abbr). This folder contains inline comments before and after completion that apply to code abbreviation extensions.
* [/CC-SSE/step6 javadoc/](https://github.com/Sherww/CC-SSE/tree/main/step6%20javadoc%20statistics). This folder contains the sampled Javadoc data set and the corresponding parser results. The data set of JavaDoc could be found in https://drive.google.com/drive/folders/1Lr1Sk6zwOf2bw3EdqRJLEjv-lDZ34dtI
## Train
* The model training and prediction was conducted on a machine with Nvidia GTX 1080 GPU, Intel(R) Core(TM) i7-6700 CPU and 16 GB RAM, the operating system is Ubuntu.
* Please refer to the paper for the detailed parameters of the model.
### CodeBERT Model
* cd codebert/
* cd codebert_obj/ or codebert_sub/
#### Dependency
* pip install torch
* pip install transformers
#### Train 
* train.sh
#### Evaluate
* python accuracy.py
# Contact us
Mail: xiaoweizhang@smail.nju.edu.cn

[![OSCS Status](https://www.oscs1024.com/platform/badge/Sherww/CC-SSE.svg?size=small)](https://www.oscs1024.com/project/Sherww/CC-SSE?ref=badge_small)
