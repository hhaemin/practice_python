import random

types = ['A', 'B', 'AB', 'O']
todayData = []
typeCnt = []

for i in range(100):
    type = types[random.randrange(len(types))]
    todayData.append(type)

print('todayData : {}'.format(todayData))
print('todayData length : {}'.format(len(todayData)))

for type in types:
    print('{}형 \t : {}개'.format(type, todayData.count(type)))




