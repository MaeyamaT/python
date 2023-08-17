def eat(**kwargs):
    for key in kwargs:
        print(f'{key}に{kwargs[key]}を食べました')

eat(朝食='納豆',遅めの昼食='パスタ',夕方のおやつ='カレーパン')
