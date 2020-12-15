def divisible(dividend, divisor):
    if dividend % divisor == 0:
        return True
    else:
        return False


for i in range(1, 101):
    if i % 2 == 0:
        print("{} is even".format(i))

    if i % 4 == 0:
        print("{} is divisible by 4".format(i))

    if divisible(i, 3):
        print("{} is a factor of 3".format(i))
