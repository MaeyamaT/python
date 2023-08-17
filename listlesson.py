ls=[4,10,2,5,7]
print(ls) #[4,10,2,5,7]
print(len(ls)) # 5
print(ls[0]) # 4
print(ls[-1]) # 7

#リストの走査
for i in ls:
    print(i)

ls[0]=1 #要素の更新

ls.append(10) #末尾の追加

del ls[-1] #リストの最後の要素削除

n=ls.pop() #リストの末尾を削除して、nに代入
n=ls.pop(0) #先頭を削除してnに代入

ls2=[1,2,3]
ls3=[4,5,6]
ls4=ls2 + ls3 #[1,2,3,4,5,6]

ls5=ls2 * 3 #[1,2,3,1,2,3,1,2,3]

ls6=[3,1,4]
ls6.sort() #昇順ソート
ls6.sort(reverse=True) #降順ソート
print(ls6)

#リストシャッフル
ls7=[1,2,3,4,5]
import random
random.shuffle(ls7) #シャッフル完了
print(ls7)

data=['大吉','中吉','吉','凶']
result=random.choice(data)
print(result)
