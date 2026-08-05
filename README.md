# QualAlign

**QualAlign: Benchmarking Automated Qualitative Coding Against Human Schemas**

Official dataset and evaluation companion for our [COLM 2026](https://colm.eventhosts.cc/Conferences/2026/AcceptedPapers) paper.

> Taggert Smith\*, Chuong Nguyen\*, Qisen Yang, Oishani Bandopadhyay, Yaru Su, Nadia Polikarpova, Xinyu Pi  
> \*Equal contribution

QualAlign benchmarks how well automated methods (including LLMs) can perform **qualitative coding** when evaluated against **human-authored schemas** across multiple real research domains.

<!-- Optional: add arXiv / OpenReview / Hugging Face links when available
[Paper](https://arxiv.org/abs/XXXX.XXXXX) · [Data](https://huggingface.co/datasets/...) · [OpenReview](...)
-->

## Dataset overview

Eight publicly curated qualitative coding domains. Each domain includes research questions and chunk-level annotations with human codes.

| Domain | Chunks | Codes | Notes |
|--------|-------:|-------|-------|
| `adhd_reddit` | 154 | `code_1`–`code_3` | Adult ADHD technology use (Reddit) |
| `data_sharing` | 349 | `code_1`–`code_3` | Scientist data sharing interviews |
| `mental_health` | 591 | `code_1`–`code_3` | Mental health narratives (+ source metadata) |
| `patient_deterioration` | 81 | `code_1`–`code_2` | Clinical deterioration recognition |
| `scrum_quality` | 249 | `code_1`–`code_2`, theme | Scrum / software quality interviews |
| `search_systems` | 327 | `code_1`–`code_3` | Systematic search platforms |
| `shuffle_music` | 784 | `code_1`–`code_3` | Personal music listening |
| `stroke_wearables` | 852 | `code_1`–`code_2` | Stroke rehab wearables |
| **Total** | **3,387** | | |

Data lives under [`benchmark_dataset/`](benchmark_dataset/). See [`benchmark_dataset/README.md`](benchmark_dataset/README.md) for schema details and per-domain research questions.

## Repository structure

```text
HumanAlignment-Dataset/
├── README.md                 # this file
├── LICENSE                   # MIT (code)
├── CITATION.cff              # cite this work
├── requirements.txt
├── benchmark_dataset/        # QualAlign domains
│   ├── README.md
│   └── <domain>/
│       ├── research_questions.txt
│       └── train_data_w_gt.csv
├── src/qualalign/            # loaders & evaluation (WIP)
└── scripts/                  # reproduction entrypoints (WIP)
```

## Setup

```bash
git clone https://github.com/chuongnguyen26/HumanAlignment-Dataset.git
cd HumanAlignment-Dataset
pip install -r requirements.txt
```

## Quick load

```python
import pandas as pd

df = pd.read_csv("benchmark_dataset/mental_health/train_data_w_gt.csv")
print(df.head())
```

## Evaluation

Evaluation scripts and official metrics from the paper will be released here (WIP).

```bash
# Coming soon
# python scripts/run_eval.py --domain all
```

## Results

Baseline results from the paper will be listed here with the exact commands used to reproduce them (WIP).

| Method | Metric | Score |
|--------|--------|------:|
| TBD    | TBD    | TBD   |

## Citation

Paper accepted at [COLM 2026](https://colm.eventhosts.cc/Conferences/2026/AcceptedPapers). Formal BibTeX (with arXiv / proceedings details) will be added here once the camera-ready version is public.
## License

Code is released under the [MIT License](LICENSE).  
Dataset reuse may be subject to the licenses of the original qualitative studies; see domain notes in [`benchmark_dataset/README.md`](benchmark_dataset/README.md).

## Contact

For questions about the benchmark, open an issue or contact the authors.
