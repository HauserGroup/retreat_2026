from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def data_path(*args: str | Path) -> Path:
    if not args:
        return PROJECT_ROOT / "data"
    return PROJECT_ROOT / "data" / Path(*args)
