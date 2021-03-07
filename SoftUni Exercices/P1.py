import math

students = int(input())
lectures = int(input())
bonus = int(input())
bonuses = []
atendances = []

for i in range(students):
    atendace = int(input())
    atendances.append(atendace)
    total_bonus = atendace / lectures * (5 + bonus)
    bonuses.append(math.ceil(total_bonus))
print(f'Max Bonus: {max(bonuses)}.')
max_index = bonuses.index(max(bonuses))
print(f'The student has attended {max(atendances)} lectures.')
# print(bonuses)
# print(atendances)
