""" Module provides 1 + 1 """

import numpy as np
import pandas as pd


def main():
    """Returns 1 + 1."""

    df = pd.DataFrame({"a": [1, 2]})

    test = np.array(df)
    return test


if __name__ == "__main__":
    main()
