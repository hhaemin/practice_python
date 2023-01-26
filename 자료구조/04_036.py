scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
print(f'scores: {scores}')

minScore = 60
fStr = 'F(재시험)'
fDic = {}

for key in scores:
    if scores[key] < minScore:
        scores[key] = fStr
        fDic[key] = fStr

print(f'scores: {scores}')
print(f'fDic: {fDic}')
