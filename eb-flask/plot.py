import pandas as pd 
import numpy as np


def zip_list (zipcode):

    df_plot = pd.read_csv('data-clean.csv')

    bins = [0,50,100,150,200,300,400,500,750,1000,50000]

    df_plot = df_plot.loc[df_plot['zipcode'] ==zipcode]

    digitized = np.digitize(df_plot['total_price'], bins)
    bin_counts = [df_plot['total_price'][digitized == i].count() for i in range(1, len(bins))]

    return bin_counts



