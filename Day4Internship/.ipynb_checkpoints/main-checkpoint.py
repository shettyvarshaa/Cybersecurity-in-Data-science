#7. Handling Missing data

import pandas as pd
df = pd.read_csv('onlinefraud.csv')

new_df = df.dropna()
print(new_df.to_string())
# #OR
# df.dropna(inplace = True) #Remove all rows with NULL values
# print(df.to_string())
#OR
df.fillna(00000, inplace = True) #Replace NULL values with the number 130
print(df.to_string())
# #OR
# df["Calories"].fillna(130, inplace = True) #Replace NULL values with the number 130 in calories column
# print(df.to_string())