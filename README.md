# Sleep, Mental Health and Cognition Analysis

Author: Victoria Kupina
Role: Data Analyst / Junior Data Scientist

## Problem Statement

Sleep quality and sleep deprivation can affect cognitive performance and mental health indicators.

This project explores sleep-related datasets and demonstrates how sleep features can be connected with cognition and mental health analysis.

The project is educational and exploratory. It is not a medical diagnostic tool.

## Objectives

- Explore Sleep-EDF data.
- Perform sleep-stage and signal-oriented exploratory analysis.
- Engineer sleep-related features.
- Analyze relationships between sleep, mental health and cognition.
- Explore sleep deprivation and cognitive performance.
- Build a clear neuroscience-oriented data analysis portfolio project.

## Datasets

This project uses sleep and cognition-related datasets, including:

- Sleep-EDF;
- MMASH;
- sleep deprivation and cognition data;
- external CANTAB-style cognitive variables.

Large raw data files are not stored in this repository. Local raw data should be placed in the data/raw/ directory.

## Project Structure

- data/ — local raw and processed data.
- notebooks/ — step-by-step analysis notebooks.
- notebooks/images/ — generated visual outputs.
- scripts/ — helper scripts.
- requirements.txt — Python dependencies.
- README.md — project documentation.
- LICENSE — MIT license.

## Notebooks

| Notebook | Description |
|---|---|
| 01_sleep_edf_exploration.ipynb | Explore Sleep-EDF files and inspect sleep-stage data |
| 02_sleep_edf_visualization.ipynb | Visualize sleep-stage patterns and related features |
| 03_sleep_edf_feature_engineering.ipynb | Engineer sleep features for later analysis |
| 04_mmash_sleep_mental_health.ipynb | Analyze sleep and mental health-related variables |
| 05_sleep_deprivation_cognition.ipynb | Explore sleep deprivation and cognitive performance |

## Methods

- Exploratory data analysis
- Sleep-stage feature engineering
- Descriptive statistics
- Correlation analysis
- Data visualization
- Cognitive performance analysis

## Results

The project demonstrates a complete exploratory workflow connecting sleep data with mental health and cognitive variables.

Current results should be interpreted as exploratory. The project is intended to demonstrate data analysis skills and neuroscience-oriented thinking rather than produce clinical conclusions.

## Visual Results

Generated figures are stored in notebooks/images/.

Examples may include:

- sleep-stage distribution plots;
- sleep feature visualizations;
- cognition-related comparison plots;
- correlation plots.

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- Statsmodels
- Scikit-learn
- MNE
- Jupyter Lab

## How to Run

Clone the repository:

git clone https://github.com/kva99kva-eng/Sleep-Mental-Health-and-Cognition-Analysis.git

Go to the project folder:

cd Sleep-Mental-Health-and-Cognition-Analysis

Create and activate a virtual environment:

python -m venv .venv

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run Jupyter Lab:

jupyter lab

Then run the notebooks in order.

## Limitations

This project is an educational exploratory analysis.

It does not provide:

- medical diagnosis;
- clinical recommendations;
- validated biomarkers;
- production-grade sleep scoring;
- population-level conclusions.

The results should be interpreted as a data analysis demonstration only.

## License

This project is licensed under the MIT License.