'''
친구 이름 다섯 명을 리스트에 저장하고 오름차순과 내림차순으로 정렬
'''
friends = []

for i in range(5):
    friends.append(input('친구 이름 입력: '))

print(f'친구들 : {friends}')

friends.sort()
print(f'오름차순 : {friends}')

friends.sort(reverse=True)
print(f'내림차순 : {friends}')

'''
다음 리스트에서 중복 아이템(숫자)를 제거하는 프로그램
'''


numbers = [2, 22, 7, 8, 9, 2, 7, 3, 5, 2, 7, 1, 3]
print(f'numbers : {numbers}')

for n in numbers:
    if numbers.count(n) >= 2:
        numbers.remove(n)

print(f'numbers : {numbers}')
