
from django.shortcuts import render

import pandas as pd 
#from django.db import connection
from .models import Data

def handle_uploaded_file(f , data):
    pd_file =pd.read_excel(f)
    
    order_id_list = [a for a in pd_file['AmazonOrderId']]
    asin_list = [ a for a in pd_file['ASIN']]
    cost_list = [a for a in pd_file['Cost(£)']]
    buyer_order_id_list= [a for a in pd_file['ShippingOrderId']]
    '''
    query = str(Data.objects.all().query)
    df = pd.read_sql_query(query, connection)
    pd_temp = df[["SATICI_SIPARIS_NUMARASI" , "TARIH" , 'SATIS_FIYATI' , 'AMAZON_FEE']]
    print(pd_temp)
    '''

    for x in data :
     #  b = Data.objects.all().filter(SATICI_SIPARIS_NUMARASI = x)
        b = Data.objects.get(SATICI_SIPARIS_NUMARASI = x)
        print(b)
        if str(x) in order_id_list :
            index = pd_file.index[pd_file['AmazonOrderId'] == str(x)].tolist()
            asin = asin_list[index[0]]
            buyer_order_id = buyer_order_id_list[index[0]]
            b.ALICI_SIPARIS_NUMARASI=buyer_order_id
            b.ASIN = asin
            b.save()
            print(asin)
            

            