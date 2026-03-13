def make_rolling_splits(n_days: int, train_frac=0.60, val_frac=0.20, n_splits=4):
    train_len = int(train_frac * n_days)
    val_len   = int(val_frac * n_days)
    test_len  = n_days - train_len - val_len

    step = max(1, test_len // n_splits)
    splits = []
    for s in range(n_splits):
        train_end = train_len + s * step
        val_end   = min(train_end + val_len, n_days - 1)
        test_end  = min(val_end + test_len, n_days)
        if test_end <= val_end or val_end <= train_end:
            continue
        splits.append((train_end, val_end, test_end))
    return splits
