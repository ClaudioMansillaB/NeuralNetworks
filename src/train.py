import numpy as np 
import pandas as pd
import os
import random

file = os.path.join('data', 'train.csv')

data = np.array(pd.read_csv(file))

