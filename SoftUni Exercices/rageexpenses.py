lost_games = int(input())
headset_price = float(input())
mouse_price = float(input())
keyboard_price = float(input())
display_price = float(input())
expanses = 0
for i in range (1, lost_games + 1):
    if i % 2 == 0:
        expanses += headset_price
    if i % 3 == 0:
        expanses += mouse_price
    if i % 6 == 0:
        expanses += keyboard_price
    if i % 12 == 0:
        expanses += display_price
print(f'Rage expenses: {expanses:.2f}$.')