from django.shortcuts import render
from .models import *
from .fileupload import keepa_excel
from .forms import UploadFileForm
# Create your views here.

switchCase = {}


def fbaHomePage(request):
    countries = ['uk','ca','ja','au','fr','de']
    data = {
        'countries' : countries
    }
    return render(request,'fbahome.html' , data)

def fbaMarketPage(request,country):
    '''
    completedDatas = None
    notCompletedDatas = None
    keepaExcelDatas = None
    '''
    form = UploadFileForm(request.POST, request.FILES)

    switchCase = {
        'fr' : [CompletedFR , NotCompletedFR , KeepaExcelFR],
        'uk' : [CompletedUK , NotCompletedUK , KeepaExcelUK],
        'ca' : [CompletedCA , NotCompletedCA , KeepaExcelCA],
        'ja' : [CompletedJA , NotCompletedJA , KeepaExcelJA],
        'au' : [CompletedAU , NotCompletedAU , KeepaExcelAU],
        'de' : [CompletedDE , NotCompletedDE , KeepaExcelDE],
    } 
    completedDatas = switchCase[country][0]
    keepaExcelDatas = switchCase[country][2]
    notCompletedDatas = switchCase[country][1]
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
            keepa_excel(com_file=request.FILES.get('com_asin') ,
                         target_file=request.FILES.get('target_asin') ,
                           completed_db=completedDatas 
                        , notCompleted_db=notCompletedDatas,
                          keepa_db=keepaExcelDatas ,
                           user = request.user )
        elif 'download_asin' in request.POST:
            pass

    return render(request,'fbamarket.html' , {'form' : form})