# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals

    Deploying a Model to automate the loan eligibility process based on customer details that are provided as online application forms are being filled. These details concern the customer's Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History.

## Hypothesis
#### Possible hypotheses

    1. Applicants having a credit history more likely get approval, vice-versa. Credit history showing reliable informations of applicants income, spending and saving.
    - Plotting hist graph to compare between group

    2. Applicants with higher applicantincome and co-applicantincome has more more likely get approval. Income is evidently showing their ability to pay back their loan
    - Calculate the total_income(Applicantincome + co-ApplicantIncome) and ploting hist graph

    3. Applicants graduated is likely to be considered to Loan status decision. applicants  graduated is likely to get higher income and secure job which is showing their ability to pay back their loan soon.
    - Plotting hist graph to compare groups

    4. Semiurbun applicants has higher change to get approval, they are in high growth perspectives. Also, rural applicants might spend less than Urban applicants.
    - Plotting hist graph to compare groups

    5. Applicants with self_employed are likely to get approval. If they own a business. For those self_employed they will have high income.
    - Plotting hist graph to compare groups

    6. Applicants have more dependants likely get refused to loan decision. They have to spend more than other groups.
    - Plotting hist graph to compare groups

## EDA 
    1. Applicants having a credit history more likely get approval

    2. Applicants with higher applicantincome and co-applicantincome has more more likely get approval

    3. Applicants graduated is likely not to be considered to Loan status decision

    4. Semiurbun applicants has higher change to get approval, they are in high growth perspectives. Also,    rural applicants might spend less than Urban applicants.

## Process
    1. EDA & cleaning
    - Initial cleaning includes fill nan values with mean, median, mode
    - EDA includes grouping and visualization to test and determine the hypothesises
    2. Feature Engineering
    - numeric tranforming
    - variable tranforming
    - categories transforming
    3. Modeling
    - deploying Pipeline inlcudes numeric, variable, categories tranforming
    - deploying PCA, KBest, prediction model
    4. Deploying
    - Flask on Local
    - Flask on AWS
    4. Testing
    - Using Postpone send request

## Results/Demo
    - Model able to predict 76% accuracy
    - API: Using Flask to create rest api which able to take POST requests with param json data from clients, then send back the pre-approval credit decison.

## Challanges 
    - A 2-days project definitely is not enough time to work extra on EDA
    - Modeling is difficult if we want to use the raw data from customer input

## Future Goals
    - Definitely spending more time to do EDA and Modeling, that will imporve predictive power