# Sleep Neuroscience Project

Exploratory modeling of sleep, stress/anxiety, and cognitive performance using open datasets.

## Project overview

This project explores how sleep-related metrics are associated with mental-health-related questionnaire outcomes and cognitive performance.

The repository contains three main case studies:

1. **Sleep architecture analytics with Sleep-EDF**
   - hypnogram analysis
   - sleep feature engineering
   - sleep quality profiling

2. **Sleep and psychological outcomes with MMASH**
   - participant-level sleep metrics
   - questionnaire-based stress/anxiety outcomes
   - exploratory prediction of stress- and anxiety-related measures

3. **Sleep deprivation and cognition**
   - before-vs-after comparison under 24-hour sleep deprivation
   - cognitive performance analysis using CANTAB-derived metrics
   - paired within-subject testing and condition classification

## Datasets

### 1. Sleep-EDF Expanded
Used for PSG-based sleep stage exploration and feature engineering.

### 2. MMASH
Used for exploratory modeling of associations between sleep quality metrics and stress/anxiety-related questionnaire outcomes.

### 3. Sleep deprivation and cognitive performance dataset
Used to study cognitive changes before and after 24 hours of sleep deprivation.

## Repository structure

```text
sleep-neuroscience-project/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_sleep_edf_exploration.ipynb
│   ├── 02_sleep_edf_feature_engineering.ipynb
│   ├── 02_5_sleep_edf_build_dataset.ipynb
│   ├── 03_mmash_sleep_mental_health.ipynb
│   └── 04_sleep_deprivation_cognition.ipynb
├── figures/
└── outputs/
