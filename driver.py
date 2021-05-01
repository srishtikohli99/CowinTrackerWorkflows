import requests
import datetime
from dateutil.tz import gettz

todays_date = datetime.datetime.now(tz=gettz('Asia/Kolkata')).strftime("%d-%m-%Y")
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=110058&date=" + str(todays_date)
r=requests.get(url=URL)
#print(r)
data = r.json()
for centre in data["centers"]:
    for session in centre["sessions"]:
        if session["min_age_limit"] == 18:
            print(centre["name"], session['date'])