#Age Calculator Part 1

#Chris Edosomwan Freshman year CS 

#April 29, 2022

import datetime

Name = input("What is your name?")

print("Hey! Nice to meet you",Name)

birth_year = int(input("Enter year you were born.."))
birth_month = int(input("Enter your number of birthmonth.."))
birth_day = int(input("enter the day you were born"))

current_year = datetime.date.today().year

current_month = datetime.date.today().month

current_day = datetime.date.today().day

age_year = current_year - birth_year

age_month = current_month + birth_month

age_day = current_day - birth_day


print("your exact age ", age_year, "Years", age_month, 'months', age_day, "days")









    