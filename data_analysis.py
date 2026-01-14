import pandas as pd

# Simple data analysis example
data = {
    "Marks": [65, 78, 82, 90, 88],
    "Attendance": [70, 80, 85, 95, 90]
}

df = pd.DataFrame(data)
print("Dataset Summary:")
print(df.describe())
