import pandas as pd

def load_data(path, nrows=None):

    df = pd.read_json(
        path,
        lines=True,
        nrows=nrows
    )

    return df