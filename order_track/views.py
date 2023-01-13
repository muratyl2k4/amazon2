from django.shortcuts import render
from .models import Order
from .trackApi import TrackingApi
from datetime import datetime 
import urllib.request
import json

def kargotakip(request):
    liste = []
    if request.method == "POST":
        apiKey = "r2k8yxvv-afjo-bhpn-e3vq-k3v38keny7tw"
        tracker = TrackingApi(apiKey)
        tracker.sandbox = False
        tracknumber = ['18221A0000975737']
        result = Order.objects.values()
        
        #for abc in result:
        
        #    tracknumber.append(str(abc.get("Tracknumber")))

        print(tracknumber)
        
        if 1 == 2:
            pass
        else:
            post = []
            for xxx in tracknumber:
                
                post.append({"tracking_number": xxx, "courier_code": "apc"})
                postData = json.dumps(post)

                # create tracking number
                result = tracker.doRequest("create", postData, "POST")
                    

                # # Get tracking results of a  tracking or List all trackings
                get = f"get?tracking_numbers={xxx}"
                result = tracker.doRequest(get)
                dict = json.loads(result.decode('utf-8'))
                print(dict)
                for abc in dict.get("data"):
                    if abc.get('latest_event'):
                        list = abc.get('latest_event').split(",")
                        datetimesplit = list[-1].split(" ")
                        Status = list[0]
                        Location = list[1]
                        if len(list) == 4:
                            Location = list[1] + " " +list [2]
                        
                        elif len(list) == 5:
                            Location = list[1] + " " +list [2] + " " +list[3]
                        Date = datetimesplit[0]
                        
                        Time = datetimesplit[1]
                        
            
                        kargodate = f"{Date} {Time}"

                        datetime_object = datetime.strptime(kargodate, "%Y-%m-%d %H:%M:%S")
                        print(datetime_object)

                        anlik = datetime.now()
                        gecensure = anlik - datetime_object
                        
                        if gecensure.total_seconds() <= 3600:
                            lastupdate = int(gecensure.total_seconds() / 60) + "Dakika"
                        elif gecensure.total_seconds() > 3600 and gecensure.total_seconds() < 86400:
                            lastupdate = int(gecensure.total_seconds() /3600) + "Saat"
                        elif gecensure.total_seconds() >= 86400:
                            lastupdate = f"{int(gecensure.total_seconds() / 86400)} Gün"
                        
                        if Status == "Delivered":
                            bg = "bg-success"

                        elif int(gecensure.total_seconds() /86400)>= 2 :
                            bg = "bg-warning"
                        else:
                            bg = "bg-primary"
                        informations = ({"Tracknumber" : xxx , "Status" : Status , "Time" : Time , "Location" : Location , "Date" : Date , "lastupdate" : lastupdate , "bg" : bg})
                        liste.append(informations)


    
    data = {        
        "info" : liste
    }


    return render(request , "kargotakip.html" , data)