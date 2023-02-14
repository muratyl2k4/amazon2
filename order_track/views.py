from django.shortcuts import render
from .order_track import order_track
from .forms import UploadFileForm
from .fileupload import uploaded_file
from main.models import Data

def kargotakip(request):
   
    apiKey = "d2euawn7-xakk-71yj-i71h-mskqaza35xlf"
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
    

