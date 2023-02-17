from django.shortcuts import render
from .muhasebe import mailparse
from .models import Ingiltere , Almanya , Fransa
from .fileupload import handle_uploaded_file
from .forms import UploadFileForm
from .forms import MALIYET
import pandas as pd 
import sqlite3
from django.core.files import File
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
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
    return render(request , 'muhasebe.html')

def ingiltere(request):
   
    
    d = reversed(Ingiltere.objects.filter(KULLANICI = request.user))
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
                updated_d = Ingiltere.objects.filter(KULLANICI = request.user)
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
                    update_cost(Ingiltere,o_id, p_cost, w_cost)
                    update_profit(Ingiltere,o_id)
                
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

    
    return render(request , 'ingiltere.html' , data) 
def almanya(request):
   
    
    d = reversed(Almanya.objects.filter(KULLANICI = request.user))
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
                updated_d = Almanya.objects.filter(KULLANICI = request.user)
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
                    update_cost(Almanya,o_id, p_cost, w_cost)
                    update_profit(Almanya,o_id)
                
                except:
                    message = "Maliyet 0 Olamaz"
                    data = {
                    "info" : d,
                    'form' : form,
                    'message' : message
                    }

        elif 'update_order_list' in request.POST:
            mailparse(country=Almanya,user = request.user)
            print("Good Job!!")
    else:
        print("no form posted")
        form = UploadFileForm()

    
    return render(request , 'almanya.html' , data) 
def fransa(request):
   
    
    d = reversed(Fransa.objects.filter(KULLANICI = request.user))
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
                handle_uploaded_file(f = request.FILES['file'] , data=Fransa)
                updated_d = reversed(Fransa.objects.filter(KULLANICI = request.user))
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
                    
                    update_cost(Fransa,o_id, p_cost, w_cost)
                    update_profit(Fransa,o_id)
                    return HttpResponseRedirect('../fransa')
                
                except:
                    message = "Maliyet 0 Olamaz"
                    data = {
                    "info" : d,
                    'form' : form,
                    'message' : message
                    }

        elif 'update_order_list' in request.POST:
            mailparse(country=Fransa,user = request.user)
            print("Good Job!!")
    else:
        print("no form posted")
        form = UploadFileForm()

    
    return render(request , 'fransa.html' , data) 


def update_cost(country,order_id,product_cost,warehouse_cost):
    order = country.objects.get(SATICI_SIPARIS_NUMARASI = order_id)
    print(order)
    order.MALIYET = product_cost
    order.DEPO_MALIYET = warehouse_cost
    order.save()     

def update_profit(country,order_id):
    order = country.objects.get(SATICI_SIPARIS_NUMARASI = order_id)
    profit = round((order.SATIS_FIYATI + order.AMAZON_FEE) / 0.81 - order.MALIYET - order.DEPO_MALIYET / 0.81,2)
    order.KAR = profit
    order.YUZDELIK_KAR = round(order.KAR / (order.MALIYET + order.DEPO_MALIYET / 0.81),2)
    order.save()



    

def pl(request):
    return render(request , 'pl.html') 