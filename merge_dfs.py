from datetime import datetime
from pprint import pprint
import os

import pandas as pd


def make_list_from_files(path: str) -> list:
    list_of_filenames = []
    
    for filename in os.listdir(path):
        if 'data' in os.path.splitext(filename)[0]:
            list_of_filenames.append(filename)
            
    return list_of_filenames


def make_dfs(list_of_filenames: list) -> pd.DataFrame:
    dfs = []
    
    for filename in list_of_filenames:
        df = pd.read_csv(f'data/{filename}')
        dfs.append(df)
    
    return dfs
    

def concat_dfs(list_of_dataframes: list) -> pd.DataFrame:

    # Concatenate the DataFrames
    concat_df = pd.concat(list_of_dataframes)

    return concat_df


def write_concat_dfs_to_csv(concat_df: pd.DataFrame):
    
    filename = 'all_dataframes.csv'
    
    concat_df.to_csv(filename, index=False, header=True)


def main():
    path = 'data/'
    
    list_of_filenames = make_list_from_files(path)
    
    dfs = make_dfs(list_of_filenames)
    
    concat_df = concat_dfs(dfs)
    
    # Write DataFrame to CSV file
    write_concat_dfs_to_csv(concat_df)

    
main()