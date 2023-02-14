from django.shortcuts import render
from .muhasebe import mailparse
from .models import Data
from .fileupload import handle_uploaded_file
from .forms import UploadFileForm
from .forms import MALIYET
from django.conf import settings
import pandas as pd 
import sqlite3
from django.core.files import File
from django.http.response import HttpResponse
from datetime import datetime

def home(request):
    return render(request , 'index.html') 


def dbdownload(request):
    now = datetime.now().strftime("%d_%m_%Y %H_%M_%S")
    
    connection = sqlite3.connect("db.sqlite3")
    query = f"SELECT * FROM main_data where KULLANICI_ID = {request.user.id}"
    df = pd.read_sql(query, connection)
    filename= f"{request.user}_{now}.xlsx"
    df.to_excel(f'main/static/{filename}')
     
    db_path = f'main\static\{filename}'
    dbfile = File(open(db_path, "rb"))
    response = HttpResponse(dbfile)
    response['Content-Disposition'] = 'attachment; filename=%s' % db_path
    response['Content-Length'] = dbfile.size

    return response
def muhasebe(request):
   
    
    d = reversed(Data.objects.filter(KULLANICI = request.user))
    form = UploadFileForm(request.POST, request.FILES)
    maliyet_form = MALIYET(request.POST) 
    
    print("request", request.POST)
    data = {
            "info" : d ,
            "form" : form , 
            
            }
        
    if request.method == 'POST':

        if 'load_excel' in request.POST:
            print("load excel")
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'] , d)
                updated_d = Data.objects.filter(KULLANICI = request.user)
                data = {
                "info" : updated_d,
                'form' : form,
                }
        
        elif 'update_cost' in request.POST:
            print("update_cost")
            if maliyet_form.is_valid():
                p_cost = maliyet_form.data['product_cost']
                w_cost = maliyet_form.data['warehouse_cost']
                o_id = maliyet_form.data['order_id']
                try:
                    update_cost(o_id, p_cost, w_cost)
                    update_profit(o_id)
                
                except:
                    message = "Maliyet 0 Olamaz"
                    data = {
                    "info" : d,
                    'form' : form,
                    'message' : message
                    }

        elif 'update_order_list' in request.POST:
            mailparse(user = request.user)
            print("Good Job!!")
    else:
        print("no form posted")
        form = UploadFileForm()

    
    return render(request , 'muhasebe.html' , data) 


def update_cost(order_id,product_cost,warehouse_cost):
    order = Data.objects.get(SATICI_SIPARIS_NUMARASI = order_id)
    print(order)
    order.MALIYET = product_cost
    order.DEPO_MALIYET = warehouse_cost
    order.save()     

def update_profit(order_id):
    order = Data.objects.get(SATICI_SIPARIS_NUMARASI = order_id)
    profit = round((order.SATIS_FIYATI + order.AMAZON_FEE) / 0.81 - order.MALIYET - order.DEPO_MALIYET / 0.81,2)
    order.KAR = profit
    order.YUZDELIK_KAR = round(order.KAR / (order.MALIYET + order.DEPO_MALIYET / 0.81),2)
    order.save()


def muhasebe_update(request , id):
    siparis = Data.objects.get(id=id)
    '''
    TODO 
    FORM UPDATE VIEWS
    '''


    data = {
        'siparis' : siparis
    }
    return render(request , 'muhasebe_update.html' , data)

def pl(request):
    return render(request , 'pl.html') 