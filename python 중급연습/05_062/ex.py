'''
상품 구매에 따른 '총 구매 금액'을 출력하되,
다음과 같이 개수가 잘 못 입력된 경우
별도로 출력하도록 프로그램을 만들어보자
'''

import calculatorPurchase as cp

g1Cnt = input('goods1 구매 개수: ')
g2Cnt = input('goods2 구매 개수: ')
g3Cnt = input('goods3 구매 개수: ')
g4Cnt = input('goods4 구매 개수: ')
g5Cnt = input('goods5 구매 개수: ')

cp.calculator(g1Cnt, g2Cnt, g3Cnt, g4Cnt, g5Cnt)