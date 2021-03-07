class Vehicle:
    def __init__(self,type_of_veh,model,color,horses):
        self.type_of_veh = type_of_veh
        self.model = model
        self.color = color
        self.horses = horses
vehicles = []
while True:
    command = input()
    if command == 'End':
        break
    data = command.split()
    type_of_veh = data[0]
    model = data[1]
    color = data[2]
    horses = int(data[3])
    vehicle = Vehicle(type_of_veh,model,color,horses)
    vehicles.append(vehicle)


while True:
    command = input()
    if command == 'Close the Catalogue':
        break

    for vehicle in vehicles:
        if vehicle.model == command:
            if vehicle.type_of_veh == 'car':
                print(f'Type: Car')
            elif vehicle.type_of_veh == 'truck':
                print('Type: Truck')
            print(f'Model: {vehicle.model}')
            print(f'Color: {vehicle.color}')
            print(f'Horsepower: {vehicle.horses}')
cars_horses = []
trucks_horses = []
for vehicle in vehicles:
    if vehicle.type_of_veh == 'car' or vehicle.type_of_veh == 'Car':
        cars_horses.append(vehicle.horses)
    elif vehicle.type_of_veh == 'truck' or vehicle.type_of_veh == 'Truck':
        trucks_horses.append(vehicle.horses)
avg_cars = sum(cars_horses)/len(cars_horses)
avg_trucks = sum(trucks_horses)/len(trucks_horses)
print(f'Cars have average horsepower of: {avg_cars:.2f}.')
print(f'Trucks have average horsepower of: {avg_trucks:.2f}.')



