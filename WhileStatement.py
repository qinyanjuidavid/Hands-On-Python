temperature=115
while temperature>112:
    print(temperature)
    temperature-=1
print("The tea is cool")

count=0
while count<=10:
    print(count)
    count+=1
print("End...")
#Just a btw
for i in range(10):
    for y in range(i):
        print("*",end=" ")
    print()
#Triangle pattern
i=0
while i<10:
    y=0
    while y<i:
        print("*",end=" ")
        y+=1
    print()
    i+=1
#II Triangle
a=10
while a>0:
    b=10
    while b>a:
        print("*",end=" ")
        b-=1
    print()
    a-=1

#Range Function
myList=list(range(4,10,2))
print(myList,type(myList),sep="|")





