print('Hello World')
print("Hello Friend")
print(type("John Doe"))
print(type("7"))
print(type(7))

#String Concatenation
print("Very "+"Hot")
print(3*"Hello "+"World")
print('7'+"2")
print(7+2)
print(type(int('7')+2))
print(5*"yes")
print(5*"Maybe"+5*"Yes")
#Variable and Assignment
width=10
height=12
area=width*height
print(area)
a=6
a=a+5
first="John"
last="Doe"
name=first+ ' '+ last
print(name)
fred ="Fredrick"
first=fred
print(first)
#Literals and Identifiers
#Literals are like 27 and "hello" since their meaning is literally
#Identifiers are defined in Python
priceAtOpening="This is a good way of declaring varibles"
print(priceAtOpening)
priceatopening="This is a poor method of declaring variables"
print(priceatopening)
price_at_opening="This is also another better method of declaring varibles"
print(price_at_opening)
#The Print Function
x=3
y=5
print("The sum of",x,'plus',y,'is',x+y)
#Strings Part II
sillyTest="""Say,
"I'm in!"
This is line 3.
"""
print(sillyTest)
#Escape Codes
print("Mr\\Mrs John")#Backslash
print("This is line one.\nThis is line two.\nThis is line three.")
print("I\'m in!")
print('a\nb\nc\n')
print('Hello Friend')
""":arg This is a multilined
comment"""
#This is a comment

#Input and output Function
# person=input("Enter your name:")
# # print("Hello",person)
# applicant=input("Enter the applicant's name:")
# interviewer=input("Enter the interviewers name:")
# time=input("Enter the appointment time:")
# print(interviewer,"will interview",applicant,'at',time,'.')
# person=input("Enter your name:")
# print("Hello", person,"!")
#Parameter sep
# person=input("Enter your name:")
# print("Hello",person,"!",sep='')
firstName="Day"
lastName="Qinyanjui"
age="23"
print("My name is",firstName,lastName,"I am",age,"years old.",sep="/")
#Parameter end
print("This is line one",end=".\n")


#Numbers and strings of digits
# x=eval(input("Enter the first number:"))
# y=int(input("Enter the second number:"))
# sum=x+y
# print(f"The sum of {x} and {y} is {sum}")

#Another approach for inputing the numbers
# xString=input("Enter the first number:")
# xString=int(xString)
# print(xString,type(xString),sep="|")
# num1=eval(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# num3=eval(input("Enter the third number:"))
# sum=num1+num2+num3
# print(f"The sum of {num1}, {num2} and {num3} is {sum}",end=".\n")

#Syring Format Operation
# person=input("Enter your name:")
# greeting="Hello, {}!".format(person)
# print(greeting)
# person=input("Enter your name:")
# age=eval(input("Enter your age:"))
# school=input("Enter your current school:")
# summary="My name is {}, I am {} years old. My current school is {}".format(person,age,school)
# print(summary,end=".\n")

# applicant=input("Enter the applicant's name:")
# interviewer=input("Enter the interviewer's name:")
# time=input("Enter the appointment time:")
# print("{} will interview {} at {}".format(interviewer,applicant,time))
#Including the braces in the .format()
a=5
b=9
setStr="The set is {{{},{}}}".format(a,b)
print(setStr,end=".\n")

firstName="John"
lastName="Doe"
age=23
school="MIT"
print("My name is {3} {2}, I am {1} years old and i school at {0}".format(school,age,lastName,firstName),end=".\n")

interviewer="CoderPass"
applicant="John Doe"
appointment="2.00 PM"
print("{2} will be interviewed by {1} at {0}".format(appointment,interviewer,applicant),end=".\n")

def Graduate():
    # credits=float(input("How many units of credit do you have?"))
    # GPA=float(input("What is your GPA?"))
    credits=126
    GPA=2.5
    if credits>=120 and GPA>=2.0:
        print("You are eligible to graduate!")
    else:
        print("You are not eligible to graduate.")
Graduate()

