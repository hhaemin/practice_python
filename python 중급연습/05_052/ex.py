''' 
다음과 같이 패키지와 모듈을 만들고 연산 결과를 출력해보자

arithmetic
    basic_operator.py               # 덧셈, 뺼셈, 곱셈, 나눗셈
    developer_operator.py           # 나머지, 몫, 거듭제곱
shape
    circle_area.py                  # 원의 넓이
    triangle_square_area.py         # 삼각형, 사각형의 넓이
'''

from arithmetic import basic_operator as bo
from arithmetic import developer_operator as do

from shape import triangle_square_area as tsa
from shape import circle_area as ca

inputNumber1 = float(input('숫자1 입력: '))
inputNumber2 = float(input('숫자2 입력: '))

print(f'{inputNumber1} + {inputNumber2} = {bo.add(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} - {inputNumber2} = {bo.sub(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} * {inputNumber2} = {bo.mul(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} / {inputNumber2} = {bo.div(inputNumber1, inputNumber2)}')

print(f'{inputNumber1} % {inputNumber2} = {do.mod(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} // {inputNumber2} = {do.flo(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} ** {inputNumber2} = {do.exp(inputNumber1, inputNumber2)}')

inputWidth = float(input('가로 길이 입력: '))
inputHeight = float(input('세로 길이 입력: '))

print(f'삼각형 넓이: {tsa.calTriangleArea(inputWidth, inputHeight)}')
print(f'사각형 넓이: {tsa.calSquareArea(inputWidth, inputHeight)}')

inputRadius = float(input('반지름 입력: '))
print(f'원의 넓이: {ca.calCircleArea(inputRadius)}')