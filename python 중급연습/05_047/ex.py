'''
상품 구매 개수에 따라 할인율이 결정되는 모듈을 만들고,
다음과 같이 계산 결과가 출력되는 프로그램을 만들어보자

구매개수 : 1개 - 할인율 5%
구매개수 : 2개 - 할인율 10%
구매개수 : 3개 - 할인율 15%
구매개수 : 4개 - 할인율 20%
구매개수 : 5개 이상 - 할인율 25%
'''

import discount as dc

if __name__ == '__main__':
    
    flag = True
    gs = []
    
    while flag:
        
        selectNumber = int(input('1.구매, 2.종료'))
        
        if selectNumber == 1:
            goods_price = int(input('상품 가격 입력:'))
            gs.append(goods_price)
            
        elif selectNumber == 2:
            result = dc.calcularotTotalPrice(gs)
            flag = False
    
    print(f'할인율: {result[0]}%')
    print(f'합계: {dc.formatedNumber(result[1])}원')