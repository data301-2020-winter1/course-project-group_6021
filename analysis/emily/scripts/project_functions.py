import pandas as pd
import numpy as np
from numpy import nan as NA

def load_and_process(dataset):
    df1 = (
        pd.read_csv(dataset)
        .dropna()
        .rename(columns={'weathersit':'WeatherSituation','dteday':'Date','mnth':'Month','yr':'Year','cnt':'Total'})
    )
    
    
    
    df2 = (
        df1.drop(columns=['instant'])
            .assign(Ratio = df1['casual']/df1['registered'])
    )
    
    df2['Month'] = df2['Month'].astype(str)
    df2['Month'] = df2['Month'].replace(['1'], ['Jan'])
    df2['Month'] = df2['Month'].replace(['2'], ['Feb'])
    df2['Month'] = df2['Month'].replace(['3'], ['March'])
    df2['Month'] = df2['Month'].replace(['4'], ['April'])
    df2['Month'] = df2['Month'].replace(['5'], ['May'])
    df2['Month'] = df2['Month'].replace(['6'], ['June'])
    df2['Month'] = df2['Month'].replace(['7'], ['July'])
    df2['Month'] = df2['Month'].replace(['8'], ['Aug'])
    df2['Month'] = df2['Month'].replace(['9'], ['Sept'])
    df2['Month'] = df2['Month'].replace(['10'], ['Oct'])
    df2['Month'] = df2['Month'].replace(['11'], ['Nov'])
    df2['Month'] = df2['Month'].replace(['12'], ['Dec'])
    
    df2['weekday'] = df2['weekday'].astype(str)
    df2['weekday'] = df2['weekday'].replace(['0'], ['Sun'])
    df2['weekday'] = df2['weekday'].replace(['1'], ['Mon'])
    df2['weekday'] = df2['weekday'].replace(['2'], ['Tues'])
    df2['weekday'] = df2['weekday'].replace(['3'], ['Wed'])
    df2['weekday'] = df2['weekday'].replace(['4'], ['Thur'])
    df2['weekday'] = df2['weekday'].replace(['5'], ['Fri'])
    df2['weekday'] = df2['weekday'].replace(['6'], ['Sat'])
    
    df2['WeatherSituation'] = df2['WeatherSituation'].astype(str)
    df2['WeatherSituation'] = df2['WeatherSituation'].replace(['1'], ['Sunny'])
    df2['WeatherSituation'] = df2['WeatherSituation'].replace(['2'], ['Cloudy'])
    df2['WeatherSituation'] = df2['WeatherSituation'].replace(['3'], ['Rain/Snow'])
    
    
    return df2







def ten_pop_days_overall(dataset):
    df1 = load_and_process(dataset)
    
    df2 = df1[["Month", "Date", "Total"]]
    
    return df2



def ten_pop_days_eleven(dataset):
    df1 = load_and_process(dataset)
    
    dfh = df1[df1["Year"] == 0]
    
    df2 = dfh[["Month", "Date", "Total"]]
    
    return df2


def ten_pop_days_twelve(dataset):
    df1 = load_and_process(dataset)
    
    dfh = df1[df1["Year"] == 1]
    
    df2 = dfh[["Month", "Date", "Total"]]
    
    return df2








def tpd(dataset):
    df = ten_pop_days_overall(dataset)
    
    td = df.sort_values('Total', ascending=False)
    
    return td


def tpd_eleven(dataset):
    df = ten_pop_days_eleven(dataset)
    
    td = df.sort_values('Total', ascending=False)
    
    return td

def tpd_twelve(dataset):
    df = ten_pop_days_twelve(dataset)
    
    td = df.sort_values('Total', ascending=False)
    
    return td
def eda(df):
    
    
    
    print("Preview of data:")
    display(df.head(10))

    print("\nTo check: \n (1) Total number of entries \n (2) Column types \n (3) Any null values\n")
    print(df.info())
    
    print('Number of rows and columns:')
    print(df.shape)
    
    categorical_data(df)
    numeric_data(df)

def weatheronly(df):
    df1 = (
        pd.read_csv(df)
        .dropna()
        .rename(columns={'dteday':'Date','yr':'Year','cnt':'Total','hum':'Humidity','mnth':'Month','windspeed':'Windspeed','temp':'Temperature',
                        'season':'Season','holiday':'Holiday','weathersit':'Weather Situation'
                        })
  
    )