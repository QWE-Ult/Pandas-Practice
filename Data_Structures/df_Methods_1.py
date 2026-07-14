import pandas as pd

data = {
    "Name":["John","Alice","Bob"],
    "Age":[25,30,28],
    "City":["Delhi","Mumbai","Pune"]
}

df=pd.DataFrame(data)
print(df)


# print(len(df))# Number of ROws

# print(df.columns)

# print(df.index)

# print(df.values)# Returns Numpy array

# print(df.dtypes)# Gives dataTypes of columns value

# print(df.info())# give small info of dataframe

# print(df.describe())# gives statstical summary of Dataframe

# print(df.head())# gives first 5 rows print(df.head(3)) give 3 rows

# print(df.tail())# gives last 5 rows print(df.tail(3)) give 3 rows from last

# print(df["Age"])# Selecting One Column

# print(df[["Age","City","Name"]])# Selecting Multiple Columns

# df["Salary"]=[50000,60000,70000]# Adding column
# print(df)

# df["Age"]=[26,31,29]# Updating column
# print(df)

# df.drop("Salary",axis=1,inplace=True)# Deleting Column axis=1 means column
# df.drop(0,axis=0,inplace=True)# Deleting row axis=0 means row

# print(df)



# Selecting Rows



# print(df.loc[1])# label based

# print(df.iloc[1])# Position Based

# print(df.iloc[0:2])# Multiple Rows




# Selecting Specific Rows and Columns

# print(df.loc[0, "Name"])

# print(df.iloc[0, 1])# By Position


