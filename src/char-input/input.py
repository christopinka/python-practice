import datetime
import age.age as forecast

name = input("Give me your name: ")
print(name)
age = input("Give me your age: ")
print(age)



print("{}, you will be a 100 years old in the year {}".format(name, forecast.age_forecast(age)))
