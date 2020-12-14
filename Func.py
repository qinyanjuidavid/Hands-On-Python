def happyBirthdayEmily():
    """:arg
    When writing a python function we use def- define
    """
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday to you dear Emily!")
    print("Happy Birthday to you.")
happyBirthdayEmily()
happyBirthdayEmily()
happyBirthdayEmily()
#Multiple Function defination

def happyBirthdayJane():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday to you dear Jane!")
    print("Happy Birthday to you.")
def happyBirthdayJohn():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday to you dear John!")
    print("Happy Birthday to you.")
happyBirthdayJane()
happyBirthdayJohn()
#Trial
def myFunc1():
    print("My name is day Qinyanjui")
def myFunc2():
    myFunc1()
    print("I love coding")
myFunc2()

#Functs can also call other functions
def happyBirthdayEmily():
    print("Happy Birthday Emily.")
def happyBirthdayAndrea():
    print("Happy Birthday Andrea")
def Main():
    happyBirthdayAndrea()
    happyBirthdayEmily()
Main()
def f():
    print("In function f")
    print("When does this print.")
f()
print("+++"*30)
def f():
    print("In function f.")
print("When does this print?")
f()
print("It has already been printed.",end="\n\n")
#TestyourMind
def mySong():
    print("Twinkle twinkle little stars")
    print("How i wonder how you are!")
    print("You fly in the sky....")
mySong()
mySong()
mySong()
print("==="*30)
#Function Parameters
def happyBirthday(person):
    """:arg Func- with arguments/parameters"""
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday dear {}".format(person),end=".\n")
    print("Happy Birthday to you.")
happyBirthday("Jane")
happyBirthday("John")
#In function parameters you can call the func in another function
def newHappyBirthday(person):
    """:arg Func- with arguments/parameters"""
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday dear {}".format(person), end=".\n")
    print("Happy Birthday to you.")
def Main():
    pass
    # while True:
    #     name=input("Enter the name:")
    #     newHappyBirthday("Carl")
Main()

def anotherHappyBirthday(person):
    """:arg Func- with arguments/parameters"""
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday dear {}".format(person), end=".\n")
    print("Happy Birthday to you.")
def Main():
    # username=input("Enter the name of the persons birthday:")
    anotherHappyBirthday("Jane")
Main()
#Multiple Function Parameters
def sumProblem(x,y):
    sum=x+y
    sen="The sum of {0} and {1} is {2}".format(x,y,sum)
    print(sen)
def Main():
    sumProblem(2,3)
    sumProblem(1234,5678)
    # a=eval(input("Enter an integer:"))
    # b=eval(input("Enter another integer:"))
    sumProblem(7,6)
Main()

#Returned Function Values
def f(x):
    return x*x
print(f(3))
print(f(4))
print(f(4)+f(3))

def sumProblem(x,y):
    sum=x+y
    return sum
print(sumProblem(5,10))
print(sumProblem(11,12))

def myFunc(name,age,school):
    sen="My name is {}, i am {} years old. I school in {} university".format(name,age,school)
    return sen
# name=input("Enter your name:")
# age=input("Enter your age:")
# school=input("Enter your school:")
name="John"
age="19"
school="MIT"
print(myFunc(name,age,school))

def lastFirst(firstName,lastName):
    separator=" , "
    result=lastName+separator+firstName
    return result
print(lastFirst("John","Doe"))
print(lastFirst("Jane","Doe"))

def sumProblemString(x,y):
    sum=x+y
    return 'The sum of {} and {} is {}'.format(x,y,sum)
def main():
    print(sumProblemString(2,3))
    print(sumProblemString(56,75))
    # x=eval(input("Enter the first integer:"))
    # y=int(input("Enter the second integer:"))
    x=23
    y=59
    print(sumProblemString(x,y))
main()

def newFunc(interviewer,applicant,time):
    return '{} will be interviewed by {} at {}'.format(applicant,interviewer,time)
def Main():
    # interviewer=input("Enter the name of the interviewer:")
    # applicant=input("Enter the name of the applicant:")
    # time=input("Enter the appointment time:")
    interviewer="John"
    applicant="Day"
    time="2.30"
    print(newFunc(interviewer,applicant,time))
Main()
#Reminder
def TestYourMight(width,height):
    area=width*height
    return "The area of a rectangle whose width is {} and height {} is {}".format(width,height,area)
def Main():
    print(TestYourMight(20,23))
    print(TestYourMight(5,7))
Main()

#Local Variablea
def Main():
    x=3
    f(x)
def f(x):
    print(x)
Main()
#global variables
pi=3.14
def circleArea(radius):
    return pi*radius*radius
def circlecumference(radius):
    return pi*radius*2
def Main():
    print("The area of the circle with radius 5 is",circleArea(5))
    print("The circumference with radius 5 is:",circlecumference(5))
Main()

