import numpy as np
import pandas as pd


def explore_dataframe(df):
    print("Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nData types:\n", df.dtypes)
    print("\nFirst 5 rows:\n", df.head())
    print("\nLast 5 rows:\n", df.tail())
    print("\nSummary statistics:\n", df.describe())
    print("\nInformation:\n")
    df.info()


# Clears data from dataframe and only the columns are left
def df_clone_nodata(df):

    empty_df = pd.DataFrame(columns=df.columns)
    
    # Preserve the data types of the original DataFrame
    for col in df.columns:
        empty_df[col] = empty_df[col].astype(df[col].dtype)
    
    return empty_df

def merge_dataframes(left_df, right_df, how='inner', on=None, left_on=None, right_on=None, 
                     suffixes=('_left', '_right'), indicator=False, validate=None):
    """
    Merge two pandas DataFrames with various options.
    
    Args:
        left_df (pandas.DataFrame): Left DataFrame to merge
        right_df (pandas.DataFrame): Right DataFrame to merge
        how (str): Type of merge to perform - 'inner', 'outer', 'left', 'right' (default: 'inner')
        on (str or list): Column name(s) to join on if column names are the same in both DataFrames
        left_on (str or list): Column name(s) from left DataFrame to join on
        right_on (str or list): Column name(s) from right DataFrame to join on
        suffixes (tuple): Suffix to add to overlapping column names (default: ('_left', '_right'))
        indicator (bool): Add a column indicating source of the row (default: False)
        validate (str): Optional integrity check - one of {'1:1', '1:m', 'm:1', 'm:m'} (default: None)
    
    """
    # Perform the merge with all specified options
    merged_df = pd.merge(
        left_df, 
        right_df, 
        how=how, 
        on=on, 
        left_on=left_on, 
        right_on=right_on, 
        suffixes=suffixes,
        indicator=indicator,
        validate=validate
    )
    
    return merged_df