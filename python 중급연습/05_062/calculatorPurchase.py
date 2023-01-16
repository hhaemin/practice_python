g1Price = 1200; g2Price = 1000; g3Price = 800
g4Price = 2000; g5Price = 900

def formatedNumber(n):
    return format(n, ',')

def calculator(*gcs):
    
    gcsDic = {}
    againCntInput = {}
    
    for idx, gc in enumerate(gcs):
        try:
            gcsDic[f'g{idx+1}'] = int(gc)
        except Exception as e:
            againCntInput[f'g{idx+1}'] = gc
            print(e)
            
    totalPrice = 0
    for g in gcsDic.keys():
        totalPrice +=  globals()[f'{g}Price'] * gcsDic[g]          #가격 * 개수
        
    print('------------------------------------------')
    print(f'총 구매 금액 : {formatedNumber(totalPrice)}원')
    print('------------미결제 항목----------------')
    for g in againCntInput.keys():
        print(f'상품: {g}, \t 구매 개수: {againCntInput[g]}')
    print('------------------------------------------')