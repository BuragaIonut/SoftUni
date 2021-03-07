# You will be given a count of wagons in a train n.
# On the next n lines you will receive how many people are going to get on that wagon.
# At the end print the whole train and after that the sum of the people in the train.

n = int(input())

train = [0] * n

for i in range(len(train)):
    train[i] = int(input())

for i in train:
    print(i, end=" ")
print()
print(sum(train))
