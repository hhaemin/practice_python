'''
교통 과속 위반 프로그램
시속 50km 이하 -> 안전속도 준수!!
시속 50km 초과 -> 안전속도 위반!! 과태료 50,000원 부과 대상!!
'''

carSpeed = int(input('속도 입력: '))
limitSpeed = 50

if carSpeed > 50:
    print('안전속도 위반!! 과태료 50,000원 부과 대상!!')
else: 
    print('안전속도 준수!!')