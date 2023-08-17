def weather():
    print('今日は晴れです')
weather()

def calc_circle_area(r:float)->float:
    return r*r*3.14

print(calc_circle_area(3.0))

def nowstr()->str:
    return '18時25分30秒'

print(nowstr())


def nowint()->tuple:
    return (18,25,30)

h,m,s=nowint()
print(h,m,s)

def is_leapyear(year:int) -> bool:
    return year%400==0 or (year%4==0 and year%100 !=0)

print(is_leapyear(2023)) #False
print(is_leapyear(2020)) #True

year=int(input('何年>>'))
if(is_leapyear(year)):
    print(f'西暦{year}年はうるう年です')
else:
    print(f'西暦{year}年はうるう年ではありません')

