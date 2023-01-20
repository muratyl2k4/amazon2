from django.shortcuts import render
from .order_track import order_track

def kargotakip(request):
    order_list = []
    '''
    TODO
    1- last status ve last update database e kaydedilecek
    2- kargotakip fonksiyonda donusturulup baska dosyadan cagirilacak --> DONE 
    3- takip numaralari excelden alinip database e kaydedileck (bekirabi)  
    4- Order modeline kargo sirketlerinin secenegi eklenicek ve exceldeki sirket kisimlari api nin courier codelarina donusturulecek --> DONE
    '''
    apiKey = "uh77udwn-90ld-lzge-e1ib-pmkl0ct2zl68"
    if request.method == "POST":
        order_track(apiKey=apiKey)
        order_list = order_track(apiKey=apiKey)

    data = {        
            "info" : order_list
        }

    return render(request , "kargotakip.html" , data)
    

