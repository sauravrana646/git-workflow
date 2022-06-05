import numpy as np
import pandas as pd

my_data = np.array([[5, 'a', 1],
                    [3, 'b', 3],
                    [1, 'b', 2],
                    [3, 'a', 1],
                    [4, 'b', 2],
                    [7, 'c', 1],
                    [7, 'c', 1]])

df = pd.DataFrame(data=my_data, columns=['y', 'dummy', 'x'])
just_dummies = pd.get_dummies(df['dummy'])

df = pd.DataFrame(data=my_data, columns=['y', 'dummy', 'x'])
just_dummies = pd.get_dummies(df['dummy'])

step_1 = pd.concat([df, just_dummies], axis=1)
step_1.drop(['dummy', 'c'], inplace=True, axis=1)
# to run the regression we want to get rid of the strings 'a', 'b', 'c' (obviously)
# and we want to get rid of one dummy variable to avoid the dummy variable trap
# arbitrarily chose "c", coefficients on "a" an "b" would show effect of "a" and "b"
# relative to "c"
step_1 = step_1.applymap(np.int)
