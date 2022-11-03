import pandas as pd

customers = pd.read_csv('Data\Customers.csv', index_col='id')

print(len(customers))
