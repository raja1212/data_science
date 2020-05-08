import pandas as pd
import tensorflow as tf
import numpy as np


def extract_n_save_germany_data():
    df = pd.read_csv('data/covid_19_data.csv')
    filt_germany = (df['Country/Region'] == 'Germany') 
    df = df[filt_germany]
    df.drop_duplicates(inplace=True)
    # dropping State because its NaN and Country since its fixed value : Germany
    df.drop(columns=['Province/State', 'Country/Region'], inplace=True)
    #dropping Last Update column since it won't help in forecasting
    df.drop(columns='Last Update', inplace=True)
    #set SNo as index
    df.set_index('SNo', inplace=True)
    #convert Object type of ObservationDate to DateTime
    df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
    #Sorting the sequence based on the observation date
    df.sort_values('ObservationDate', inplace=True)
    #visualize observation date with confirmed cases
    data = df['Confirmed']
    data.index = df['ObservationDate']
    data = data.values
    data = data.astype(np.float32)
    np.savetxt('./data/germany.csv', data, delimiter=',')