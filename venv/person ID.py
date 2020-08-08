class Person:
    def __init__(self, name, ID, age):
        self.name = name
        self.ID = ID
        self.age = age

persons = []
while True:
    data = input()
    if data == 'End':
        break
    command = data.split()
    name = command[0]
    ID = command[1]
    age = int(command[2])
    person = Person(name, ID, age)
    persons.append(person)
