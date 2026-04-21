# retreat_2026

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/)
[![Orcid: Jakob](https://img.shields.io/badge/Jakob-bar?style=flat&logo=orcid&labelColor=white&color=grey)](https://orcid.org/0000-0002-2841-7284)

Analysis notebooks and scripts for the 2026 Hasuer Group retreat. Covers scikit-learn models that needs some love

## Getting started

Clone the repo, then install dependencies:

### with uv (recommended)

```bash
uv sync
```

### with pip

```bash
pip install -e .
```

## Other legitimately useful methods

 - 🐋 SGDRegressor  / SGDClassifier
   - legitimate simple online learning

 - 🐬 Graphical Lasso
   - conditional dependence and sparse precision

  - 🫍 Gaussian Processes
    - massively underrated for small non-linear data with uncertainty
 - 🦭 Non-negative Matrix Factorization (NMF)
    - hugely useful when data is nonnegative and additive especially compared to PCA
 - 🦦 Isotonic Regression
    - Data only go up but difficult to fit
 - 🐻‍❄️ GaussianMixture
   - Probability clustering with highly interpretable generative view of data
