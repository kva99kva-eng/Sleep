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
├── notebooks/
│   ├── 01_sleep_edf_exploration.ipynb
│   ├── 02_sleep_edf_feature_engineering.ipynb
│   ├── 02_5_sleep_edf_build_dataset.ipynb
│   ├── 03_mmash_sleep_mental_health.ipynb
│   └── 04_sleep_deprivation_cognition.ipynb
├── data/
│   ├── raw/
│   │   ├── sleep_edf/
│   │   ├── mmash/
│   │   └── sleep_deprivation/
│   └── processed/
├── figures/
└── outputs/

Notebooks
01_sleep_edf_exploration.ipynb

Exploratory analysis of Sleep-EDF hypnograms and sleep-stage distributions.

02_sleep_edf_feature_engineering.ipynb

Extraction of subject-level sleep features such as:

sleep duration
sleep latency
REM latency
fragmentation
sleep efficiency
stage proportions
02_5_sleep_edf_build_dataset.ipynb

Batch conversion of multiple hypnogram files into a participant-level feature table.

03_mmash_sleep_mental_health.ipynb

Exploratory modeling of associations between sleep quality metrics and stress/anxiety-related questionnaire outcomes in MMASH.

Main outcomes explored:

Daily_stress
STAI1
Pittsburgh
04_sleep_deprivation_cognition.ipynb

Analysis of cognitive performance before and after 24-hour sleep deprivation.

Main tasks:

classification of baseline vs sleep-deprived sessions
paired before-vs-after testing
identification of cognitive metrics most affected by sleep deprivation
Main findings
Sleep-EDF
Built a full preprocessing and feature-engineering pipeline from hypnogram-level sleep staging data.
Generated subject-level sleep features and visualization outputs such as hypnograms and radar charts.
MMASH
Sleep fragmentation metrics showed the strongest exploratory associations with questionnaire-based stress outcomes.
STAI1 showed the most promising predictive signal among the tested questionnaire targets.
Predictive performance remained limited, highlighting the constraints of small-sample wearable datasets.
Sleep deprivation and cognition
The strongest exploratory changes appeared in RVP- and RTI-related cognitive metrics after 24 hours of sleep deprivation.
Paired within-subject analysis suggested directional changes in sustained attention and reaction-time-related measures.
No metric remained significant after multiple-comparison correction, which is consistent with the small sample size.
Methods
Python
pandas
numpy
matplotlib
scikit-learn
scipy
statsmodels
mne
Limitations
Small sample sizes in the open datasets
Exploratory rather than clinical-grade modeling
Heterogeneous datasets with different study designs and outcome types
Next steps
add more signal-derived physiological features
include feature importance and explainability
compare multiple open sleep-related datasets
improve packaging with a dashboard or report-style figures
How to run

Install dependencies:

pip install -r requirements.txt
Open the notebooks in order:
01_sleep_edf_exploration.ipynb
02_sleep_edf_feature_engineering.ipynb
02_5_sleep_edf_build_dataset.ipynb
03_mmash_sleep_mental_health.ipynb
04_sleep_deprivation_cognition.ipynb
Project positioning

This repository is best interpreted as an open-data exploratory sleep analytics portfolio project, not as a clinical decision-making system.

It focuses on:

reproducible preprocessing
interpretable feature engineering
exploratory modeling
careful interpretation of small-sample results