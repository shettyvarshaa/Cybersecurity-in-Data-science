import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#indexing using the index argument

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

#OR
# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df)

#return specified numbers from the top
# print(df.head(10))
#tail&head - first 5 and last 5
#print(df.head())

#to locate few rows

# print(df.loc[[0, 1]])

#Remove all rows with NULL values

#import pandas as pd

# df = pd.read_csv('data.csv')

# df.dropna(inplace = True)

# print(df.to_string())

#Replace NULL values with the number 130:


# import pandas as pd

# df = pd.read_csv('data.csv')

# df.fillna(130, inplace = True)

# print(df.to_string())



#This operation inserts 130 in empty cells in the "Calories" column (row 18 and 28).
# import pandas as pd

# df = pd.read_csv('data.csv')

# df["Calories"].fillna(130, inplace = True)

# print(df.to_string())


#As you can see in row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68

# import pandas as pd

# df = pd.read_csv('data.csv')

# x = df["Calories"].mean()

# df["Calories"].fillna(x, inplace = True)

# print(df.to_string())


#Set "Duration" = 45 in row 7:
# import pandas as pd

# df = pd.read_csv('data.csv')

# df.loc[7,'Duration'] = 45

# print(df.to_string())

#Delete rows where "Duration" is higher than 120:



#Notice that row 12 has been removed from the result

# import pandas as pd

# df = pd.read_csv('data.csv')

# df.drop_duplicates(inplace = True)

# print(df.to_string())

#using loc to add rows
# df.loc[len(df)] = new_row


#adding column into

# Import pandas package
# import pandas as pd
 
# # Define a dictionary containing Students data
# data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Height': [5.1, 6.2, 5.1, 5.2],
#         'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
 
# # Convert the dictionary into DataFrame
# df = pd.DataFrame(data)
 
# # Declare a list that is to be converted into a column
# address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
 
# # Using 'Address' as the column name
# # and equating it to the list
# df['Address'] = address
 
# # Observe the result
# print(df)

