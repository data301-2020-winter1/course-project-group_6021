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
    
    return df2

def ten_pop_days_twelve(dataset):
    df1 = load_and_process(dataset)
    
    dfh = df1[df1["Year"] == 1]
    
    df2 = dfh[["Month", "Date", "Total"]]
    
    return df2


def ten_pop_days_eleven(dataset):
    df1 = load_and_process(dataset)
    
    dfh = df1[df1["Year"] == 0]
    
    df2 = dfh[["Month", "Date", "Total"]]
    
    return df2



def tpd(dataset):
    df = ten_pop_days(dataset)
    
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
    
def newT(dataset):
    df = load_and_process(dataset)
    
    df = df.drop(columns=['season', 'temp', 'atemp', 'hum', 'windspeed', 'Ratio'])
    
    df = df.rename(columns={'holiday':'Holiday', 'weekday':'Weekday', 'workingday':'WorkingDay', 'casual':'Casual', 'registered':'Registered'})
    
    df['Month'] = df['Month'].astype(str)
    df['Month'] = df['Month'].replace(['1'], ['Jan'])
    df['Month'] = df['Month'].replace(['2'], ['Feb'])
    df['Month'] = df['Month'].replace(['3'], ['March'])
    df['Month'] = df['Month'].replace(['4'], ['April'])
    df['Month'] = df['Month'].replace(['5'], ['May'])
    df['Month'] = df['Month'].replace(['6'], ['June'])
    df['Month'] = df['Month'].replace(['7'], ['July'])
    df['Month'] = df['Month'].replace(['8'], ['Aug'])
    df['Month'] = df['Month'].replace(['9'], ['Sept'])
    df['Month'] = df['Month'].replace(['10'], ['Oct'])
    df['Month'] = df['Month'].replace(['11'], ['Nov'])
    df['Month'] = df['Month'].replace(['12'], ['Dec'])
    
    df['Weekday'] = df['Weekday'].astype(str)
    df['Weekday'] = df['Weekday'].replace(['0'], ['Sun'])
    df['Weekday'] = df['Weekday'].replace(['1'], ['Mon'])
    df['Weekday'] = df['Weekday'].replace(['2'], ['Tues'])
    df['Weekday'] = df['Weekday'].replace(['3'], ['Wed'])
    df['Weekday'] = df['Weekday'].replace(['4'], ['Thur'])
    df['Weekday'] = df['Weekday'].replace(['5'], ['Fri'])
    df['Weekday'] = df['Weekday'].replace(['6'], ['Sat'])
    
    df['WeatherSituation'] = df['WeatherSituation'].astype(str)
    df['WeatherSituation'] = df['WeatherSituation'].replace(['1'], ['Sunny'])
    df['WeatherSituation'] = df['WeatherSituation'].replace(['2'], ['Cloudy'])
    df['WeatherSituation'] = df['WeatherSituation'].replace(['3'], ['Rain/Snow'])
    
    df['Holiday'] = df['Holiday'].astype(str)
    df['Holiday'] = df['Holiday'].replace(['0'], ['False'])
    df['Holiday'] = df['Holiday'].replace(['1'], ['True'])
    
    df['WorkingDay'] = df['WorkingDay'].astype(str)
    df['WorkingDay'] = df['WorkingDay'].replace(['0'], ['False'])
    df['WorkingDay'] = df['WorkingDay'].replace(['1'], ['True'])
    
    df['Year'] = df['Year'].replace([0], [2011])
    df['Year'] = df['Year'].replace([1], [2012])
    
    return df