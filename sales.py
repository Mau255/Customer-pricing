# coding: utf-8

import csv
import pandas as pd
import numpy as np

# Load data from csv file
with open('sales.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        #print(line)
        pass

# Load sales.csv as pandas dataframe
df = pd.read_csv('sales.csv')
#print(df.head())

   
# sum the data of the column item_price of df
#print(df['item_price'].sum())


# Change all "商品" by "Product"
df['item_name'] = df['item_name'].str.replace('商品', 'Product')
print(df['item_name'])


# Plot a bar graph with the top 5 expensive item_price in red. Plot another bar with the top 5 cheap item_price in blue. Plot a line graph with the average item_price in green
df.groupby('item_name').sum()['item_price'].sort_values(ascending=False).head(100).plot(kind='bar', color='r')
df.groupby('item_name').sum()['item_price'].sort_values(ascending=True).head(100).plot(kind='bar', color='b')
df.groupby('item_name').mean()['item_price'].plot(kind='line', color='g')



import matplotlib.pyplot as plt
plt.show()


# Create a list with all products category_lv1 and category_lv2 encoded in utf8


df2 = pd.read_csv('transactions.csv')
print(df2.head())

# Create a new dataframe
df3 = pd.DataFrame(df['item_id'])

# multiply the column item_id from df and df2
df3['item_id'] = df['item_id'] * df2['item_id']


# print df to markdown format
print(df.to_markdown())
