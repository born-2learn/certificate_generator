import pandas as pd
from random import randint
from time import sleep

def decide_winner():
    dataset = pd.read_csv('data.csv')
    names = dataset.iloc[:, 0].values
    max_val = len(names) - 1
    min_val = 0
    print('The ')
    sleep(1)
    print('Winner')
    sleep(1)
    print('is:')
    sleep(2)

    print(names[randint(min_val, max_val)])


decide_winner()

