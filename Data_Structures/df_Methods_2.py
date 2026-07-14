import pandas as pd

data = {
    "Name":["John","Alice","Bob"],
    "Age":[25,30,28],
    "City":["Delhi","Mumbai","Pune"]
}

df=pd.DataFrame(data)
print(df)



# Filtering

# print(df[df["Age"] > 25]) # Age greater than 25

# print(df[(df["Age"] > 25) & (df["City"] == "Mumbai")])# Multiple Conditions


# Sorting

# df.sort_values("Age")# Ascending

# df.sort_values("Age", ascending=False)# Descending



# Rename Columns
# df.rename(columns={"Age":"Student_Age"},inplace=True)
# print(df)



# Reset Index - Sometimes after deleting rows, sorting data, or filtering, the row numbers become irregular.
# df.reset_index()
# print(df)




#Set Index= Takes passed value as index(here name acts as index)
df.set_index("Name",inplace=True)
print(df)