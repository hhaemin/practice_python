'''
1부터 1000까지의 소수인 난수 10개를 생성하되,
소수가 아니면 사용자 예외가 발생하도록 프로그램 생성
'''

import random
import prime_module as pm

primeNumbers = []

n =0
while n < 10:
    
    rn = random.randint(2,1000)
    if rn not in primeNumbers:
        try:
            pm.isPrime(rn)
        except pm.NotPrimeException as e:
            print(e)
            continue
        
        except pm.PrimeException as e:
            print(e)
            primeNumbers.append(rn)
        
    else:
        print(f'{rn} is overlap number.')
        continue
    
    n += 1 

print(f'primeNumbers: {primeNumbers}')