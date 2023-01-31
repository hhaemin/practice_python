'''
리스트에서 아스키코드가 가장 큰 값을 찾는 알고리즘
'''

class MaxAlgorithm:

    def __init__(self, cs):
        self.chars = cs
        self.maxChar = 0

    def getMaxChar(self):
        self.maxChar = self.chars[0]

        for c in self.chars:
            # ord() : 문자열을 아스키코드로 변환해 주는 함수
            if ord(self.maxChar) < ord(c):
                self.maxChar = c

        return self.maxChar

ma = MaxAlgorithm(['c', 'x', 'Q', 'A', 'e', 'P', 'p'])
maxChar = ma.getMaxChar()
print(f'maxChar: {maxChar}')