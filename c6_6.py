scores1=[80,40,50]
scores2=[80,40,50]
print(f'scores1のidentity:{id(scores1)}')
print(f'scores2のidentity:{id(scores2)}')

if scores1==scores2:
    print('同じ内容です')
else:
    print('違う内容です')

if id(scores1)==id(scores2):
    print('同じ存在です')
else:
    print('違う存在です')

brefore_names=['a','b','c']
"""
copied_names=list()
for n in before_names:
    copied_names.append(n)
"""
copied_names=before_names[:]
