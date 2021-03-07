
students = []
second_grades = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    student = []
    student.append(name)
    student.append(score)
    students.append(student)
my_min = float('Inf')
for student in students:
    if student[1] <= my_min:
        my_min = student[1]
for student in students:
    if student[1] == my_min:
        students.remove(student)
my_min = float('Inf')
for student in students:
    if student[1] <= my_min:
        my_min = student[1]
for student in students:
    if student[1] == my_min:
        second_grades.append(student[0])
second_grades.sort()
for el in second_grades:
    print(el)
# print(students)
