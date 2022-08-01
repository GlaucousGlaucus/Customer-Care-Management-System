import pandas as pd
import numpy as np

# Read the Files
customers = pd.read_csv('Data\customers.csv')
orders = pd.read_csv('Data\orders.csv')
products = pd.read_csv('Data\products.csv')
tickets = pd.read_csv(r'Data\tickets.csv')

print("Files Loaded")
