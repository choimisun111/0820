import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error


data = pd.read_csv('./data/5.HeightWeight.csv',
                   index_col=0)
data['Height(Inches)'] = data['Height(Inches)'] * 2.54
print(data['Height(Inches)'])

data['Weight(Pounds)'] = data['Weight(Pounds)'] * 0.453592
print(data['Weight(Pounds)'])


array=data.values
X=array[:,1]
Y=array[:,2]
plt.clf()
fig,ax=plt.subplots()

X1=X.reshape(-1,1)
print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X1,Y,test_size=0.001)
model=LinearRegression()
model.fit(X_train,Y_train)

Y_prediction = model.predict(X_test)
mae = mean_absolute_error(y_prediction, Y_test)
print(mae)

plt.scatter(X_test[:100],Y-y_prediction[:100],color='blue')
plt.xlabel("Height(cm)")
plt.ylabel("Weight(kg)")

plt.scatter
































