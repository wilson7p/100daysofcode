#Use the random module to generate random numbers and select random elements from a list.
print("\nWilson - Day 39 of #100DaysOfCode\n")
print("\nUse the random module to generate random numbers and select random elements from a list.")

import random

list = [1,2,3,4,5]
random_number = random.choice(list)
print(f"random number from {list} is {random_number}")

#Use the datetime module to work with dates and times.
print("\nUse the datetime module to work with dates and times.")

from datetime import datetime, date, time, timedelta

current_date = date.today()
print("current date is: ",current_date)

current_time = datetime.now().time()
print("current time is: ",current_time)

current_datetime = datetime.now()
print("current date and time is: ",current_datetime)
