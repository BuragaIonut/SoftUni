numbers = list(map(int, input().split()))
bomb, power = list(map(int, input().split()))


while bomb in numbers:
    index = numbers.index(bomb)
    left_range = max(0, index - power)

    for i in range(left_range, index):
        numbers.pop(left_range)

    index = numbers.index(bomb)
    right_range = min(index + power, len(numbers)- 1)

    for i in range(index, right_range + 1):
        numbers.pop(index)

sum = 0
for i in numbers:
    sum += i
print(sum)
