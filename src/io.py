from pathlib import Path

def ensure_exists(path: str) -> Path:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p.resolve()}")
    return p
