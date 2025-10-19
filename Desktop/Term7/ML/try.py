import pandas as pd
import numpy as np

# Pandas DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000.0, 60000.0, 70000.0]
})
print(df['Name'])  # Access by column name

# NumPy Array
arr = np.array([
    [25, 50000.0],
    [30, 60000.0],
    [35, 70000.0]
])
print(arr[:, 0])  # Access by numeric index