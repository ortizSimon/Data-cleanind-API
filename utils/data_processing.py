import pandas as pd
import numpy as np


def clean_data(df):
    """
    Removes duplicates and fixes column types.
    """
    cleaned_df = df.copy()
    
    # Remove duplicates
    cleaned_df = cleaned_df.drop_duplicates()
    
    # Convert string numbers to actual numbers if possible
    for col in cleaned_df.columns:
        if cleaned_df[col].dtype in ['int64', 'float64']:
            continue
            
        try:
            cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors='coerce')
        except:
            pass
    
    # Remove rows that are completely empty
    cleaned_df = cleaned_df.dropna(how='all')
    
    return cleaned_df


def get_summary(df):
    """
    Returns stats using pandas describe().
    """
    numeric_df = df.select_dtypes(include=[np.number])
    
    if numeric_df.empty:
        return {"message": "No numeric columns found in dataset"}
    
    desc = numeric_df.describe()
    
    # Convert to dict for JSON
    summary = {}
    for col in desc.columns:
        summary[col] = {
            "count": float(desc[col]['count']),
            "mean": float(desc[col]['mean']),
            "std": float(desc[col]['std']),
            "min": float(desc[col]['min']),
            "25%": float(desc[col]['25%']),
            "50%": float(desc[col]['50%']),
            "75%": float(desc[col]['75%']),
            "max": float(desc[col]['max'])
        }
    
    return summary


def get_correlations(df):
    """
    Calculates correlation matrix.
    """
    numeric_df = df.select_dtypes(include=[np.number])
    
    if numeric_df.empty:
        return {"message": "No numeric columns found for correlation"}
    
    corr_matrix = numeric_df.corr()
    
    # Convert to dict, handle NaN values
    corr_dict = {}
    for col in corr_matrix.columns:
        corr_dict[col] = {}
        for idx in corr_matrix.index:
            val = corr_matrix.loc[idx, col]
            corr_dict[col][idx] = None if pd.isna(val) else float(val)
    
    return corr_dict

