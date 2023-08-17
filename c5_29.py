def eat(breakfast,lunch='',dinner='カレー',*desserts):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')

    for d in desserts:
        print(f'おやつに{d}をたべました')

print('8月1日')
eat('トースト','パスタ','カレー','アイス','チョコ','カレー')

def sumof(*args):
    total=0
    for i in args:
        total+=i
    return total
print(sumof()) #0
print(sumof(3,5)) #8
print(sumof(3,5,7)) #15
