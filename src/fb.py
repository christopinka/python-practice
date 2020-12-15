# Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

def fizz_buzz():
    fizz_buzzes = {}
    for i in range(1, 51):
        fizz_buzzes.update({i: i})
        if i % 3 == 0:
            fizz_buzzes.update({i: "Fizz"})
        if i % 5 == 0:
            fizz_buzzes.update({i: "Buzz"})
        if i % 5 == 0 and i % 3 == 0:
            fizz_buzzes.update({i: "FizzBuzz"})

    print(fizz_buzzes)
    return fizz_buzzes


print(fizz_buzz().values())
