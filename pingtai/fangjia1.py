import pandas as pd
import os
from sklearn.linear_model import LinearRegression  #  普通最小二乘线性回归
df=pd.read_csv(os.path.join("uploads",'house_price.csv'))
pd.set_option('display.max_columns',None)
df1=pd.get_dummies(df[["dist","floor"]])
del df1["dist_chaoyang"]
del df1["floor_high"]
# print(df1.head())
df2=pd.concat([df1,df],axis=1)
del df2["dist"]
del df2["floor"]
# print(df2.head(20))
X=df2.iloc[:,:-1]
y=df2["price"]
reg=LinearRegression()       #岭回归
reg=reg.fit(X,y)
# print(reg.intercept_)   #求theta的值
# print(reg.coef_)
# print(reg.score(X,y))  #优劣性
