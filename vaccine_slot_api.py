import urllib3
import json
from datetime import date
 
http = urllib3.PoolManager()

base_url = "http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
today = date.today().strftime("%d-%m-%Y")

#Adjust according to your pincode area
pincode = '825312'

req = http.request('GET', base_url, fields={'pincode':pincode, 'date':today})
res = json.loads(req.data.decode('utf-8'))

available_vaccine_info = []

for centers in res['centers']:
    
    name = centers['name']
    sessions = centers['sessions']
    
    for ses in sessions:
        date               = ses['date']
        age_limit          = ses['min_age_limit']
        vaccine            = ses['vaccine']
        available_capacity = ses['available_capacity']
        dose1              = ses['available_capacity_dose1']
        dose2              = ses['available_capacity_dose2']
        
        if(available_capacity>0):
            info = { 
                'center':name,
                'date':date,
                'age_limit' : str(age_limit)+'+',
                'availablity':available_capacity
                }
            available_vaccine_info.append(info)
            
#print(available_vaccine_info)
        
    
        
    

    
    