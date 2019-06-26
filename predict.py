import pandas as pd 
import math
import numpy as np

""" Python file containing predict function """

#def get_prediction(zipcode, property_type, room_type, accommodates=2,
#                   bathroom=1, bedrooms=1, beds=2, bed_type="Real Bed"):
#    """ Determines the price of an Airbnb listing """
#    pass

def get_prediction(zipcode, property_type, room_type, accommodates=2,
                   bathroom=1, bedrooms=1, beds=2, bed_type="Real Bed"):
    
    data = {"zipcode" : zipcode,
             "property_type": property_type,
             "room_type" : room_type,
             "accommodates": accommodates,
             "bathrooms": bathroom,
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