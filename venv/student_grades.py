n = int(input())
student_grades = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in student_grades:
        student_grades[name] = []

    student_grades[name].append(grade)

average_grades = {}

for s in student_grades:
    sum = 0
    grades = student_grades[s]
    for grade in grades:
        sum += grade

    average = sum/len(grades)

    if average >= 4.5:
        average_grades[s] = average

sorted_average_grade = sorted(average_grades.items(), key=lambda kvp: average_grades[kvp[0]],
                              reverse=True)
for s in sorted_average_grade:
    print(f'{s[0]} -> {s[1]:.2f}')