from .models import Order
from .trackApi import TrackingApi
from datetime import datetime 
import json
def order_track(apiKey):
    tracker = TrackingApi(apiKey)
    tracker.sandbox = False
    result = Order.objects.values()
    tracknumber = [str(abc.get("Tracknumber")) for abc in result]
    order_list = []
    print(tracknumber)
    post = []
    for xxx in tracknumber:
        post.append({"tracking_number": xxx, "courier_code": "landmark-global"})
        postData = json.dumps(post)
        # create tracking number
        result = tracker.doRequest("create", postData, "POST")
        # # Get tracking results of a tracking or List all trackings
        get = f"get?tracking_numbers={xxx}"
        result = tracker.doRequest(get)
        dict = json.loads(result.decode('utf-8'))
        for abc in dict.get("data"):
            if abc.get('latest_event'):
                ## SIPARIS SON DURUMU 
                list = abc.get('latest_event').split(",")
                datetimesplit = list[-1].split(" ")
                Status = list[0]
                Location = list[1]
                if len(list) == 4:
                    Location = list[1] + " " +list [2]
                elif len(list) == 5:
                    Location = list[1] + " " +list [2] + " " +list[3]
                ## ZAMAN
                Date = datetimesplit[0]
                Time = datetimesplit[1]
                kargodate = f"{Date} {Time}"
                datetime_object = datetime.strptime(kargodate, "%Y-%m-%d %H:%M:%S")
                anlik = datetime.now()
                gecensure = anlik - datetime_object
                ## GECEN SURE 
                if gecensure.total_seconds() <= 3600:
                    lastupdate = int(gecensure.total_seconds() / 60) + "Dakika"
                elif gecensure.total_seconds() > 3600 and gecensure.total_seconds() < 86400:
                    lastupdate = int(gecensure.total_seconds() /3600) + "Saat"
                elif gecensure.total_seconds() >= 86400:
                    lastupdate = f"{int(gecensure.total_seconds() / 86400)} Gün"
                ## SON DURUM - KART RENGI 
                if Status == "Delivered":
                    bg = "bg-success"
                elif int(gecensure.total_seconds() /86400)>= 2 :
                    bg = "bg-warning"
                else:
                    bg = "bg-primary"
                informations = ({"Tracknumber" : xxx , "Status" : Status , "Time" : Time , "Location" : Location , "Date" : Date , "lastupdate" : lastupdate , "bg" : bg})
                order_list.append(informations)    
    return order_list