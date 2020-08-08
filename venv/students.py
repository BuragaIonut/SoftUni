class Student:
    def __init__(self,first_name,second_name,grade):
        self.first_name = first_name
        self.second_name = second_name
        self.grade = grade


students = []
n = int(input())

for i in range(n):
    data = input().split()
    first_name = data[0]
    second_name = data[1]
    grade = float(data[2])
    student = Student(first_name, second_name,grade)
    students.append(student)

for student in students:
    if student.grade >= 3:
        print(f'{student.first_name} {student.second_name}: PASS')
    else:
        print(f'{student.first_name} {student.second_name}')


