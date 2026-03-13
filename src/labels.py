import numpy as np
import pandas as pd

def make_horizon_labels(event_days: pd.Series, H: int) -> pd.Series:
    e = event_days.astype(int).values
    y = np.zeros_like(e)
    for i in range(len(e)):
        j1 = i + 1
        j2 = min(i + H, len(e) - 1)
        if j1 <= j2 and e[j1:j2+1].sum() > 0:
            y[i] = 1
    return pd.Series(y, index=event_days.index, name=f"y_H{H}")
