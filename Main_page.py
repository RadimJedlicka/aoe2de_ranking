from datetime import date

import streamlit as st
import pandas as pd


st.header('AoE2 DE ranking')


df = pd.read_csv('all_dataframes.csv')

df = df[
    ['rank', 'name', 'country', 'rating', 
     'games', 'wins', 'losses', 
     'highest_rating', 'lowest_streak', 'highest_streak', 'Timestamp']
]

df['winratio'] = (100*(df['wins']) /  df['games'])

df = df[
    ['rank', 'name', 'country', 'rating', 
     'games', 'wins', 'losses', 'winratio',
     'highest_rating', 'lowest_streak', 'highest_streak', 'Timestamp']
]

df.winratio = df.winratio.round(2)

df['DateTime'] = pd.to_datetime(df['Timestamp'])
df['Date'] = df['DateTime'].dt.date

df.drop(['Timestamp', 'DateTime'], axis=1, inplace=True)
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

today = date.today()
df.loc[(df['Date'] == str(today))]

# st.dataframe(df)