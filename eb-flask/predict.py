import os 
import json
import numpy as np
import pandas as pd
import dill as pickle
import math
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import category_encoders as ce
from sklearn.linear_model import RidgeCV

import warnings
warnings.filterwarnings("ignore")


""" Python file containing predict function """

with open('./model_v1.pk','rb') as f:
  model = pickle.load(f)
with open('./cols.pk','rb') as f:
  cols = pickle.load(f)
with open('./num_preprocessor.pk','rb') as f:
  num_preprocessor = pickle.load(f)
with open('./cat_preprocessor.pk','rb') as f:
  cat_preprocessor = pickle.load(f)


def get_prediction(zipcode, property_type, room_type, accommodates=2,
                   bathrooms=1.0, bedrooms=1.0, beds=2.0, bed_type="Real Bed"):
    
    data = {"zipcode" : zipcode,
             "property_type": property_type,
             "room_type" : room_type,
             "accommodates": accommodates,
             "bathrooms": bathrooms,
             "bedrooms": bedrooms,
             "beds": beds,
             "bed_type": bed_type}

    # Create dataframe from JSON dict
    data = pd.DataFrame.from_dict([data])
    
    num_cols = ['accommodates', 'bathrooms', 'bedrooms', 'beds']
    cat_cols = ['zipcode', 'property_type', 'room_type','bed_type']
    
    # Seperate into Numeric and Categorical columns
    df_num = data[num_cols]
    df_cat = data[cat_cols]
     
    # Use train data preprocessor
    cat_transformed = cat_preprocessor.fit_transform(df_cat)
    
    # Use train data preprocessor
    num_transformed = num_preprocessor.fit_transform(df_num)
    num_transformed = pd.DataFrame(num_transformed, columns=num_cols)
    
    # Concatenate numeric and categorical dataframes
    df_transformed = pd.concat((num_transformed, cat_transformed), axis=1)
    # Create blank dataframe using columns from transformed train data
    df_blank = pd.DataFrame(columns=cols)
    
    # Concatenate  
    df_model = pd.concat((df_blank, df_transformed))
    df_model = df_model.replace(np.nan, 0)
    
    y_pred = model.predict(df_model)
    prediction = math.exp(y_pred[0])
    
    return prediction

#print(get_prediction(zipcode='91304', property_type='Apartment', room_type='Private room', bathrooms=2.0, bedrooms=1.0, beds=2.0, bed_type="Real Bed"))