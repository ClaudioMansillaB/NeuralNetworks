import numpy as np 
import pandas as pd
import os
import random

file = os.path.join('data', 'train.csv')

data = np.array(pd.read_csv(file))

m,n = data.shape
np.random.shuffle(data)

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]

data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
