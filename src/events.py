import numpy as np
import pandas as pd

def transition_score(Z: pd.DataFrame) -> pd.Series:
    dZ = Z.diff().fillna(0.0)
    return np.sqrt((dZ**2).sum(axis=1))

def percentile_threshold(train_scores: pd.Series, percentile: float) -> float:
    return float(np.nanpercentile(train_scores.values, percentile))

def define_event_days(scores: pd.Series, thr: float) -> pd.Series:
    return (scores >= thr)

def event_run_statistics(event_days: pd.Series) -> dict:
    e = event_days.astype(bool).values
    durations = []
    cur = 0
    for v in e:
        if v:
            cur += 1
        else:
            if cur > 0:
                durations.append(cur)
                cur = 0
    if cur > 0:
        durations.append(cur)

    n_events = len(durations)
    return {
        "n_event_days": int(e.sum()),
        "n_events": n_events,
        "durations": durations,
        "duration_mean": float(np.mean(durations)) if n_events else float("nan"),
        "duration_median": float(np.median(durations)) if n_events else float("nan"),
        "duration_max": int(np.max(durations)) if n_events else 0,
    }
