dog_name=input('犬の名前を入力してください>')
dog_age=input('犬の年齢を入力してください>')
human_age=int(dog_age)*7
print(dog_name,'は今',dog_age,'才、人間に換算すると',human_age,'才です',sep='')
print(f'{dog_name}は今{dog_age}才、人間に換算すると{human_age}才です')
