import pandas as pd

# # read data from CSV file into a DataFrame

# #df = pd.read_csv("Basics/Students.csv")
# #df = pd.read_csv("Basics/Students.csv", encoding="latin1/utf-8") when encoding error comes
# #df = pd.read_excel("Basics/Students.xlsx")

# # df= pd.read_json("Basics/Students.json")
# # print(df)

# #gcsfs=google cloud data


# # saves the file
# # df.to_csv("name.csv",index=False)
# # df.to_excel("name.xlsx",index=False)
# # df.to_json("name.json",index=False)


df=pd.read_json("Basics/Students.json")# rads the file and then printing it gives the data frame in terminal
# # print(df.head(3))#gives first 3 info of table
# # print(df.tail(3))# gives last 3 info of table
# # # print(df)



# print(df.describe())# gives quick statistical summary of your data.

# print(df.shape)# Shape of dataframe
# print(df.columns)# coumns of dataset





# # selecting columns
# print(df["Name"])# selecting one column (seires return)

# print(df[["Name","Marks"]])# selecting multiple columns use 2 square brackets(return dataframe)


# # filtering Rows

# high_score=df[df["Marks"]>90]
# print(high_score)


# # Filtering rows with multiple conditions(And / OR)

# condi=df[(df["Marks"]>80) & (df["Attendance"]>90)]
# print(condi)


