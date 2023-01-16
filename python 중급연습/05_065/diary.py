'''
회원 계정별 텍스트 파일을 생성한 후 회원 본인 파일에 
한 줄 일기를 쓰고 읽는 프로그램을 만들어보자
'''
import time

def writeDiary(u, f, d):
    lt = time.localtime()
    timeStr = time.strftime('%Y-%m-%d %I:%M:%s %p', lt)
    
    filePath = u + f
    with open(filePath,'a') as f:
        f.write(f'[{timeStr}] {d}\n')

def readDiary(u, f):
    filePath = u + f
    datas = []
    with open(filePath,'r') as f:
        datas = f.readlines()
        
    return datas