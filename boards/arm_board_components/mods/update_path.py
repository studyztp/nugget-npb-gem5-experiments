import sys
from pathlib import Path


def update_path():
    here = Path(__file__)
    to_append = str(here.resolve().parent.parent)
    sys.path.append(to_append)
    return to_append
