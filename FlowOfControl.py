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

def StudentsGrade():
    # marks=eval(input("Enter the students marks:"))
    marks=86
    if marks>=80 and marks<=100:
        print("The student scored an A.")
    elif marks>=75:
        print("The student scored an A-")
    elif marks>=70:
        print("The student scored a B+.")
    elif marks>=65:
        print("The student scored a B.")
    elif marks>=54:
        print("The student scored a B-.")
    elif marks>=49:
        print("The student scored a C+.")
    elif marks>=44:
        print("The student scored a C.")
    elif marks>=39:
        print("The student scored a D+.")
    elif marks>=34:
        print("The student scored a D.")
    elif marks>=24:
        print('The student scored a D-.')
    elif marks<=23 and marks>=0:
        print("The student failed.")
    else:
        print("Please check the students score and enter again!!!")
StudentsGrade()
# Nested loops
def PrintAllPositive(numberList):
    """:arg """
    for num in numberList:
        if num>0:
            print("Positive numbers",num)
PrintAllPositive([3,-6,8,92,56,12,])

def PrintEvenNumbers(nums):
    """:arg"""
    for num in nums:
        if num%2==0:
            print(num)
PrintEvenNumbers([3,5,6,9,8,5,1,7,10,18])

def ChooseEven():
    """
    :param num:
    :return:
    """
    myList=[]
    for i in range(3):
        num=eval(input("Enter the the numbers:"))
        myList.append(num)
    newList=[]
    for num in myList:
        if num%2==0:
            newList.append(num)
    print(newList)
ChooseEven()




