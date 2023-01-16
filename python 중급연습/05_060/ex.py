'''
사용자가 입력한 숫자를 이용해서 산술연산 결과를 출력하는
모듈을 만들되, 예상하는 예외에 대한 예외처리 코드를 작성해보자
'''

import calculator as cc

num1 = input('첫 번째 피연산자 입력: ')
num2 = input('두 번째 피연산자 입력: ')

cc.add(num1, num2)