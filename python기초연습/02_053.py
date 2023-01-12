'''
조건문 04
상수도 요금 계산기를 만들어보자
가정용) 사용량에 관계없이 540원
대중탕용)
사용량 50이하 820원
50초과 300이하 1,920원
300초과 2,400원
공업용)
사용량 500이하 240원
500초과 470원
'''

part = input('업종 선택(1.가정용    2.대중탕용    3.공업용) : ')
useWater = int(input('사용량 입력: '))
unitPrice = 0

if part == 1:
    unitPrice = 540

elif part ==2:
    if useWater <= 50:
        unitPrice = 820
    elif useWater > 50 and useWater <=300:
        unitPrice = 1920
    elif useWater > 300:
        unitPrice = 2400
        
elif part ==3:
    if useWater <=500:
        unitPrice = 240
    else:
        unitPrice = 470

print('=' * 30)
print('상수도 요금표')
print('=' * 30)
print('사용량 : 요금')
userPrice = useWater * unitPrice
print('{} : {}원'.format(useWater, userPrice))
print('=' * 30)