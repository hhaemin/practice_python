'''
객체를 이용한 프로그래밍
TV 클래스를 다음과 같은 상속 구조로 만들고 객체를 생성해보자

NormalTv
    속성 : inch, color, resolution, smartTv, aiTv
    기능 : turnOn(), turnOff(), printTvInfo()
    
    Tv4K
        기능 : setSmartTv()
        
    Tv8K
        기능 : setSmartTv(), setAiTv()
'''

import smartTv as st

my4KTv = st.Tv4K('65', 'silver', '4k')
my4KTv.setSmartTv('on')
my4KTv.turnOn()
my4KTv.printTvInfo()
my4KTv.turnOff()