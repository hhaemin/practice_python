'''
금액, 이율, 거치기간을 입력하면 복리계산하는 복리계산기 프로그램을 만들어보자
'''

money = int(input('금액 입력: '))
rate = float(input('이율 입력: '))
term = int(input('기간 입력: '))

targetMoney = money

for i in range(term):
    targetMoney += (targetMoney * rate * 0.01) # 원금 + 이자(이율을 100으로 나눠줘야하므로 0.01을 곱해준다)
    
targetMoneyFormated = format(int(targetMoney), ',') #int로 정리해주고, 세자리씩 끊어보이게 하는 것

print('-' * 30)
print('이율 : {}%'.format(rate))
print('원금 : {}원'.format(format(money,',')))
print('{}년 후 금액: {}원'.format(term, targetMoneyFormated))
print('-' * 30)