import numpy as np
import pandas as pd

dataset = np.zeros

dataset['NewYork_State'] = np.where(dataset['State'] == 'New York', 1, 0)
dataset['California_State'] = np.where(dataset['State'] == 'California', 1, 0)
dataset['Florida_State'] = np.where(dataset['State'] == 'Florida', 1, 0)
