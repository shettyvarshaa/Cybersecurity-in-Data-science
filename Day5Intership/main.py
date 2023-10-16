import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('onlinefraud.csv')

# condition = df['amount'] == 181   #1
# filtered_data = df[condition]
# filtered_data.to_csv('filtered_data.csv', index=False)


# column_mapping = {       #2
#     'step': 'STEPS',
#     'type': 'modeofpayment',
# }
# df.rename(columns=column_mapping, inplace=True)

# df.to_csv('renamed_dataset.csv', index=False)


# numeric_df = df.select_dtypes(include=['number'])   #3
# correlation_matrix = numeric_df.corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Correlation Matrix Heatmap')
# plt.show()

# # Create a scatter plot for two columns
# x_column = 'amount'
# y_column = 'oldbalanceOrg'
# z_column = 'newbalanceOrig'
# plt.scatter(df[x_column], df[y_column])
# plt.title(f'Scatter Plot for {x_column} vs. {y_column}')
# plt.show()


# print(len(df.axes[0])) # 5 Quantitative(no of rows and column)
# print(len(df.axes[1]))

# print(df.describe()[['amount', 'oldbalanceOrg','newbalanceOrig']]) #checking presence of outlier

