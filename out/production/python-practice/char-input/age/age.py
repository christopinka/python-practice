import datetime


def age_forecast(age, age_in=100):
    now = datetime.datetime.now()
    return int(now.year) + (age_in - int(age))