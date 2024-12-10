#import lib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import numpy as np

#load the data
data=pd.read_csv("mhtcet.csv")
print(data)

#check the null data
print(data.isnull().sum())

#features and target
features=data[["Percentile","Location"]]
target=data["College"]
print(target)



#handle the null data
nfeatures=pd.get_dummies(features)
print(nfeatures)

#features scaling
mms=MinMaxScaler()
mfeatures=mms.fit_transform(nfeatures)
print(mfeatures)




#train and test
x_train,x_test,y_train,y_test=train_test_split(mfeatures,target,test_size=0.2)


#model
model=RandomForestClassifier()
model.fit(x_train,y_train)

#score
s1=model.score(x_train,y_train)
s2=model.score(x_test,y_test)
print("Training Score = ",round(s1*100,2))
print("Testing Score = ",round(s2*100,2))








#predictions

percentile=float(input("Enter your MHTCET percentile "))



loc=int(input("1 Mumbai & 2 Navi Mumbai "))
if loc==1:
	x=[percentile]+[1,0]
else:
	x=[percentile]+[0,1]


d=mms.transform([x])
ans=model.predict(d)
print(ans[0])


























