'''
72에 x를 곱하면 y의 제곱이 된다고 할 때, x에 해당하는 가장 작은 정수는?
'''

inputNumber = int(input('1보다 큰 정수 입력: '))

n =2 
searchNumbers = []
while n <= inputNumber:
    if inputNumber % n == 0:
        print('소인수: {}'.format(n))
        if searchNumbers.count(n) == 0:
            searchNumbers.append(n)
        elif searchNumbers.count(n) ==1:
            searchNumbers.remove(n)
        inputNumber /= n 
    else:
        n += 1