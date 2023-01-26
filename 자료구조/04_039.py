'''
1부터 사용자가 입력한 숫자까지의 약수와 소수를 리스트에 각각 지정하고,
이것을 출력하는 프로그램
'''

inputNum = int(input('1보다 큰 정수 입력: '))
listA = []
listB = []

for n in range(1, inputNum+1):
    if n == 1:
        listA.append(n)
    else:
        if inputNum % n == 0:
            listA.append(n)

for number in range(2, inputNum+1):
    flag = True
    for n in range(2, number):
        if number % n == 0:
            flag = False
            break

    if flag:
        listB.append(number)




print(f'{inputNum}의 약수: {listA}')
print(f'{inputNum}까지의 소수: {listB}')