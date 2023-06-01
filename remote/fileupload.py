import pandas as pd 
from .models import *
from datetime import datetime
def keepa_excel(com_file , target_file , keepa_db , completed_db , notCompleted_db , user):
    com_pd_file =pd.read_excel(com_file)[['Title','ASIN','Buy Box: Current','New: Current','New, 3rd Party FBA: Current','New, 3rd Party FBM: Current']]
    target_pd_file = pd.read_excel(target_file)[['ASIN','Sales Rank: Current','Sales Rank: Drops last 30 days','Buy Box: Current','New: Current','New, 3rd Party FBA: Current','New, 3rd Party FBM: Current','Referral Fee %','FBA Fees:']]

    df = pd.merge(com_pd_file, target_pd_file, on="ASIN")    
    
    try: 
        com_pd_file.rename(columns = {'New, 3rd Party FBM: Current':'Buy_Price_FBM'}, inplace = True)
        com_pd_file.rename(columns = {'New, 3rd Party FBA: Current':'Buy_Price_FBA'}, inplace = True)
        com_pd_file.rename(columns = {'New: Current':'Buy_Price_NC'}, inplace = True)
        com_pd_file.rename(columns = {'Buy Box: Current':'Buy_Price_BB'}, inplace =True)


        target_pd_file.rename(columns = {'Sales Rank: Current':'SalesRank'}, inplace = True)
        target_pd_file.rename(columns = {'Sales Rank: Drops last 30 days':'Drop_Count'}, inplace = True)

        target_pd_file.rename(columns = {'New, 3rd Party FBM: Current':'Sale_Price_FBM'}, inplace = True)
        target_pd_file.rename(columns = {'New, 3rd Party FBA: Current':'Sale_Price_FBA'}, inplace = True)
        target_pd_file.rename(columns = {'New: Current':'Sale_Price_NC'}, inplace = True)
        target_pd_file.rename(columns = {'Buy Box: Current':'Sale_Price_BB'}, inplace = True)
        target_pd_file.rename(columns = {'Referral Fee %':'Referral_Fee_Percentage'}, inplace = True)
        target_pd_file.rename(columns = {'FBA Fees:':'Pick_and_Pack_Fee'},inplace= True)

        df = pd.merge(com_pd_file, target_pd_file, on=["ASIN" , 'ASIN'])    


        Titles = [a for a in df['Title']]
        Asins = [a for a in df['ASIN']]
        SalesRanks = [a for a in df['SalesRank']]
        Drop_Counts = [a for a in df['Drop_Count']]
        Buy_Price_FBAs = [a for a in df['Buy_Price_FBA']]
        Buy_Price_FBMs = [a for a in df['Buy_Price_FBM']]
        Buy_Price_NCs = [a for a in df['Buy_Price_NC']]
        Buy_Price_BBs = [a for a in df['Buy_Price_BB']]
        Sale_Price_NCs = [a for a in df['Sale_Price_NC']]
        Sale_Price_FBMs = [a for a in df['Sale_Price_FBM']]
        Sale_Price_FBAs = [a for a in df['Sale_Price_FBA']]
        Sale_Price_BBs = [a for a in df['Sale_Price_BB']]
        Referral_Fee_Percentages = [a for a in df['Referral_Fee_Percentage']]
        Pick_and_Pack_Fees = [a for a in df['Pick_and_Pack_Fee']]
        
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
                    Drop_Count = Drop_Counts[asin],
                    Buy_Price_FBA = Buy_Price_FBAs[asin],
                    Buy_Price_FBM = Buy_Price_FBMs[asin],
                    Buy_Price_BB = Buy_Price_BBs[asin],
                    Buy_Price_NC = Buy_Price_NCs[asin],
                    Sale_Price_NC = Sale_Price_NCs[asin],
                    Sale_Price_BB = Sale_Price_BBs[asin],
                    Sale_Price_FBM = Sale_Price_FBMs[asin],
                    Sale_Price_FBA = Sale_Price_FBAs[asin],
                    Referral_Fee_Percentage = Referral_Fee_Percentages[asin],
                    Pick_and_Pack_Fee = Pick_and_Pack_Fees[asin]
                    )
                data.save(using='mysql')
                new = completed_db(User = user , Asin = Asins[asin])
                new.save(using='mysql')
                
        for asin in range(len(Asins)):
            asin = int(asin)
            try:
                check = completed_db.objects.get(Asin= Asins[asin] , Referral_Fee_Percentage= Referral_Fee_Percentages[asin])
                check2nd = datetime.now() - check.Date      
                if check.User == user:
                    continue
                else : 
                    if (datetime.now() - check.Date).day >=7:
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
                    dataSaver(asin = asin)
                except:
                    dataSaver(asin=asin)            
    except Exception as e:
        print(e)

