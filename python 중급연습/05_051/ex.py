'''
수입과 공과금을 입력하면 공과금 총액과 수입 대비 공과금 비율을 계산하는
모듈을 만들어보자

수도요금 - 15,000
전기요금 - 17,500
가스요금 - 125,000
'''

import utilityBill as ub

inputIncome = int(input('수입 입력: '))
ub.setIncome(inputIncome)

inputWaterPrice = int(input('수도요금 입력: '))
ub.setWaterPrice(inputWaterPrice)

inputElectricPrice = int(input('전기요금 입력: '))
ub.setElectricPrice(inputElectricPrice)

inputGasPrice = int(input('가스요금 입력: '))
ub.setGasPrice(inputGasPrice)

print(f'공과금 : {ub.getUtilityBill()}원')
print(f'수입 대비 공과금 비율: {ub.getUtilityBillRate()}')