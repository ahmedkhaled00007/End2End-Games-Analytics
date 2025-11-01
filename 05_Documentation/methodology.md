# Methodology

The methodology follows a structured **end-to-end pipeline**:

## 1. Data Acquisition
- Raw datasets collected from gaming databases (CSV, Excel, or APIs).  
- Stored in the `01_Data/raw` folder.

## 2. Data Cleaning & Preprocessing
- Handled missing values using imputation.  
- Encoded categorical variables using `LabelEncoder` and `OneHotEncoder`.  
- Scaled numerical features with `StandardScaler`.  
- Stored cleaned datasets in `01_Data/processed`.

## 3. Exploratory Data Analysis (EDA)
- Visualized data distributions, trends, and correlations using `matplotlib` and `seaborn`.  
- Identified top-selling genres, platforms, and publishers.  
- Checked relationships between sales regions and game characteristics.

## 4. SQL Analysis
- Loaded cleaned data into **SQL Server**.  
- Answered business questions using SQL queries (aggregations, rankings, filtering).  
- Example analyses: top-selling games, publisher performance, regional trends.

## 5. Power BI Visualizations
- Created interactive dashboards to visualize sales, genre performance, and publisher impact.  
- Enabled filtering, slicers, and dynamic visuals for insights.

## 6. Machine Learning
- Built classification models to predict game categories or success levels.  
- Built regression models for predicting sales amounts.  
- Used pipelines for preprocessing, model training, and evaluation.  
- Models used: `RandomForestClassifier`, `LinearRegression`.  
- Evaluated with metrics like `accuracy`, `F1-score`, `R²`, and `MAE`.

## 7. Deployment
- Saved models with `pickle` for future inference.  
- Deployment-ready pipeline allows input of new game data for predictions.
S