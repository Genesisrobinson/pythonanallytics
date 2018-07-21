import pandas as pd
cars = pd.read_csv('d:/report/DMP Execution suite1.csv', index_col = 0)

print(cars['Name'])