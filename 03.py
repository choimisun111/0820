import pandas as pd
from sklearn.model_selection import train_test_split
header = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS'
          'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT','MEDV']
data = pd.read_csv("./data/3.housing.csv",
                   delim_whitespace= True, names=header)

array= data. values

X =array[:,0:13]
Y= array[:, 13]

train_test_split(X,Y,test_size=0.2)



#선형회귀분석


