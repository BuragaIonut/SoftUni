import  math
money = float(input())
stud_count = int(input())
sabre_price = float(input())
robe_price = float(input())
belt_price = float(input())


robe_cost = stud_count * robe_price
sabre = math.ceil(stud_count + (10/100) * stud_count)
sabre_cost =sabre * sabre_price
belt_cost = 0
for i in range(1, stud_count + 1):
    if i % 6 == 0:
        belt_cost += 0
    else:
        belt_cost += belt_price
total_cost = sabre_cost + belt_cost + robe_cost
if total_cost < money:
    print(f'The money is enough - it would cost {total_cost:.2f}$.')
else:
    money_needed = total_cost - money
    print(f'The master will need {money_needed:.2f}$ more.')