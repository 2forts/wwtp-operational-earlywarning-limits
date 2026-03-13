import numpy as np
import pandas as pd

def false_alarms_per_30d(alert_bool: pd.Series) -> float:
    days = len(alert_bool)
    if days == 0:
        return 0.0
    fa = int(alert_bool.sum())
    return fa * (30.0 / days)

def hit_rate_on_event_days(event_days_bool: pd.Series, alert_bool: pd.Series) -> float:
    events = event_days_bool.astype(bool)
    n_event_days = int(events.sum())
    if n_event_days == 0:
        return float("nan")
    hits = int((events & alert_bool).sum())
    return hits / n_event_days

def operational_curve(scores: pd.Series, event_days_bool: pd.Series, grid_fa):
    qs = np.linspace(0.0, 1.0, 200)
    ths = np.quantile(scores.dropna().values, qs)

    points = []
    for th in ths:
        alert = (scores >= th)
        fa30 = false_alarms_per_30d(alert)
        hr = hit_rate_on_event_days(event_days_bool, alert)
        points.append((fa30, hr))

    pts = pd.DataFrame(points, columns=["fa30", "hit_rate"]).sort_values("fa30")
    pts = pts.groupby("fa30", as_index=False)["hit_rate"].mean()

    fa_vals = pts["fa30"].values
    hr_vals = pts["hit_rate"].values
    hr_interp = np.interp(grid_fa, fa_vals, hr_vals, left=hr_vals[0], right=hr_vals[-1])
    return hr_interp, pts

def summarize_operating_points(fa_grid, hr_mean, targets=(1,5,10,20)):
    rows = []
    for t in targets:
        i = int(np.argmin(np.abs(fa_grid - t)))
        rows.append((float(fa_grid[i]), float(hr_mean[i])))
    return pd.DataFrame(rows, columns=["fa_per_30d", "hit_rate_mean"])
