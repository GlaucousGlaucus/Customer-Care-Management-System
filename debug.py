import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

custom_date_parser = lambda x: datetime.strptime(x, r'%Y/%m/%d %H:%M:%S')
tickets = pd.read_csv(r'Data\tickets.csv', index_col='TicketID', parse_dates=[
                        'DateOpened'], date_parser=custom_date_parser)


