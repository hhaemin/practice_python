'''
파이썬을 이용해서 사용자가 입력한 수를 소인수분해하자
'''

inputNumber = int(input('1보다 큰 정수 입력: '))

n =2 
while n <= inputNumber:
    if inputNumber % n ==0:
        print('소인수: {}'.format(n))
        inputNumber /=n
    else:
        n+=1