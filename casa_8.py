import pandas as pd

filename = "big-mac-full-index.csv"

df = pd.read_csv(filename) 

# print(df.columns)

# Method 4: Using iterrows() method of the Dataframe. 
for index,row in df.iterrows():
    print(row['name'],
          row['local_price'],
          row['adj_price'],
          row['USD_adjusted'],
          row['date'],
          row['iso_a3'])
          
# Method 6:  Using apply() method of the Dataframe. 
print(df.apply(lambda row: (row['name'], row['local_price']), axis = 1))



