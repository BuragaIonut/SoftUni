class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


people = []

n = int(input())

for i in range(n):
    data = input().split()
    name = data[0]
    age = int(data[1])
    if age > 30:
        p = Person(name, age)
        people.append(p)
for person in people:
    print(f'{person.name} - {person.age}')