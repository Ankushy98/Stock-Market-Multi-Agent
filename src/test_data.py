import pandas as pd
import numpy as np

print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)

data = {
    "Stock": ["TCS", "RELIANCE", "INFY"],
    "Price": [3500, 1400, 1700]
}

df = pd.DataFrame(data)

print("\nStock Data:")
print(df)