import pandas as pd
import numpy as np
import csv
from datetime import datetime

train_data_path = 'train_data.csv'
data = pd.read_csv(train_data_path)
data = data.sort_values(by = 'date')

y = np.array(data['home_team_win'], dtype=int)

float_cols = []
for col in data.columns:
    if(data[col].dtype == np.float64):
        float_cols.append(1)
    else:
        float_cols.append(0)
       
x = []
for _, row in data.iterrows():
    ls = row.tolist()
    if np.isnan(row.iloc[12]):
        date = datetime.strptime(row.iloc[3], '%Y-%m-%d')
        ls[12] = float(date.year)
    temp = []
    for i in range(len(ls)):
        if float_cols[i] == 1:
            temp.append(ls[i])
        elif i == 4:
            if ls[i]:
                temp.append(1)
            else:
                temp.append(0)
    x.append(temp)

for season in range(2016, 2024):
    x_train = []
    for row in x:
        if np.isnan(row[5]):
            continue
        if row[5] == float(season):
            row.pop(5)
            x_train.append(row)
    break
    # logistic regression
    
    