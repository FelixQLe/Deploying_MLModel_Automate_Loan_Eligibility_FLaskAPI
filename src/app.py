from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator,TransformerMixin

from sklearn.feature_selection import SelectKBest
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import RidgeClassifier



# App definition
app = Flask(__name__)

#extract columns
label_cols = ['Gender','Married', 'Self_Employed', 'Education', 'Property_Area']
log_scale_cols = ['LoanAmount', 'Total_Income']
depep_cols = ['Dependents']
loan_cols = ['Loan_Amount_Term']

#Log function
def log_transform(x):
    return np.log(x + 1)

# Labelencoder to Gender_transform, Married_transform, Self_Eployed_transform, Edu_transform(x):
    
def Loan_term(X):
    X = X/12
    return X.astype(int)

def Dependents_transform(X):
    col = 'Dependents'
    conditions  = [X == '0', X == '3+']
    
    X = np.select(conditions, [0,2], default=1)
    
    return X

class CustomLabelEncode(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X ,y=None):
        le=LabelEncoder()
        for i in X[label_cols]:
            X[i]=le.fit_transform(X[i])
        return X

# importing models
with open('/Users/hople/Desktop/Bootcamp Lectures/week_7/mini-project-4/Model_Pickle/credit_classifier.pkl', 'rb') as f:
   credit_predict = pickle.load(f)

#webpage
@app.route('/')
def welcome():
   return "Welcome! Use this Flask App for Credit pre-determination"

@app.route('/predict', methods=['POST','GET'])
def predict():

   if flask.request.method == 'GET':
       return "Prediction page. Try using post with params to get specific prediction. Format data to pandas dataframe"
                

   if flask.request.method == 'POST':
       try:
           json_ = request.json # '_' since 'json' is a special word
           print(json_)
           query_pd = pd.DataFrame(json_)
           #query = query_#.reindex(columns = model_columns, fill_value= 0)
           prediction = list(credit_predict.predict(query_pd))

           return jsonify({
               "prediction":str(prediction)
           })

       except:
           return jsonify({
               "trace": traceback.format_exc()
               })



if __name__ == "__main__":
   app.run()

