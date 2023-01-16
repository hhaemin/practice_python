'''
회원가입 클래스와 회원정보를 관리하는 클래스를 만들고 회원가입 로그인 기능을 구현

#회원가입
아이디 입력:
비밀번호 입력:
...

#전체회원 조회
ID:
PW:
...

#로그인
abc@gmail.com: Log-in success!!

#회원 정보 삭제 후 전체회원 조회
ID:
PW:

'''

import member as mb

mems = mb.MemberResitory()

for i in range(3):
    mId = input('아이디 입력: ')
    mPw = input('비밀번호 입력: ')
    
    mem = mb.Member(mId, mPw)
    mems.addMember(mem)
    
mems.printMembers()

mems.loginMember('abc@gmail.com', '1234')
mems.loginMember('deg.gmail.com', '5678')
mems.loginMember('hig@gmail.com', '8900')

mems.removeMember('abc@gmail.com', '1234')

mems.printMembers()