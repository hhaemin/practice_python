'''
사용자가 입력한 수를 이용해서, 진법 변환하는 코드

10진수-> 2,8,16진수 변환
x진수 -> 10진수
x진수 -> x진수
'''

dNum = int(input('10진수 입력: '))

# 10진수 > 2, 8, 16진수
print('2진수: {}'.format(bin(dNum)))
print('8진수: {}'.format(oct(dNum)))
print('16진수: {}'.format(hex(dNum)))


# X진수 -> 10진수
print('2진수(0b10101) -> 10진수({})'.format(int('0b10101', 2)))
print('8진수(0o135) -> 10진수({})'.format(int('0o135', 8)))
print('16진수(0x5f) -> 10진수({})'.format(int('0x5f', 16)))


# X진수 -> X진수
print('2진수(0b10101) -> 8진수({})'.format(oct(0b10101)))
print('2진수(0b10101) -> 10진수({})'.format(int(0b10101)))
print('2진수(0b10101) -> 16진수({})'.format(hex(0b10101)))


print('8진수(0o675) -> 2진수({})'.format(bin(0o675)))
print('8진수(0o675) -> 10진수({})'.format(int(0o675)))
print('8진수(0o675) -> 16진수({})'.format(hex(0o675)))


print('16진수(0x45d) -> 2진수({})'.format(bin(0x45d)))
print('16진수(0x45d) -> 8진수({})'.format(oct(0x45d)))
print('16진수(0x45d) -> 10진수({})'.format(int(0x45d)))