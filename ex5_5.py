def int_input(msg:str)->int:
    return int(input(f'{msg}>>'))

def calc_payment(amount:int,people:int=2)->tuple:
    dnum=amount/people
    pay=dnum//100*100
    if dnum>pay:
        pay=int(pay+100)
    payorg=amount-pay*(people-1)
    return (pay,payorg)

def show_payment(pay:int,payorg:int,people:int=2):
    print('***支払額***')
    print(f'1人あたり{pay}円({people-1}人),幹事は{payorg}円です')

amount=int_input('支払い総額を入力してください')
people=int_input('参加人数を入力してください')

pay,payorg=calc_payment(amount,people)

show_payment(pay,payorg,people)
