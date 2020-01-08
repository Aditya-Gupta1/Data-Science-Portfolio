# __Project : Loan Eligibility Prediction__

## Install

This project requires Python 3.x and following libraries installed:

* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [scikit-learn](https://scikit-learn.org/)
* [Seaborn](https://seaborn.pydata.org/)

We will also need to install software to run jupyter notebooks. You can download it from [here](https://www.anaconda.com/distribution/#download-section)

## Problem Statement

Dream Housing Finance company deals in all home loans. They have presence across all urban, semi urban and rural areas. Customer first apply for home loan after that company validates the customer eligibility for loan. Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others. To automate this process, they have given a problem to identify the customers segments, those are eligible for loan amount so that they can specifically target these customers.

It is a **binary** classification problem where we have to predict whether a loan would be approved or not.

## Understanding the Data


* Loan_ID : Unique Loan ID 
* Gender : Male / Female 
* Married : Applicant married (Y/N)
* Dependents : Number of dependents
* Education : Applicant Education (Graduate/Under Graduate)
* Self_Employed : Self employed (Y/N)
* ApplicantIncome : Applicant income
* CoapplicantIncome : Coapplicant income
* LoanAmount : Loan amount in thousands
* Loan_Amount_Term : Term of loan in months
* Credit_History : Credit history meets guidelines
* Property_Area : Urban/ Semi Urban/ Rural
* Loan_Status : Loan approved (Y/N)

## Univariate Analysis

It is the simplest form of analyzing data where we examine each variable individually. For **categorical** features we can use frequency table or bar plots which will calculate the number of each category in a particular variable. For **numerical** features, probability density plots can be used to look at the distribution of the variable.

## Hypothesis Generation

This is a very important stage in any data science/machine learning pipeline. It involves understanding the problem in detail by brainstorming as many factors as possible which can impact the outcome. It is done by understanding the problem statement thoroughly and before looking at the data.

Below are some of the factors which I think can affect the Loan Approval (dependent variable for this loan prediction problem):

 > Salary: Applicants with high income should have more chances of loan approval.
 > Previous history: Applicants who have repayed their previous debts should have higher chances of loan approval.
 > Loan amount: Loan approval should also depend on the loan amount. If the loan amount is less, chances of loan approval should be high.
 > Loan term: Loan for less time period and less amount should have higher chances of approval.
 > EMI: Lesser the amount to be paid monthly to repay the loan, higher the chances of loan approval.

These are some of the factors which i think can affect the target variable, there might be many others which we can think of.

We verify our hypothesis with **Bivariate Analysis**.

## Bivariate Analysis

In this section, we try to test the above mentioned hypothesis by exploring the features with respect to the target variable. We will use bar plots, stacked bar plots and other visualization and statistical techniques to test our hypothesis as done in [this](https://github.com/Aditya-Gupta1/Data-Science-Portfolio/blob/master/2%20-%20Loan%20Prediction/Loan_Prediction.ipynb) project.
We can also see the correlation of features with each other and with the target variable with heatmaps.

## Missing Value and Outlier Treatment

There are missing values in Gender, Married, Dependents, Self_Employed, LoanAmount, Loan_Amount_Term and Credit_History features.

Missing values in all the features will be treated one by one.

We can consider these methods to fill the missing values:

* **For numerical variables:** imputation using mean or median
* **For categorical variables:** imputation using mode

#### Missing Values Treatment

> There are very less missing values in Gender, Married, Dependents, Credit_History and Self_Employed features so we can fill them using the mode of the features.
> It can be seen that in loan amount term variable, the value of 360 is repeating the most. So we will replace the missing values in this variable using the mode of this variable.
> As the LoanAmount variable is a numerical variable, we can use mean or median to impute the missing values. We will use median to fill the null values as earlier we saw that loan amount have outliers so the mean will not be the proper approach as it is highly affected by the presence of outliers.

#### Outlier Treatment

It can be done easily by performing log transformation of the features containing outliers. Log transformations does not affect the smaller values much, but reduces the larger values. So, we get a distribution similar to normal distribution.

## Evaluation Metric

As it is a classification problem with not much skewness, we will use accuracy_score as our evaluation metric.
We can also use Receiver Operating Characteristic(ROC) curve to see the trade-off between the True Positive Rate(sensitivity) and False Positive Rate(1 - specificity). The Area Under Curve(AUC) is a perfect performance metric for ROC curve. More the AUC score, better the predictive power of the model.

## Feature Enginnering

In this section, I performed following steps :

1. One Hot Encode all categorical features.
2. Made new features such as 'Total Income', 'EMI', 'Balance Income' from the existing features.

## Model Building

There are several models that are trained in this section. These are :
* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost

These models are trained using k-Fold Stratified Cross Validation technique.

As a result , **Logistic Regression** maximum accuracy score among all the other models.
