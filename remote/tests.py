from django.test import TestCase


import pandas as pd 

df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

other = pd.DataFrame({'key': ['K0', 'K1', 'K7'],
                      'B': ['B0', 'B1', 'B2']})
a = pd.merge(df, other, on="key")
print(a)

