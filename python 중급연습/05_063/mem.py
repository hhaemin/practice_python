class EmptyDataException(Exception):
    
    def __init__(self, i):
        super().__init__(f'{i} is empty!')

def checkInputData(n, m, p, a, ph):
    
    if n == '':
        raise EmptyDataException('name')
    elif m == '':
        raise EmptyDataException('mail')
    elif p == '':
        raise EmptyDataException('password')
    elif a == '':
        raise EmptyDataException('address')
    elif ph == '':
        raise EmptyDataException('phone')
    
class RegistMember():
    
    def __init__(self, n, m, p, a, ph):
        self.m_name = n
        self.m_mail = m
        self.m_pw = p
        self.m_addr = a
        self.m_phone = ph
        print('Membership complete!!')
        
    def printMemberInfo(self):
        print(f'm_name: {self.m_name}')
        print(f'm_mail: {self.m_mail}')
        print(f'm_pw: {self.m_pw}')
        print(f'm_addr: {self.m_addr}')
        print(f'm_phone: {self.m_phone}')
        