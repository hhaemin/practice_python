# students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
# print('students : {}'.format(students[2:4]))
# print('students : {}'.format(students[:4]))
# print('students : {}'.format(students[2:]))
# print('students : {}'.format(students[2:-2]))
# print('students : {}'.format(students[-5:-2]))

students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('students: {}'.format(students))
print('students: {}'.format(students[2:4]))
print('students: {}'.format(students[:4]))
print('students: {}'.format(students[2:]))
print('students: {}'.format(students[2:-2]))
print('students: {}'.format(students[-5:-2]))

print('students: {}'.format(students[slice(2, 4)]))
print('students: {}'.format(students[slice(4)]))
print('students: {}'.format(students[slice(2, len(students))]))
print('students: {}'.format(students[slice(2, len(students)-2)]))
print('students: {}'.format(students[slice(len(students)-5, len(students)-2)]))
