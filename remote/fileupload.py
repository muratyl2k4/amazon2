import pandas as pd 
from .models import *
from datetime import datetime
import datetime
def keepa_excel(com_file , target_file , keepa_db , completed_db , notCompleted_db , user):
    com_pd_file =pd.read_excel(com_file)
    target_pd_file = pd.read_excel(target_file)
    df = pd.merge(com_pd_file, target_pd_file, on="ASIN")    
    
    try: 
        Asins = [a for a in df['ASIN']]
        SalesRanks = [a for a in df['Sales Rank: Current']]
        sale_price_BuyBox_list = [a for a in df['Buy Box: Current']]
        sale_price_NewCurrent_list = [a for a in df['New: Current']]
        sale_price_FBA_list = [a for a in df['New, 3rd Party FBA: Current']]
        sale_price_FBM_list = [a for a in df['New, 3rd Party FBM: Current']]
        Drop_Count_list = [a for a in df['Sales Rank: Drops last 30 days']]
        Titles = [a for a in df['Title']]
        Buy_Prices = [a for a in df['Buy Box: Current']]
        
        def dataSaver(asin):
            try:
                data = keepa_db.objects.get(Asin = Asins[asin])
                try: 
                    check = completed_db.objects.get(User = user , Asin = Asins[asin])
                except:
                    new = completed_db(User = user , Asin = Asins[asin])
                    new.save(using='mysql')                    
            except:
                data = keepa_db(Asin = Asins[asin] , 
                    Title = Titles[asin],
                    SalesRank = SalesRanks[asin],
                    Drop_Count = Drop_Count_list[asin],
                    Buy_Price = Buy_Prices[asin],
                    Sale_Price_NC = sale_price_NewCurrent_list[asin],
                    Sale_Price_BB = sale_price_BuyBox_list[asin],
                    Sale_Price_FBM = sale_price_FBM_list[asin],
                    Sale_Price_FBA = sale_price_FBA_list[asin],
                    )
                data.save(using='mysql')
                new = completed_db(User = user , Asin = Asins[asin])
                new.save(using='mysql')
                
        for asin in len(Asins):
            try:
                check = completed_db.objects.get(Asin= Asins[asin] , Buy_Price= Buy_Prices[asin])
                if check.User == user:
                    continue
                else : 
                    if (check.Date - datetime.now()).day >=7:
                        dataSaver(asin=Asins[asin])
                    else :
                        #test edilecek 
                        data = check
                        data.User = user
                        data.save(using='mysql')                         
            except:
                try:
                    data = notCompleted_db.objects.get(Asin = Asins[asin])
                    data.delete()
                    dataSaver(asin = Asins[asin])
                except:
                    dataSaver(asin=Asins[asin])            
    except:
        return 'Dosyalari kontrol edin'

