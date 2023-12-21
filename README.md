# T-Eval: Evaluating the Tool Utilization Capability Step by Step

<div align="center">

[![arXiv](https://img.shields.io/badge/arXiv-xxxx.xxxxx-b31b1b.svg)](https://arxiv.org/abs/xxxx.xxxxx)
[![license](https://img.shields.io/github/license/InternLM/opencompass.svg)](./LICENSE)

</div>

## ✨ Introduction  

This is an evaluation harness for the benchmark described in [T-Eval: Evaluating the Tool Utilization Capability Step by Step](). 

<div align="center">

[[Paper](https://arxiv.org/abs/xxxx.xxxxx)]
[[Project Page](https://open-compass.github.io/T-Eval/)]
[[LeaderBoard](https://open-compass.github.io/T-Eval/leaderboard.html)]

</div>

> Large language models (LLM) have achieved remarkable performance on various NLP tasks and are augmented by tools for broader applications. Yet, how to evaluate and analyze the tool utilization capability of LLMs is still under-explored. In contrast to previous works that evaluate models holistically, we comprehensively decompose the tool utilization into multiple sub-processes, including instruction following, planning, reasoning, retrieval, understanding, and review. Based on that, we further introduce T-Eval to evaluate the tool-utilization capability step by step. T-Eval disentangles the tool utilization evaluation into several sub-domains along model capabilities, facilitating the inner understanding of both holistic and isolated competency of LLMs. We conduct extensive experiments on T-Eval and in-depth analysis of various LLMs. T-Eval not only exhibits consistency with the outcome-oriented evaluation but also provides a more fine-grained analysis of the capabilities of LLMs, providing a new perspective in LLM evaluation on tool-utilization ability.

<!-- 
[T-Eval: ]()<br>
Zehui Chen<sup>&spades;</sup>, Weihua Du<sup>&spades;</sup>, Wenwei Zhang<sup>&spades;</sup>, Kuikun Liu, Jiangning Liu, Miao Zheng, Jingming Zhuo, Songyang Zhang, Dahua Lin, Kai Chen<sup>&diams;</sup>, Feng Zhao<sup>&diams;</sup>

<sup>&spades;</sup> Equal Contribution<br>
<sup>&diams;</sup> Corresponding Author -->

<div>
<center>
<img src="figs/teaser.png">
</div>

## 🚀 What's New

- **[2023.12.21]** Paper available on [Arxiv](). 🔥🔥🔥
- **[2023.12.20]** Release the test scripts and data for T-Eval. 🎉🎉🎉

## 🛠️ Preparations

```bash
$ git clone https://github.com/open-compass/T-Eval.git
$ cd T-Eval
$ pip install lagent
$ pip install requirements.txt
```

## 🎮 Usage

```bash
# test all data at once
sh test_all.sh gpt-4-1106-preview
# test for Instruct only
python test.py --model_type gpt-4-1106-preview --resume --out_name instruct_gpt-4-1106-preview.json --out_dir data/work_dirs/ --dataset_path data/instruct_v1.json --eval instruct --prompt_type json
```

## 📊 Benchmark Results

More detailed and comprehensive benchmark results can refer to 🏆 [T-Eval official leaderboard]()!

<div>
<center>
<img src="figs/teval_results.png">
</div>

## ❤️ Acknowledgements

T-Eval is built with [Lagent](https://github.com/InternLM/lagent) and [OpenCompass](https://github.com/open-compass/opencompass). Thanks for their awesome work!

## 🖊️ Citation

If you find this project useful in your research, please consider cite:
```
```

## 💳 License

This project is released under the Apache 2.0 [license](./LICENSE).