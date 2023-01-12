## Python test file for flask to test locally
import requests as r
import pandas as pd
import json


base_url = 'http://127.0.0.1:5000/' #base url local host


json_data = [
    {
    "Gender" : "Male",
    "Married" : "Yes",
    "Dependents" : "3+",
    "Education" : "Not Graduate",
    "Self_Employed" : "No",
    "LoanAmount" : 70,
    "Loan_Amount_Term" : 180.0,
    "Credit_History" : 0,
    "Property_Area" : "Urban",
    "Total_Income" : 4611,
    }
]

# Get Response
# response = r.get(base_url)
response = r.post(base_url + "predict", json = json_data)


if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print(response.json())
    print('request failed')

