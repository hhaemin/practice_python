myInfo = {}

myInfo['이름'] = '박경진'
myInfo['전공'] = 'computer'
myInfo['메일'] = 'jin@naver.com'
myInfo['학년'] = 3
myInfo['주소'] = '대한민국 서울'
myInfo['취미'] = ['요리', '여행']

print(f'myInfo : {myInfo}')

myInfo['메일'] = 'gyeongjin@naver.com'
print(f'myInfo : {myInfo}')

factorialDic = {}
for i in range(11):
    if i == 0:
        factorialDic[i] = 1
    else:
        for j in range(1, (i+1)):
            factorialDic[i] = factorialDic[i-1] * j

print(f'factorialDic : {factorialDic}')