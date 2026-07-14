# Pandas has only two major objects.

#** Series and DataFrame


# Series - Single Column Many Rows


import pandas as pd

s=pd.Series([10,20,30,40])
print(s)


# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64





# Custom index
s = pd.Series([80,90,70],index=["Math","Science","English"])
print(s)

#Math       80
# Science    90
# English    70
# dtype: int64




# Accessing Series

# By Index
print(s["Math"])# s[1]

# By specific position
print(s.iloc[0])



#### For Reading the files


#df = pd.read_csv("students.csv")
#df = pd.read_excel("students.xlsx")


#### For saving data
#df.to_csv("students.csv", index=False)
#df.to_excel("students.xlsx", index=False)