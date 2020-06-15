# Software Engineer Salary Prediction

### Overview
- Created a model to help Software Engineers estimate their expected salary
- Web scrapped over 1000 job descriptions from glassdoor using Selenium
- Cleaned the data and engineered new features to identify how skills and seniority level affect salary
- Utilized and optimized Lasso and Random Forest Regressor using GridsearchCV

This project is based on a tutorial by Ken Jee:

https://www.youtube.com/watch?v=MpF9HENQjDo&t=1s

## Code and Resources
__Python version__: 3.7
__Packages__: pandas, numpy, sklearn, matplotlib, seaborn, selenium
__Scrapper__: https://github.com/arapfaik/scraping-glassdoor-selenium


## Web Scrapping
Scrapped 1000 job psotings from glassdoor and obtianed the following:
- Job title
- Salary Estimate
- Job Description
- Rating
- Company
- Location
- Company Headquarters
- Company Size
- Company Founded Date
- Type of Ownership
- Industry
- Sector
- Revenue
- Competitors


## Data Cleaning and Feature Engineering
- Parsed salary range and calculated its average (numeric) out of Salary Estimate 
- Removed rows without salary
- Extracted companies' state (US) from Location
- Made a new column for the age of companies
- Extracted different skills from job description and put them on new columns. These include _java, C++, python, PHP, SQL, html, CSS, javascript_
- Extracted seniority category from job titles


## EDA
Few Highlight:


## Model
I transformed the categorical variables into dummy variables and split them into train and test sets (80%&20%).

I chose Lasso and Random Forest Regression for the prediction, implemented using scikit-learn with MAE as the evaluation score. I utilized GridSearchCV to find the best estimators.

## Performance (MAE)
- Lasso Regression: -17.757
- Random Forrest: -18.049
