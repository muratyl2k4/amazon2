import pandas as pd 
#from django.db import connection
from .models import Data

def handle_uploaded_file(f , data):
    pd_file =pd.read_excel(f)
    print('aa')
    print(pd_file)
    order_id_list = [a for a in pd_file['AmazonOrderId']]
    cost_list = [a for a in pd_file['Cost(£)']]
    '''
    query = str(Data.objects.all().query)
    df = pd.read_sql_query(query, connection)
    pd_temp = df[["SATICI_SIPARIS_NUMARASI" , "TARIH" , 'SATIS_FIYATI' , 'AMAZON_FEE']]
    print(pd_temp)
    '''

    for x in data :
        b = Data.objects.all().filter(SATICI_SIPARIS_NUMARASI = x)
        print(b)
        if str(x) in order_id_list :
            index = pd_file.index[pd_file['AmazonOrderId'] == str(x)].tolist()
            cost = cost_list[index[0]]
            print(cost)
            