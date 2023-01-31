'''
재귀 알고리즘을 이용한 최대 공약수 계산
• 유클리드 호제법
• 두자연수n1,n2에대하여(n1>n2)n1를n2로나눈나머지를r이라고할때, 
• n1과n2의최대공약수는n2와r의최대공약수와같다
'''

# def greatestCommonDevide(n1, n2):
#     maxNum = 0
#     for i in range(1, (n1 + 1)):
#         if n1 % i == 0 and n2 % i == 0:
#             maxNum = i
#
#     return maxNum
#
# print(f'gcd(82, 32): {greatestCommonDevide(82, 32)}')
# print(f'gcd(96, 40): {greatestCommonDevide(96, 40)}')



def gcd(n1, n2):

    if n1 % n2 == 0:
        return n2
    else:
        return gcd(n2, n1 % n2)

print(f'gcd(82, 32): {gcd(82, 32)}')
print(f'gcd(96, 40): {gcd(96, 40)}')