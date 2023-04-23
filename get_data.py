import requests
from datetime import datetime
from pprint import pprint
from typing import Dict

import pandas as pd


def get_data_by_api(url: str):

    params = {
        'game': 'aoe2de', 
        'leaderboard_id': '3', 
        'start':'1',
        'count':'100'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
    else:
        print('Chyba při získávání dat')
    
    return data


def make_dataframe(data: Dict[str, str]) -> pd.DataFrame:
    # Creating a DataFrame from the dictionary
    df = pd.DataFrame(data['leaderboard'])
    
    # Adding a column with the current date and time
    df['Timestamp'] = pd.Timestamp.now()
    
    return df



def write_csv(date: str, dataframe: pd.DataFrame):
    '''Write DataFrame to CSV file with today's date in the filename'''
    
    filename = f"data_{date}.csv"
    
    dataframe.to_csv(f'data/{filename}', index=False, header=True)


def main():
    url = 'https://aoe2.net/api/leaderboard'
    
    data = get_data_by_api(url)
    
    df = make_dataframe(data)
    
    # Get today's date
    today = datetime.today().strftime('%Y%m%d')
    
    write_csv(today, df)


if __name__ == '__main__':
    main()