import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import missingno


def load_and_process(df):
    df1 = (
        pd.read_csv(df)
        .dropna()
        .rename(columns={'dteday':'Date','yr':'Year','cnt':'Total','hum':'Humidity','mnth':'Month','windspeed':'Windspeed','temp':'Temperature',
                        'season':'Season','holiday':'Holiday','weathersit':'Weather Situation'
                        })
  
    )
    
    df2 = (
        df1.drop(columns=['instant','atemp'])
            .assign(Ratio = df1['casual']/df1['registered'])
    )
    
    df2['Season'] = df2['Season'].replace([1], ['Winter'])
    df2['Season'] = df2['Season'].replace([2], ['Spring'])
    df2['Season'] = df2['Season'].replace([3], ['Summer'])
    df2['Season'] = df2['Season'].replace([4], ['Fall'])
    
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
    
    df2['Weather Situation'] = df2['Weather Situation'].astype(str)
    df2['Weather Situation'] = df2['Weather Situation'].replace(['1'], ['Sunny'])
    df2['Weather Situation'] = df2['Weather Situation'].replace(['2'], ['Cloudy'])
    df2['Weather Situation'] = df2['Weather Situation'].replace(['3'], ['Rain/Snow'])
    
    df2['Season'] = df2['Season'].astype('category')
    df2['Month'] = df2['Month'].astype('category')
    df2['weekday'] = df2['weekday'].astype('category')
    df2['Weather Situation'] = df2['Weather Situation'].astype('category')
    return df2

   
    
def categorical_data(df):
        print("\nUnique count of each category\n")
        print(df.select_dtypes(include=['object', 'category']).nunique())
        for col in df.select_dtypes(include='category').columns:
            fig = sns.catplot(x=col, kind="count", data=df)
            fig.set_xticklabels(rotation=90)
            plt.show()

def numeric_data(df):
        print("\nDistribution of numeric data")
        display(df.describe().T)
        plt.figure(figsize=(14,12))
        sns.heatmap(df.corr(),linewidths=.1,cmap="YlGnBu", annot=True)
        plt.yticks(rotation=0);
        sns.pairplot(df)    
    
    
def eda(df):
    
    
    
    print("Preview of data:")
    display(df.head(10))

    print("\nTo check: \n (1) Total number of entries \n (2) Column types \n (3) Any null values\n")
    print(df.info())
    
    print('Number of rows and columns:')
    print(df.shape)
    
    categorical_data(df)
    numeric_data(df)
