from django.shortcuts import render
from .order_track import order_track
from .forms import UploadFileForm
from .fileupload import uploaded_file
from main.models import Data

def kargotakip(request):
    '''
    TODO
    1- last status ve last update database e kaydedilecek ? 
    2- kargotakip fonksiyonda donusturulup baska dosyadan cagirilacak --> DONE 
    3- takip numaralari excelden alinip database e kaydedileck --> DONE
    4- Order modeline kargo sirketlerinin secenegi eklenicek ve exceldeki sirket kisimlari api nin courier codelarina donusturulecek --> DONE
    '''
    apiKey = "uh77udwn-90ld-lzge-e1ib-pmkl0ct2zl68"
    order_list = order_track(apiKey=apiKey)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file(request.FILES['file'] , Data)
    else:
        form = UploadFileForm()
    data = {        
            "info" : order_list , 
            'form' : form
        }
    return render(request , "kargotakip.html" , data)
    

