'''
2개의 튜플에 대해서 합집합과 교집합을 출력
tuple1 = (1,3,2,6,12,5,7,8)
tuple2 = (0,5,2,9,8,6,17,3)
'''

# tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
# tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

# tempHap = list(tuple1)
# tempGyo = list()

# for n in tuple2:
#     if n not in tempHap:
#         tempHap.append(n)
#     else:
#         tempGyo.append(n)

# tempHap = tuple(sorted(tempHap))
# tempGyo = tuple(sorted(tempGyo))

# print(f'합집합(중복X)\t : {tempHap}')
# print(f'교집합\t\t : {tempGyo}')


# while문으로 할 때
tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

tempHap = tuple1 + tuple2
tempGyo = list()
tempHap = list(tempHap)

print(f'tempHap: {tempHap}')
print(f'tempGyo: {tempGyo}')

idx = 0
while True:
    
    if idx >= len(tempHap):
        break
    
    if tempHap.count(tempHap[idx]) >=2:
        tempGyo.append(tempHap[idx])
        tempHap.remove(tempHap[idx])
        continue
    
    idx +=1
    
print(f'tempHap: {tempHap}')
print(f'tempHap(tuple): {tuple(sorted(tempHap))}')

print(f'tempGyo: {tempGyo}')
print(f'tempGyo(tuple): {tuple(sorted(tempGyo))}')