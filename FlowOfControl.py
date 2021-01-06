import random
print(2<5)
print(3>7)
x=11
print(x>10)
print(2*x<x)
print(type(True))
print(bool(0))
y=bool(0)
print(type(y),y,sep="|")
#Simple if statements
# weight=float(input("How many pounds does your suitcase weight?"))
weight=56
if weight>50:
    print("There is a 25$ for luggades that heavy:")
print("Thank you for your business.")

#If-else Statements
# temp=float(input("What is the temperature?"))
temp=25
if temp>70:
    print("I think your should wear shorts.")
else:
    print('I think you should wear long pants.')
print("Get some exercise outside")
# #More Conditional Expressions
# def CalcWeeklyWages(totalHours,hourlyWage):
#     """Return the total weekly wages for a worker working totalHours with a given regular hourlywage, include overtime for hours over 40"""
#     if totalHours<=40:
#         totalwages=hourlyWage*totalHours
#     else:
#         overtime=totalHours-40
#         totalWages=hourlyWage*40+(1.5*hourlyWage)*overtime
#     return totalwages
# def Main():
#     # hours=float(input("Enter hours worked"))
#     # wage=float(input("Enter dollars paid per hour:"))
#     hours=40.0
#     wage=2.0
#     total=CalcWeeklyWages(hours,wage)
#     print(f"Wages for {hours} hours at ${round(wage,2)} per hour are ${round(total,2)}")
# # Main()
# from random import randint
# class headsTail:
#     def __init__(self):
#         """:arg"""
#     def flip(self):
#         guess = input("1 or 0:")
#         comp=randint(guess)
#         guess.capitalize()
#         if guess==comp:
#             print("Congrats!, You won....")
#         else:
#             print(f"Ooopps!, You failed... The outcome is {comp}")
# day=headsTail()
# day.flip()

def letterGrade(score):
    score=eval(input(""))
    if score>=80:
        letter="A"

