'''
과목별 점수를 입력하면 합격 여부를 출력하는 모듈을 만들어보자
(평균 60이상 합격, 과락 40으로 한다)
'''

import passOrFail as pf

if  __name__=='__main__':
    sub1 = int(input('과목1 점수 입력: '))
    sub2 = int(input('과목2 점수 입력: '))
    sub3 = int(input('과목3 점수 입력: '))
    sub4 = int(input('과목4 점수 입력: '))
    sub5 = int(input('과목5 점수 입력: '))
    
    pf.exampleResult(sub1, sub2, sub3, sub4, sub5)