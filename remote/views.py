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
    notCompletedDatas = switchCase[country][1]
    keepaExcelDatas = switchCase[country][2]

    
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
                        product = notCompletedDatas(User = request.user , Asin = asin)
                        product.save()
                    except:
                        print(asin , 'failed')        
        elif 'asin_file_upload' in request.POST:
            keepa_excel(com_file=request.FILES.get('com_asin') ,
                         target_file=request.FILES.get('target_asin') ,
                           completed_db=completedDatas 
                        , notCompleted_db=notCompletedDatas,
                          keepa_db=keepaExcelDatas ,
                           user = request.user )
        elif 'asin_link_upload' in request.POST:
            product = StoreLink(User = request.user ,
                                Link = request.POST['storelink'],
                                 Marketplace = country)                
            product.save()
        elif 'send_pool' in request.POST:
            asin_list = request.POST.getlist('poolCheckBox')
            for asin in asin_list:
                product_to_pool =completedDatas.objects.get(User = request.user , Asin=asin) 
                product_to_pool.Pool = True
                product_to_pool.save()

    return render(request,'fbamarket.html' , {'form' : form ,
                                              'asins' : completedDatas.objects.filter(User=request.user),
                                              'country':[country.upper()]})


def fbaMarketPoolPage(request,country):
    switchCase = {
        'fr' : [CompletedFR],
        'uk' : [CompletedUK],
        'ca' : [CompletedCA],
        'ja' : [CompletedJA],
        'au' : [CompletedAU],
        'de' : [CompletedDE],
    } 
    form = UploadFileForm(request.POST, request.FILES)
    completedDatas = switchCase[country]
    poolDatas = completedDatas.objects.get(User = request.user , Pool = True)
    if request.method == 'POST':
        if 'send_pool' in request.POST:
            asin_list = request.POST.getlist('poolCheckBox')
            for asin in asin_list:
                product_to_pool =completedDatas.objects.get(User = request.user , Asin=asin) 
                product_to_pool.Pool = False
                product_to_pool.save()
    data = {
        'asins' : poolDatas ,
        'form' : form ,
        'country' : [country.upper()]
    }
    return render(request,'fbamarketpool.html' , data)