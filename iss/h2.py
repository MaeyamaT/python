import requests as req
import json
url='http://api.open-notify.org/iss-now.json'
res=req.get(url)
data=json.loads(res.text)
pos=data['iss_position']
print(f"ISSの緯度は{pos['latitude']},経度は{pos['longitude']}")
