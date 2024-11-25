""" Module provides 1 + 1 """

import pandas as pd
import numpy as np

def main():
    """ Returns 1 + 1 """
    df = pd.DataFrame({'a': [1, 2]})
    test = np.array(df)
    return test

if __name__ == '__main__':
    main()
