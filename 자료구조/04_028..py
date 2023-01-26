studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
sum = 0
avg = 0
for classNo, cnt in studentCnts:
    print('{}학급 학생수: {}명'.format(classNo, cnt))
    sum += cnt

print('전체 학생 수: {}명'.format(sum))
print('평균 학생 수: {}명'.format(sum / len(studentCnts)))