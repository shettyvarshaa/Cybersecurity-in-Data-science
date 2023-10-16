new_df = df.dropna()
# print(new_df.to_string())
# #OR
# df.dropna(inplace = True) #Remove all rows with NULL values
# print(df.to_string())
# #OR
# df.fillna(130, inplace = True) #Replace NULL values with the number 130
# print(df.to_string())