import pandas as pd 
from .models import *
from datetime import datetime
import datetime
def com_keepa_excel(com_file , target_file , keepa_db , completed_db , notCompleted_db , user):
    com_pd_file =pd.read_excel(com_file)
    target_pd_file = pd.read_excel(target_file)
    df = pd.merge(com_pd_file, target_pd_file, on="ASIN")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    Asins = [a for a in df['ASIN']]
    SalesRanks = [a for a in df['Sales Rank: Current']]
    sale_price_BuyBox_list = [a for a in df['Buy Box: Current']]
    sale_price_NewCurrent_list = [a for a in df['New: Current']]
    sale_price_FBA_list = [a for a in df['New, 3rd Party FBA: Current']]
    sale_price_FBM_list = [a for a in df['New, 3rd Party FBM: Current']]
    Drop_Count_list = [a for a in df['Sales Rank: Drops last 30 days']]
    Titles = [a for a in com_pd_file['Title']]
    Asins = [a for a in com_pd_file['ASIN']]
    Buy_Prices = [a for a in com_pd_file['Buy Box: Current']]
    


















    def dataSaver(asin):
        try:
            data = keepa_db.objects.get(Asin = asin)
            try :
                check = completed_db.objects.get(User = user , Asin = asin)
                if data.Buy_Price is None:
                    data.Buy_Price = Buy_Prices[Asins.index(asin)]
                    data.Title = Titles[Asins.index(asin)]
                    data.save()
            except:
                new = completed_db(User = user , Asin = asin)
                new.save()
                if data.Buy_Price is None:
                    data.Buy_Price = Buy_Prices[Asins.index(asin)]
                    data.Title = Titles[Asins.index(asin)]
                    data.save()                
        except:
            data = keepa_db(Asin = asin , 
                Title = Titles[Asins.index(asin)],
                Buy_Price = Buy_Prices[Asins.index(asin)])
            data.save()
            new = completed_db(User = user , Asin = asin)
            new.save()
            
    for asin in Asins:
        try:
            check = completed_db.objects.get(Asin= asin , Buy_Price= Buy_Prices[Asins.index(asin)])
            if check.User == user:
                continue
            else : 
                if (check.Date - datetime.now()).day >=7:
                    dataSaver(asin=asin)
                else :
                    #test edilecek 
                    data = check
                    data.User = user
                    data.save()                         
        except:
            try:
                data = notCompleted_db.objects.get(Asin = asin)
                data.delete()
                dataSaver(asin = asin)
            except:
                dataSaver(asin=asin)            


def target_keepa_excel(file , keepa_db , completed_db , notCompleted_db , user):

    
    def dataSaver(asin):
        try:
            data = keepa_db.objects.get(Asin = asin)
            try :
                check = completed_db.objects.get(User = user , Asin = asin)
                if data.SalesRank is None:
                    data.Buy_Price = Buy_Prices[Asins.index(asin)]
                    data.Title = Titles[Asins.index(asin)]
                    data.save()
            except:
                new = completed_db(User = user , Asin = asin)
                new.save()
                if data.Buy_Price is None:
                    data.Buy_Price = Buy_Prices[Asins.index(asin)]
                    data.Title = Titles[Asins.index(asin)]
                    data.save()                
        except:
            data = keepa_db(Asin = asin , 
                Title = Titles[Asins.index(asin)],
                Buy_Price = Buy_Prices[Asins.index(asin)])
            data.save()
            new = completed_db(User = user , Asin = asin)
            new.save()

    for asin in Asins:
        try:
            check = completed_db.objects.get(Asin= asin , SalesRank= SalesRanks[Asins.index(asin)])
            if check.User == user:
                continue
            else : 
                if (check.Date - datetime.now()).day >=7:
                    dataSaver(asin=asin)
                else :
                    #test edilecek 
                    data = check
                    data.User = user
                    data.save()                         
        except:
            try:
                data = notCompleted_db.objects.get(Asin = asin)
                data.delete()
                dataSaver(asin = asin)
            except:
                dataSaver(asin=asin)     
