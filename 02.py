import pandas as pd

header = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS'
          'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT','MEDV']

data = pd.read_csv("./data/3.housing.csv",
                   delim_whitespace= True, names=header)

print(data)
