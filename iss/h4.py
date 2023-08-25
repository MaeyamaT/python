import requests as req
import json
import turtle
screen=turtle.Screen()
screen.setup(1000,500)
screen.bgpic('earth.gif')
#座標系を変換
screen.setworldcoordinates(-180,-90,180,90)

iss=turtle.Turtle()
turtle.register_shape('iss.gif')#画像を登録
iss.shape('iss.gif')#見た目を設定

url='http://api.open-notify.org/iss-now.json'
res=req.get(url)
data=json.loads(res.text)
pos=data['iss_position']
lat=float(pos['latitude'])
lng=float(pos['longitude'])

iss.penup()
iss.goto(lng,lat)
iss.pendown()

turtle.mainloop()
