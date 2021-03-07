n = int(input())

heroes = {}
for _ in range(n):
    line = input().split()
    hero_name = line[0]
    hp = int(line[1])
    mp = int(line[2])
    heroes[hero_name] = [hp,mp]

while True:
    command = input().split(' - ')
    action = command[0]
    if action == 'End':
        break
    elif action == 'CastSpell':
        hero = command[1]
        mp_needed = command[2]
        spell = command[3]
        if hero in heroes:
            stats = heroes[hero]
            current_mp = int(stats[1])
            current_hp = int(stats[0])
            mp_needed = int(mp_needed)
            if current_mp > mp_needed:
                current_mp = current_mp - mp_needed
                heroes[hero] = [current_hp,current_mp]
                print(f'{hero} has successfully cast {spell} and now has {current_mp} MP!')
            else:
                print(f'{hero} does not have enough MP to cast {spell}!')
    elif action == 'TakeDamage':
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]
        if hero in heroes:
            stats = heroes[hero]
            current_hp = int(stats[0])
            current_mp = int(stats[1])
            if damage < current_hp:
                current_hp = current_hp - damage
                if current_hp > 0:
                    heroes[hero] = [current_hp,current_mp]
                    print(f'{hero} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!')
            else:
                del heroes[hero]
                print(f'{hero} has been killed by {attacker}!')
    elif action == 'Recharge':
        hero = command[1]
        amount = int(command[2])
        if hero in heroes:
            stats = heroes[hero]
            current_mp = int(stats[1])
            current_hp = int(stats[0])
            mana_needed = 200 - current_mp
            current_mp += amount
            if current_mp > 200:
                current_mp = 200
                heroes[hero] = [current_hp,current_mp]
                print(f'{hero} recharged for {mana_needed} MP!')
            else:
                heroes[hero] = [current_hp, current_mp]
                print(f'{hero} recharged for {amount} MP!')
    elif action == 'Heal':
        hero = command[1]
        amount = int(command[2])
        if hero in heroes:
            stats = heroes[hero]
            current_hp = int(stats[0])
            current_mp = int(stats[1])
            hp_needed = 100 - current_hp
            current_hp += amount
            if current_hp > 100:
                current_hp = 100
                heroes[hero] = [current_hp,current_mp]
                print(f'{hero} healed for {hp_needed} HP!')
            else:
                heroes[hero] = [current_hp, current_mp]
                print(f'{hero} healed for {amount} HP!')

heroes = dict(sorted(heroes.items(), key=lambda x: (-(x[1][0]), x[0])))
print(heroes)

for key, value in heroes.items():
    print(key)
    print(f'HP: {value[0]}')
    print(f'MP: {value[1]}')