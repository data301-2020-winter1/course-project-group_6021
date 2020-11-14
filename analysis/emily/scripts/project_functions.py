#Created a module

import pandas as pd
import numpy as np
from numpy import nan as NA

def load_and_process(dataset):
    df1 = (
        pd.read_csv(dataset)
        .dropna()
        .rename(columns={'dteday':'date','yr':'year','mnth': 'month','weathersit': 'weather','temp':'temprature','hum':'humidity','cnt':'Total'})

    )
    
    df2 = (
        df1.drop(columns=['instant', 'atemp'])
            .assign(Ratio = df1['casual']/df1['registered'])
    )
    
    return df2



import pandas as pd
import numpy as np
from numpy import nan as NA

def load_and_process(dataset):
    df1 = (
        pd.read_csv(dataset)
        .dropna()
        .rename(columns={'dteday':'Date','yr':'Year','cnt':'Total'})
        
    )
    
    df2 = (
        df1.drop(columns=['instant'])
            .assign(Ratio = df1['casual']/df1['registered'])
    )
    
    return df2