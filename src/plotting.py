import matplotlib.pyplot as plt

def save_operational_curve_png(path: str, fa_grid, hr_mean, hr_p25=None, hr_p75=None, title=None):
    plt.figure(figsize=(7,4))
    plt.plot(fa_grid, hr_mean)
    if hr_p25 is not None and hr_p75 is not None:
        plt.fill_between(fa_grid, hr_p25, hr_p75, alpha=0.2)
    plt.xlabel("False alarms per 30 days")
    plt.ylabel("Event hit-rate")
    if title:
        plt.title(title)
    plt.grid(True)
    plt.savefig(path, dpi=200, bbox_inches="tight")
    plt.close()
