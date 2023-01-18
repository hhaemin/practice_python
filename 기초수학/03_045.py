'''
<팩토리얼>
팩토리얼 프로그램을 만들되, 반복문을 이용한 함수와 재귀함수를 이용해서
구현해보고 또한, 파이썬에서 제공하는 모듈도 사용하는 방법
'''

# 반복문을 이용한 경우
def facFun1(n):
    
    fac = 1
    for n in range(1, (n+1)):
        fac *= n
        
    return fac

num = int(input('input number: '))
print(f'{num}!: {facFun1(num)}')

# 재귀 함수를 이용한 경우
def facFun2(n):
    
    if n ==1:
        return n
    
    return n * facFun2(n-1)

num = int(input('input number: '))
print(f'{num}!: {facFun2(num)}')

# python에서 제공하는 모듈 이용

import math

num = int(input('input number: '))
print(f'{num}!: {math.factorial(num)}')
