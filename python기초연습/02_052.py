'''
난수를 이용해서 홀/짝 게임을 만들어보자
'''

import random

comNum = random.randint(1,2)
userSelect = int(input('홀/짝 선택: 1.홀 \t 2.짝'))

if comNum == 1 and userSelect == 1: 
    print('빙고!! 홀수!!!')
elif comNum == 2 and userSelect ==2:
    print('빙고!! 짝수!!!')
elif comNum == 1 and userSelect ==2:
    print('실패!! 홀수!!!')
elif comNum == 2 and userSelect ==1:
    print('실패!! 짝수!!!')
