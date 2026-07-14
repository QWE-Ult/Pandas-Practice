import pandas as pd

data = {
    "Name":["John","Alice","Bob"],
    "Age":[25,None,28],
    "City":["Delhi","Mumbai","Pune"]
}

df=pd.DataFrame(data)
print(df)

# here we havent use inplace so all the changes are not affecting original dataframe
# Missing Values

print(df.isnull()) #checks for missing values if present returns true

#     Name    Age   City
# 0  False  False  False
# 1  False  True  False
# 2  False  False  False

# count missing values
print(df.isnull().sum())


# Fill missing values
print(df.fillna(0))

#     Name   Age    City
# 0   John  25.0   Delhi
# 1  Alice   0.0  Mumbai
# 2    Bob  28.0    Pune



# Deletes the null value
print(df.dropna())


#    Name   Age   City
# 0  John  25.0  Delhi
# 2   Bob  28.0   Pune



# Duplicate Rows

# Checks for duplicate row

# df.duplicated()

# Removes it

# df.drop_duplicates()


# Value Counts
# df["City"].value_counts()
# Counts the frequency of each unique value.


# Unique Values
# df["City"].unique()



# Number of Unique Values
# df["City"].nunique()