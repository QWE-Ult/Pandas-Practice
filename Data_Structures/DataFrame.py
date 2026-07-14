# DataFrame - Like an Excel Sheet, it has both Rows and Columns

import pandas as pd

data = {
    "Name":["John","Alice","Bob"],
    "Age":[25,30,28],
    "City":["Delhi","Mumbai","Pune"]
}

df=pd.DataFrame(data)
print(df)

# print(df.shape)

# print(df.size)

