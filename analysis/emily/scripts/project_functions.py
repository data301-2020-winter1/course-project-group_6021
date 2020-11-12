import pandas as pd
import numpy as np
from numpy import nan as NA

def load_and_process(dataset):
    df1 = (
        pd.read_csv(dataset)
        .dropna()
        .rename(columns={'dteday':'date','yr':'year', 'mnth': 'month', 'weathersit': 'weather', 'temp':'temprature', 'hum':'humidity', 'casual': 'casual_users', 'registered': 'registered_users','cnt':'Total'})

    )
    
    df2 = (
        df1.drop(columns=['instant', 'atemp'])
            .assign(Ratio = df1['casual']/df1['registered'])
    )
    
    return df2