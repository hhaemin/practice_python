'''
다음 수열의 일반항을 구하고 n번째항의 값과 합을 구하는 프로그램을 만들어보자
{4, 10, 16, 22, 28, 34, 40, 46, 52, 58, 64,...}
'''

inputA1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력: '))

valueN = 0              # N번째 항의 값
sumN = 0                # N번째항 까지의 합
n = 1
while n <= inputN:

    if n == 1:
        valueN = inputA1
        sumN += valueN
        print('{}번째 항의 값: {}'.format(n, valueN))
        print('{}번째 항까지의 합: {}'.format(n, sumN))
        n += 1
        continue

    valueN += inputD
    sumN += valueN
    print('{}번째 항의 값: {}'.format(n, valueN))
    print('{}번째 항까지의 합: {}'.format(n, sumN))
    n += 1

print('{}번째 항의 값: {}'.format(inputN, valueN))
print('{}번째 항까지의 합: {}'.format(inputN, sumN))


# 등차 수열(일반항) 공식: an = a1 + (n-1) * d
valueN = inputA1 + (inputN-1) * inputD
print('{}번째 항의 값: {}'.format(inputN, valueN))

# 등차 수열(합) 공식: sn = n(a1 + an) / 2
sumN = inputN * (inputA1 + valueN) / 2
print('{}번째 항까지의 합: {}'.format(inputN, int(sumN)))