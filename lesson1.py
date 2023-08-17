num=int(input('正の整数を入力してください>'))
#print(sum(range(1,n+1)))
total=0
for i in range(1,num+1):
    total+=i
print(total)


start=int(input('start>>'))
end=int(input('end>>'))
for i in range(start,end+1):
    if i%2==0:
        print(i,end=' ')
print()
