import pandas as pd

# Step 1: Create the dictionary
data = {
    'Id': [1, 2, 3, 4],
    'Name': ['Meher Nigar Hridy', 'Clara', 'Sara', 'Flora'],
    'Role': ['CEO', '', '', ''],
    'Salary': [100, 200, None, None]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Print initial 2 and last 2 rows
print("First 2 rows:\n", df.head(2))
print("\nLast 2 rows:\n", df.tail(2))

# Step 4: Count total null values
print("\nTotal null values in each column:\n", df.isnull().sum())

# Step 5: Detailed info about DataFrame
print("\nDataFrame info:")
df.info()

# Step 6: Drop rows with null values
df_rows_dropped = df.dropna()
print("\nDataFrame after dropping null rows:\n", df_rows_dropped)

# Step 7: Drop columns with null values
df_columns_dropped = df.dropna(axis=1)
print("\nDataFrame after dropping null columns:\n", df_columns_dropped)

# Step 8: Fill null Salary with 300
df['Salary'].fillna(300, inplace=True)
print("\nDataFrame after filling null Salaries:\n", df)

# Step 9: Fill null Role with 'CEO'
df['Role'].replace('', 'CEO', inplace=True)
print("\nDataFrame after filling null Roles:\n", df)