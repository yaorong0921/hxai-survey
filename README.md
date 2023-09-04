# hxai-survey
This is the repo for the survey paper ["Towards Human-centered Explainable AI: User Studies for Model Explanations"](https://arxiv.org/pdf/2210.11584.pdf)

## Abstract
Explainable AI (XAI) is widely viewed as a sine qua non for ever-expanding AI research. A better understanding of the needs of XAI users, as well as human-centered evaluations of explainable models are both a necessity and a challenge. In this paper, we explore how human-computer interaction (HCI) and AI researchers conduct user studies in XAI applications based on a systematic literature review. After identifying and thoroughly analyzing 97 core papers with human-based XAI evaluations over the past five years, we categorize them along the measured characteristics of explanatory methods, namely *trust*, *understanding*, *usability*, and *human-AI collaboration* performance. Our research shows that XAI is spreading more rapidly in certain application domains, such as recommender systems than in others, but that user evaluations are still rather sparse and incorporate hardly any insights from cognitive or social sciences. Based on a comprehensive discussion of best practices, i.e., common models, design choices, and measures in user studies, we propose practical guidelines on designing and conducting user studies for XAI researchers and practitioners. Lastly, this survey also highlights several open research directions, particularly linking psychological science and human-centered XAI. 

## Guidelines of XAI User Study
Based on past XAI user studies, we provide summary cards of the guidelines:

![Summary cards of the guidelines extracted from past XAI user studies](https://github.com/yaorong0921/hxai-survey/blob/main/guidelines.png "Summary cards of the guidelines extracted from past XAI user studies")

(More details can be found in the paper.)

## Analysis of Papers
For a full list of core papers, please see instructions in `Demo.ipynb`.

Extracted keywords used in the figure (shown below) are stored in json files, and can be found in the folder "code". (Code for extracting keywords can be found there, too.)


![Illustration of the foundational research domains and influenced research domains](https://github.com/yaorong0921/hxai-survey/blob/main/code/combined.png "Illustration of the foundational research domains (Left) and influenced research domains (Right)")

## Citation
If you find this repo useful, please star the repo and cite:
```
@article{rong2022towards,
  title={Towards Human-centered Explainable AI: User Studies for Model Explanations},
  author={Rong, Yao and Leemann, Tobias and Nguyen, Thai-trang and Fiedler, Lisa and Seidel, Tina and Kasneci, Gjergji and Kasneci, Enkelejda},
  journal={arXiv preprint arXiv:2210.11584},
  year={2022}
}
```
Contact me (yao.rong@uni-tuebingen.de) if you have any questions or suggestions.
