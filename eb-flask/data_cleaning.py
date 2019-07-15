import pandas as pd 
import numpy as np 
import os

df = pd.read_csv('data.csv')
print(df.head())

def clean_zips(df):
    """A helper function to clean zip code columns for Los Angeles Airbnb Data"""
    
    def first_ele(df):
        for i in df:
            return i
    
    def first_five(df):
        return df[2:7]
    
    # Splits data for entries containing period
    df['zipcode'] = df['zipcode'].str.split('.')

    # Transform all values into strings
    df['zipcode'] = df['zipcode'].apply(str)
    
    # Returns only the first five characters
    df['zipcode'] = df['zipcode'].map(first_five)

    df = df.loc[df['zipcode'] != 'n']
    print(df.head())
    
    return df

def clean_price(df):

  df['price'] = df['price'].str.strip('$')
  df['cleaning_fee'] = df['cleaning_fee'].str.strip('$')

  df['price'] = df['price'].str.replace(',', '')
  df['cleaning_fee'] = df['cleaning_fee'].str.replace(',', '')

  df['cleaning_fee'] = df['cleaning_fee'].replace(np.nan, 0)

  df['price'] = df['price'].astype(float)
  df['cleaning_fee'] = df['cleaning_fee'].astype(float)

  df['total_price'] = df['price'] + df['cleaning_fee']
  df = df.drop(['price', 'cleaning_fee'], axis=1)

  df = df[df['total_price'] > 1]

  # Log transform total price
  df['price_log'] = df['total_price'].apply(lambda x: np.log(x))

  return df

def clean_data(df):

  # Drop columns containing null values
  df = df.dropna()

  return df

if __name__ == '__main__':
  df = clean_data(clean_price(clean_zips(df)))
  df.to_csv('data-clean.csv',index=False)
  os.remove("data.csv") 
  print("Old CSV File Removed!")








