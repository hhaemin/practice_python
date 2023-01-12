'''
백신 접종 대상자를 구분하기 위한 프로그램
19세 이하 또는 65세 이상이면 출생 연도 끝자리에 따른 접종
그렇지 않으면 하반기 일정 확인
'''

inputAge = int(input('나이 입력: '))

if inputAge <=19 or inputAge >= 65:
    endNum = int(input('출생 연도 끝자리 입력 : '))
    if endNum == 1 or endNum == 6:
        print('월요일 접종 가능!!')
    if endNum == 2 or endNum == 7:
        print('화요일 접종 가능!!')
    if endNum == 3 or endNum == 8:
        print('수요일 접종 가능!!')
    if endNum == 4 or endNum == 9:
        print('목요일 접종 가능!!')
    if endNum == 5 or endNum == 0:
        print('금요일 접종 가능!!')
else:
    print('하반기 일정 확인하세요')
        