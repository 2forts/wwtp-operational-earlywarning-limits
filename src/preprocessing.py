import numpy as np
import pandas as pd

def fit_impute_scale(df_train: pd.DataFrame):
    mu = df_train.mean()
    sd = df_train.std().replace(0, 1.0)
    return mu, sd

def transform_impute_scale(df: pd.DataFrame, mu: pd.Series, sd: pd.Series) -> pd.DataFrame:
    x = df.copy()
    x = x.apply(pd.to_numeric, errors="coerce")
    x = x.fillna(mu)
    return (x - mu) / sd
