
  
from imap_tools import MailBox , AND
from django.contrib.auth.models import User
from .models import *
import re
import locale
from bs4 import BeautifulSoup


from datetime import datetime


def mailparse(user):
    ###EMAIL PARSE
    username = "veonxltd@gmail.com"
    app_password = "ykibsqevqzelimln"
    mb = MailBox('imap.gmail.com').login(username, app_password)
    last_date = list(Data.objects.filter(KULLANICI = user))
    dx = last_date[-1].TARIH
    messages = mb.fetch(AND(subject='Sold, dispatch now:' , date_gte=dx))
    liste = []
    i=0 
    
    for msg in messages:
        try : 
            aaaa = BeautifulSoup(msg.html , 'html.parser').prettify()

            
           
          
            ##FROM 
            #ORDER İD 
            order_id_text=re.findall("Order ID:.*$",aaaa,re.MULTILINE)
            for x in order_id_text:

                order_id = re.findall('(?<=: )(.*)', x)
                oi = order_id[0]
                print('x' , x)

                
            #ORDER DATE
            order_date_text=re.findall("Order date: .*$",aaaa,re.MULTILINE)
            locale.setlocale(locale.LC_ALL, 'en_US')

            for x in order_date_text:
                order_date = re.findall('(?<=: )(.*)', x)
                od = order_date[0]
                datetime_object = datetime.strptime(od[0:len(od)], "%d/%m/%Y")
                    
            #PRICE
            price_text=re.findall("Price: .*$",aaaa,re.MULTILINE)
            for x in price_text:
                price = re.findall('(?<=: )(.*)', x)
                prc = price[0]
            
            #SHIPPING
            shipping_text=re.findall("Shipping: .*$",aaaa,re.MULTILINE)
            for x in shipping_text:
                shipping = re.findall('(?<=: )(.*)', x)
                shp = shipping[0]
            
            
            #AMAZON FEES
            fee_text=re.findall("Amazon fees: .*$",aaaa,re.MULTILINE)
            for x in fee_text:
                fee = re.findall('(?<=: )(.*)', x)
                afee = fee[0]
            
            #YOUR EARNING
            earning_text=re.findall("Your earnings: .*$",aaaa,re.MULTILINE)
            for x in earning_text:
                earning = re.findall('(?<=: )(.*)', x)
                ern = earning[0]
            try:
                b = Data.objects.get(SATICI_SIPARIS_NUMARASI = oi[0:len(oi)-1])
                
            except:
                b = Data(
                    KULLANICI = user, 
                    SATICI_SIPARIS_NUMARASI = oi[0:len(oi)-1],
                    SATIS_FIYATI  = float(prc.replace("£" , "")[0:len(prc)-1]),
                    AMAZON_FEE  = float(afee.replace("£" , "")[0:len(afee)-1]),
                    TARIH = datetime_object,
                    MALIYET = 0,
                    DEPO_MALIYET = 0
                )
                b.save()
        except: 
            print(1)

        
        
            
    