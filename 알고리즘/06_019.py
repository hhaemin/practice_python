import random

nums = random.sample(range(0, 50), 20)
print(f'nums: {nums}')

inputNum = int(input('input number: '))
print(f'inputNum: {inputNum}')
nearNum = 0
minNum = 50

for n in nums:
    # abs() : 절대값 함수
    absNum = abs(n - inputNum)
    # print(f'absNum: {absNum}')
    if absNum < minNum:
        minNum = absNum
        nearNum = n

print(f'nearNum: {nearNum}')