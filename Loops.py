x=3
y=x+2
y=2*y
x=y-x
print(x,y)
#The range Function
print(list(range(10)))
print(list(range(5,20,2)))
#Basic for Loops
for count in [1,2,3]:
    print(count)
    print("yes"*count)
myList=[1,2,3,4,5]
for x in myList:
    print("*"*x)
for x in range(10,1,-1):
    print("$"*x)

for color in ['red','blue','green']:
    print(color)
print("Done")
for i in range(10):
    print("Hello Friend!")
# n=eval(input("Enter the number of times to repeat:"))
n=5
for n in range(n):
    print("This is repetative")
for _ in range(10):
    print("Hello world!")

#Successive modification loops
colors=["red","blue","Orange","Green"]
number=0
for i in colors:
    number+=1
    print(number,i,sep=".")

def numberList(items):
    number=1
    for item in items:
        print(number,item,sep=".")
        number+=1

def main():
    numberList(["John","Jane","Day","Mary"])
    print()
    numberList(['green','red',"orange","yellow"])
main()
#Accumulation Loops
def sumList(nums):
    sum=0
    for num in nums:
        sum=sum+num
    print(sum)
def Main():
    nums=[2,6,3,8]
    sumList(nums)
    print()
    nums=[5,8,4,12]
    sumList(nums)
Main()

#Multiply
def multList(nums):
    mult=1
    for i in nums:
        mult=mult*i
    print(mult)
    pass
def Main():
    nums=[2,6,3,8]
    multList(nums)
Main()

#Divide
def multDivide(nums):
    div=1
    for i in nums:
        div=div/i
    print(div)
def Main():
    nums=[1000,5,2,4]
    multDivide(nums)
Main()

#Substraction
def subList(nums):
    sub=0
    for n in nums:
        sub=n-sub
    print(sub)
def Main():
    nums=[1000,500,100,50]
    subList(nums)
Main()

#Trial Sums
def sumList(nums):
    sum=0
    for i in nums:
        sum=sum+i
    return sum
print(sumList([2,4,5,6]))
#Exercise
def JoinStrings(stringList):
    s=''
    for name in stringList:
        s=s+name+" "
    print(s,end=".\n")
def Main():
    JoinStrings(["My","Name","Is","David"])
Main()



#More Playing Computer
def listOnOneLine(items):
    for item in items:
        print(item,end=" ")
listOnOneLine(['apple','banana','pear'])
