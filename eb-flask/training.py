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

# Import cleaned data
df = pd.read_csv('flask_ready.csv')

# Seperate features from target variable
X = df.drop(['total_price', 'price_log'], axis=1)
y = df['price_log']

num_cols = ['accommodates', 'bathrooms', 'bedrooms', 'beds']
cat_cols = ['zipcode', 'property_type', 'room_type','bed_type']

def transform_data(df):
  """
  Creates transformed dataframe with:
    -One-hot-encoded categorical features
    -Scaled numerical features

  Creates list with all column names of transformed dataframe 
  """  
  df_num = df[num_cols]
  df_cat = df[cat_cols]

  cat_preprocessor = make_pipeline(ce.OneHotEncoder(use_cat_names=True))

  num_preprocessor = make_pipeline(StandardScaler())

  cat_transformed = cat_preprocessor.fit_transform(df_cat)

  num_transformed = num_preprocessor.fit_transform(df_num)
  num_transformed = pd.DataFrame(num_transformed, columns=num_cols)

  df = pd.concat((num_transformed, cat_transformed), axis=1)

  cols = df.columns

  return df, cols, num_preprocessor, cat_preprocessor

def fit_model(X, y):
  """
  Fits model to data
  """
  reg_params = 10.**np.linspace(-10, 5, 10)
  model = RidgeCV(alphas=reg_params, fit_intercept=True, cv=5)
  model.fit(X, y)

  return model


if __name__ == '__main__':
  """
  Pickles model and column list
  """
  X, cols, num_preprocessor, cat_preprocessor = transform_data(X)
  model = fit_model(X,y)

  filename_model = 'model_v1.pk'
  with open('../'+filename_model, 'wb') as file:
    pickle.dump(model, file)
    
  filename_cols = 'cols.pk'
  with open('../'+filename_cols, 'wb') as file:
    pickle.dump(cols, file)

  file_name_numpre = 'num_preprocessor.pk'
  with open('../'+file_name_numpre, 'wb') as file:
    pickle.dump(num_preprocessor, file)

  file_name_catpre = 'cat_preprocessor.pk'
  with open('../'+file_name_catpre, 'wb') as file:
    pickle.dump(cat_preprocessor, file)














