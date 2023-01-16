def add(n1, n2):
    print('덧셈 연산')
    
    try:
        n1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return
    
    try:
        n2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return
    
    print(f'{n1} + {n2} = {n1 + n2}')