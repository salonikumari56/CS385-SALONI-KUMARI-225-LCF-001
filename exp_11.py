import pandas as pd
import numpy as np

# Creating empty series
ser = pd.Series()
print("Pandas Series: ", ser)

# Simple array
data = np.array(['g', 'e', 'e', 'k', 's'])

# Creating Pandas Series with an explicit index
ser = pd.Series(data, index=range(len(data)))
print("Pandas Series:\n", ser)
