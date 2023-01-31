'''
<선형검색 알고리즘> : 선형으로 나열되어 있는 데이터를 순차적으로 스캔하면서 원하는 값을 찾는다.

숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들어보자
1. 검색 모듈은 선형 검색 알고리즘을 이용하자
2. 리스트는 1부터 20까지의 정수 중에서 난수 10개를 이용하자
3. 검색 과정을 로그로 출력하자
4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없다면 -1을 출력하자.
'''

import lineMod
import random

if __name__ == '__main__':

    rNums = random.sample(range(1, 21), 10)
    searchNum = int(input('input search number: '))

    resultIdx = lineMod.searchNumberByLineAlgorithm(rNums, searchNum)
    if resultIdx == -1:
        print('No resutls found')
        print(f'search result index: {resultIdx}')

    else:
        print('>>> Search Results <<<')
        print(f'search result index: {resultIdx}')
        print(f'search result number: {rNums[resultIdx]}')