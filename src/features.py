import numpy as np
import pandas as pd

def build_window_features(Z: pd.DataFrame, W: int) -> pd.DataFrame:
    feats = []
    idx = []

    tt = np.arange(W)
    tt_mean = tt.mean()
    denom = ((tt - tt_mean) ** 2).sum()

    for t in range(W - 1, len(Z)):
        win = Z.iloc[t - W + 1 : t + 1]
        x_last = win.iloc[-1].values
        x_mean = win.mean(axis=0).values
        x_std  = win.std(axis=0).values

        x_vals = win.values
        cov = ((tt - tt_mean)[:, None] * (x_vals - x_vals.mean(axis=0)[None, :])).sum(axis=0)
        slope = cov / (denom + 1e-12)

        delta = win.iloc[-1].values - win.iloc[-2].values if W >= 2 else np.zeros(win.shape[1])

        f = np.concatenate([x_last, x_mean, x_std, slope, delta])
        feats.append(f)
        idx.append(Z.index[t])

    return pd.DataFrame(np.vstack(feats), index=idx)
