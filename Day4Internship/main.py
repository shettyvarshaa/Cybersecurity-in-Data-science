import pandas as pd
df = pd.read_csv('onlinefraud.csv')

# 1. Fetch the basic information
# print(df.info())

# 2. Count of data

# print(len(df.axes[0])) # (a) Quantitative
# print(len(df.axes[1]))

# print(df['type'].mode()) # (b) Qualitative
# print(df['type'].unique())

# print(df['type'].value_counts()) # (c) Nominal

# df['type'] = df['type'].astype('type') # (d) Categorical
# print(df)
# print("\nData Types:")
# print(df.dtypes)

# 3.Display the descriptive statics

# print(df.describe())

# 4. Checking for duplicate values
# print(df.duplicated())
#OR
# df.drop_duplicates(inplace = True) #Removing the duplicate values if any

# 5. Know the unique values in particular column
# print(df['type'].unique())

# 6 Handling Missing Data

# print(df.isnull().sum()) # (a) Check for null or missing values

# df.fillna(69, inplace=True)  # (b) Replace null values
# print(df)

# df=df.dropna(axis=0) #To drop missing or null values
# print(df)

# bool_series = pd.isnull(df["amount"]) #(c) type1
# print(df[bool_series]) 

# print(df.notnull()) #(d) type2

# 7. Know DataTypes of all Attributes
# print(df.dtypes)





