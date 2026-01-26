# House Prices: Advanced Regression Techniques

> Predicting house prices using advanced regression techniques with comprehensive EDA, feature engineering, and model optimization.

[![Kaggle](https://img.shields.io/badge/Kaggle-Competition-20BEFF?style=flat&logo=kaggle)](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

## 📋 Project Overview

This project explores key factors affecting home values and builds optimized regression models for accurate price forecasting. The analysis includes:

- **Exploratory Data Analysis (EDA)** - Understanding data distributions, correlations, and patterns
- **Data Cleaning & Preprocessing** - Handling missing values, outliers, and data transformations
- **Feature Engineering** - Creating new features, logarithmic transformations, and temporal features
- **Model Training & Optimization** - Linear models (ElasticNet) and ensemble methods (Gradient Boosting)
- **Hyperparameter Tuning** - GridSearchCV optimization for best model performance
- **Feature Selection** - SelectKBest and SelectFromModel for dimensionality reduction

**Data Source:** [Kaggle House Prices Competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

## 📁 Project Structure
```
house-prices-advanced-regression-analysis/
│
├── .idea/                            # IDE configuration files (PyCharm/IntelliJ)
│
├── data/
│   ├── raw/                          # Original datasets from Kaggle
│   ├── processed/                    # Cleaned and preprocessed data
│   │   ├── train_postprocessed.csv
│   │   └── test_postprocessed.csv
│   ├── predictions/                  # Model prediction outputs
│   │   └── model_predictions.csv
│   ├── data_description.txt          # Dataset documentation
│   └── data.py                       # Data cleaning and preparation script
│
├── notebooks/
│   ├── 00_eda.ipynb                  # Initial exploratory data analysis
│   ├── 01_eda.ipynb                  # Advanced EDA and visualizations
│   ├── 02_models.ipynb               # Baseline model training
│   ├── 03_resultsAnalysis.ipynb      # Results analysis and comparisons
│   ├── 04_feature_engineering_optimization.ipynb  # Feature engineering & tuning
│   ├── best_enet_pipeline.pkl        # Saved ElasticNet model
│   └── best_gb_pipeline.pkl          # Saved Gradient Boosting model
│
├── plots/                            # Generated visualizations and charts
│
├── reports/                          # LaTeX project documentation
│   └── [LaTeX source files]          # Technical report and analysis documentation
│
├── src/                              # Source code modules
│   └── [Python modules]              # Reusable functions and classes
│
├── text-data/                        # Text-based data files and descriptions
│
├── env/                              # Virtual environment (not tracked in git)
│
└── README.md                         # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/yourusername/house-prices-analysis.git
   cd house-prices-analysis
```

2. **Create and activate virtual environment:**
```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

4. **Download data:**
   - Download the dataset from [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
   - Place files in `data/raw/`

## 📊 Workflow

### 1. Data Preparation (`data/data.py`)
- Handle missing values
- Remove outliers
- Initial data transformations

### 2. Exploratory Data Analysis (`00_eda.ipynb`, `01_eda.ipynb`)
- Analyze distributions and correlations
- Identify key features affecting house prices
- Visualize relationships between variables

### 3. Model Training (`02_models.ipynb`)
- Baseline models: Linear Regression, Ridge, ElasticNet
- Ensemble models: Random Forest, Gradient Boosting, XGBoost
- Initial performance comparison

### 4. Feature Engineering & Optimization (`04_feature_engineering_optimization.ipynb`)
- **Logarithmic transformations** for skewed features
- **Temporal features**: house age, years since remodel
- **Cyclical encoding**: month of sale (sin/cos)
- **Interaction features**: combined living area, bathroom count
- **Feature selection**: SelectKBest, SelectFromModel
- **Hyperparameter tuning**: GridSearchCV for optimal parameters

### 5. Results Analysis (`03_resultsAnalysis.ipynb`)
- Compare model performance (RMSE, R², MAE)
- Visualize predictions vs actual values
- Analyze feature importance

## 🎯 Key Features

### Feature Engineering Highlights

- **Log Transformations**: `LotArea`, `LotFrontage`, `MasVnrArea`, `WoodDeckSF`
- **Temporal Features**: `AgeAtSold`, `YearsSinceRemod`, `HouseAge`, `GarageAge`
- **Cyclical Features**: `MoSold_sin`, `MoSold_cos`, `HighSeasonSell`
- **Aggregated Features**: `GrAndBsmtArea`, `Bathrooms`, `QualCondScore`
- **Binary Indicators**: `HasMasVnrArea`, `HasWoodDeckSF`

### Models Implemented

| Model | Type | Best Configuration | Best RMSE | Best R² |
|-------|------|-------------------|-----------|---------|
| **ElasticNet** | Linear | Pipeline (feature engineering) | 0.098 | 0.890 |
| **Gradient Boosting** | Ensemble | Pipeline + Tuning (GridSearchCV) | 0.110 | 0.861 |

## 🔧 Pipeline Components

### Preprocessing Pipeline
```python
- Numerical features: SimpleImputer(median) → StandardScaler
- Categorical features: SimpleImputer(most_frequent) → OneHotEncoder
```

### Feature Selection Methods
- **SelectKBest**: Fast statistical feature selection
- **SelectFromModel**: Model-based feature importance
- **CorrelationFiltering**: Custom correlation-based selector

### Optimization Techniques
- **GridSearchCV**: Exhaustive hyperparameter search
- **Cross-validation**: 5-fold CV for robust evaluation
- **Regularization**: Alpha and L1/L2 ratio tuning

## 📈 Results

The best performing models after optimization:

- **ElasticNet** with feature engineering: RMSE = 0.098, R² = 0.890
- **Gradient Boosting** with feature engineering: RMSE = 0.110, R² = 0.861

Key findings:
- Feature engineering significantly improves model performance
- Log transformations help with skewed distributions
- Temporal features capture house age effects effectively
- Regularization prevents overfitting in linear models

## 📄 Documentation

Complete technical documentation is available in the `reports/` directory in LaTeX format, including:
- Detailed methodology
- Statistical analysis
- Model comparisons
- Feature engineering techniques
- Results and conclusions

## 🛠️ Technologies Used

- **Python 3.8+**
- **pandas** - Data manipulation
- **NumPy** - Numerical computing
- **scikit-learn** - Machine learning models and pipelines
- **Matplotlib/Seaborn** - Data visualization
- **Jupyter Notebook** - Interactive development
- **LaTeX** - Technical documentation

