'''
다음 추상 클래스를 이용해서 한/영, 한/일 사전 클래스를 만들어보자
'''

import ADictionary as dic

kTe = dic.KorToEng()

kTe.registWord('책', 'book')
kTe.registWord('나비', 'butterfly')
kTe.registWord('연필', 'pencil')
kTe.registWord('학생', 'student')
kTe.registWord('선생님', 'teacher')

kTe.printWords()

kTe.updateWord('책', 'book')
kTe.printWords()

print(f'책: {kTe.searchWord("책")}')