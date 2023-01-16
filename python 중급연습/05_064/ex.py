'''
은행 계좌 개설 및 입/출금 프로그램
'''

import bank

KoreaBank = bank.Bank()

new_account_name = input('통장 개설을 위한 예금주 입력: ')
myAccount = bank.PrivateBank(KoreaBank, new_account_name)
myAccount.printBankInfo()

while True:
    
    selectNumber = int(input('1.입금, \t 2.송금, \t 3.종료'))
    if selectNumber == 1:
        m = int(input('입금액 입력: '))
        KoreaBank.doDeposit(myAccount.account_no, m)
        myAccount.printBankInfo()
        
    elif selectNumber ==2:
        m = int(input('총금액 입력: '))
        try:
            KoreaBank.doWithdraw(myAccount.account_no, m)
            
        except bank.LackException as e:
            print(e)
            
        finally:
            myAccount.printBankInfo()
            
    elif selectNumber == 3:
        print('Bye~')
        break
    
    else:
        print('잘못 입력했습니다. 다시 입력해주세요!')