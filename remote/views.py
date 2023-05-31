from django.shortcuts import render
from .models import *
# Create your views here.
def fbaHomePage(request):
    countries = ['uk','ca','ja','au','fr','de']
    data = {
        'countries' : countries
    }
    return render(request,'fbahome.html' , data)

def fbaMarketPage(request,country):
    '''
    switchCase = {
        'fr' : [CompletedFR , NotCompletedFR , KeepaExcelFR],
        'uk' : [CompletedUK , NotCompletedUK , KeepaExcelUK],
        'ca' : [CompletedCA , NotCompletedCA , KeepaExcelCA],
        'ja' : [CompletedJA , NotCompletedJA , KeepaExcelJA],
        'au' : [CompletedAU , NotCompletedAU , KeepaExcelAU],
        'de' : [CompletedDE , NotCompletedDE , KeepaExcelDE],
    } 
    completedDatas = switchCase[country][0]
    notCompletedDatas = switchCase[country][1]
    keepaExcelDatas = switchCase[country][2]
    '''
    switchCase = {}
    completedDatas = None
    notCompletedDatas = None
    keepaExcelDatas = None
    if request.method == 'POST':
        if 'asin_text_upload' in request.POST:
            asins = request.POST['asintext'].split('\n')
            for asin in asins:
                try:
                    completedDatas.objects.get(Asin = asin)
                    keepaExcelDatas.objects.get(Asin = asin)
                    notCompletedDatas.objects.get(Asin = asin)
                except:
                    try: 
                        notCompletedDatas(User = request.user , Asin = asin)
                    except:
                        print(asin , 'failed')        
        elif 'asin_file_upload' in request.POST:
            pass
        elif 'download_asin' in request.POST:
            pass

    return render(request,'fbamarket.html')