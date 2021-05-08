import requests
import datetime
from dateutil.tz import gettz

todays_date = datetime.datetime.now(tz=gettz('Asia/Kolkata')).strftime("%d-%m-%Y")
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=110052&date=" + str(todays_date)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
r=requests.get(url=URL, headers = headers)
#print(r)
data = r.json()
for centre in data["centers"]:
    for session in centre["sessions"]:
        if session["min_age_limit"] == 18:
            print(centre["name"], session['date'])
