from django.shortcuts import render
from .muhasebe import mailparse
from .models import Data
from .fileupload import handle_uploaded_file
from .forms import UploadFileForm
def home(request):
    return render(request , 'index.html') 


def muhasebe(request):
    mailparse(user = request.user)
    d = Data.objects.filter(KULLANICI = request.user)
    if request.method == 'POST':
        print('1')
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            print('2')
            handle_uploaded_file(request.FILES['file'] , d)
    else:
        form = UploadFileForm()
    data = {
        "info" : d,
        'form' : form
        
    }
    
    return render(request , 'muhasebe.html' , data) 
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