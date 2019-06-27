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
df = pd.read_csv('flask_ready_property_type.csv')

# Seperate features from target variable
X = df.drop(['total_price', 'price_log'], axis=1)
y = df['price_log']

X_2 = df.drop(['total_price', 'price_log'], axis=1)

num_cols = ['accommodates', 'bathrooms', 'bedrooms', 'beds']
cat_cols = ['zipcode', 'property_type', 'room_type','bed_type']

num_cols_simp = ['bedrooms', 'bathrooms']
cat_cols_simp = ['zipcode']

def transform_data(df, num_cols, cat_cols):
  """
  Creates transformed dataframe with:
    -One-hot-encoded categorical features
    -Scaled numerical features

  Creates list with all column names of transformed dataframe 
  """  
  print(df.head())
  df_num = df[num_cols]

  if len(cat_cols) == 1:
    df_cat = pd.DataFrame(df, columns=cat_cols)
  else:
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
  Pickles model,column list, and data preprocessors
  """
  # Premium Model
  X, cols, num_preprocessor, cat_preprocessor = transform_data(X, num_cols=num_cols, cat_cols=cat_cols)
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

  # Simple Model
  X_simp, simp_cols, simp_num_preprocessor, simp_cat_preprocessor = transform_data(X_2, num_cols=num_cols_simp, cat_cols=cat_cols_simp)
  simp_model = fit_model(X_simp,y)

  filename_simp_model = 'simp_model_v1.pk'
  with open('../'+filename_simp_model, 'wb') as file:
    pickle.dump(simp_model, file)
    
  filename_simp_cols = 'simp_cols.pk'
  with open('../'+filename_simp_cols, 'wb') as file:
    pickle.dump(simp_cols, file)

  file_name_simp_numpre = 'simp_num_preprocessor.pk'
  with open('../'+file_name_simp_numpre, 'wb') as file:
    pickle.dump(simp_num_preprocessor, file)

  file_name_simp_catpre = 'simp_cat_preprocessor.pk'
  with open('../'+file_name_simp_catpre, 'wb') as file:
    pickle.dump(simp_cat_preprocessor, file)
















