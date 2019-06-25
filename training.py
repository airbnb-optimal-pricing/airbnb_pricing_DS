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

df = pd.read_csv('flask_ready.csv')

X = df.drop(['total_price', 'price_log'], axis=1)
y = df['price_log']

def wrangle(df):  
    num_cols = ['accommodates', 'bathrooms', 'bedrooms', 'beds']
    cat_cols = ['zipcode', 'property_type', 'room_type','bed_type']

    df_num = df[num_cols]
    df_cat = df[cat_cols]

    cat_preprocessor = make_pipeline(ce.OneHotEncoder(use_cat_names=True))

    num_preprocessor = make_pipeline(StandardScaler())

    cat_transformed = cat_preprocessor.fit_transform(df_cat)

    num_transformed = num_preprocessor.fit_transform(df_num)
    num_transformed = pd.DataFrame(num_transformed, columns=num_cols)

    df = pd.concat((num_transformed, cat_transformed), axis=1)

    cols = df.columns

    return df, cols

def fit_model(X, y)

    reg_params = 10.**np.linspace(-10, 5, 10)
    model = RidgeCV(alphas=reg_params, fit_intercept=True, cv=5)
    model.fit(X, y)

    return model


if __name__ == '__main__':
    X, cols = wrangle(X)
    model = fit_model(X,y)

    filename = 'model_v1.pk'
    with open('../'+filename, 'wb') as file:
        pickle.dump(model, file)
        pickle.dump(cols, file)














