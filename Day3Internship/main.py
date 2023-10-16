# 1. Creating Dataframe

# import pandas as pd
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data)
# print(df) 


#2(a). Add Operation with Rows

# import pandas as pd
# dict = {'Name':['Martha', 'Tim', 'Rob', 'Georgia'],
#         'Maths':[87, 91, 97, 95],
#         'Science':[83, 99, 84, 76]
#        }
# df = pd.DataFrame(dict)
# print(df)
# df.loc[len(df.index)] = ['Amy', 89, 93] 
# print(df)


#2(b). Add Operation with Columns

# import pandas as pd
# data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Height': [5.1, 6.2, 5.1, 5.2],
#         'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
# df = pd.DataFrame(data)
# address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
# df['Address'] = address
# print(df)


#2(c). Remove Operation with Rows

# import pandas as pd
# dataFrame = pd.DataFrame([[10, 15], [20, 25], [30, 35], [40, 45]],
#                          index=['w', 'x', 'y', 'z'],
#                          columns=['a', 'b'])
# print(dataFrame)
# dataFrame = dataFrame.drop('w')
# print(dataFrame)

#2(d) Remove Operation with Column

# import pandas as pd
# data = {'name': ['Alice', 'Bob', 'Charlie'],
#         'age': [25, 30, 35],
#         'gender': ['F', 'M', 'M']
#         }
# df = pd.DataFrame(data)
# print('Original DataFrame:\n', df)
# #to delete columns
# df = df.drop(columns=['gender'])
# #to delete rows
# # df = df[df['age'] != 30]
# print('Modified DataFrame:\n', df)


#3. Indexing the data

# import pandas as pd
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df) 

#4. Selecting the data

# import pandas as pd
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df) 
# print(df.loc[["day1", "day3"]])

#5(a). Handling Missing Data- remove rows that contain empty cells

# import pandas as pd
# df = pd.read_csv('data1.csv')

# new_df = df.dropna()
# print(new_df.to_string())
# #OR
# df.dropna(inplace = True) #Remove all rows with NULL values
# print(df.to_string())
# #OR
# df.fillna(130, inplace = True) #Replace NULL values with the number 130
# print(df.to_string())
# #OR
# df["Calories"].fillna(130, inplace = True) #Replace NULL values with the number 130 in calories column
# print(df.to_string())



#6. Iterating over rows and columns

import pandas as pd 
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
		'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
		'score':[90, 40, 80, 98]} 
df = pd.DataFrame(dict) 
for i in df.index:
    print(df['name'][i], df['degree'][i])