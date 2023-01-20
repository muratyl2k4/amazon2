from django.test import TestCase


# Create your tests here.

import pandas 

csv = pandas.read_csv("order_track/c.csv")
liste = []
courier_name = 'landmark'
csv["Courier Name\t"] = csv["Courier Name\t"].str.lower() 
result = csv[csv["Courier Name\t"] == courier_name+ '\t'] if not csv[csv["Courier Name\t"] == courier_name+ '\t'].empty else csv[csv["Courier Name\t"].str.contains(courier_name.lower())]
print(result['Carrier Code\t'].values[0])
#if result.empty: 
#    for i in (csv['Courier Name\t'].values):
#        if courier_name.lower() in i.lower():
#            print(i)
