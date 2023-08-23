try:
    price=int(input('料金を入力>>'))
    number=int(input('人数を入力>>'))
    print(f'1人あたり{price/number}円です')
except:
    print('料金と人数に適切な整数を入力してください')

print('プログラムを終了します')
