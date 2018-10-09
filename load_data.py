import numpy as numpy
import pandas as pd

TRAIN_DATA = '../input/train.csv'
TEST_DATA = '../input/test.csv'

def read_csv(path):
    df = pd.read_csv(path)
    return df

def load_train_data():
    df = pd.read_csv(TRAIN_DATA)
    return df

def load_test_data():
    df = pd.read_csv(TEST_DATA)
    return df

if __name__ == '__main__':
    print load_train_data().head()
    print load_test_data().head()