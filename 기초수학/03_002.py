'''
파이썬을 이용해서 사용자가 입력한 숫자의 약수를 출력해보자.
'''

inputNumber = int(input('0보다 큰 정수 입력: '))

for number in range(1, (inputNumber + 1)):
    if inputNumber % number == 0:
        print('{}의 약수: {}'.format(inputNumber, number))
        
        
'''
파이썬을 이용해서 사용자가 입력한 숫자까지의 소수를 출력해보자.
'''

for number in range(2, (inputNumber + 1)):
    flag = True
    for n in range(2, number):
        if number % n ==0:
            flag = False
            break
    
    if (flag):
        print('{}: 소수!!'.format(number))
    else:
        print('{}: 합성수!!'.format(number))