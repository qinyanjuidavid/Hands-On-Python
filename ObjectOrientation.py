s="Hello"
print(s.upper())
s="HELLO FRIEND"
print(s.lower())
x="this is a title"
print(x.title())
tale="This is the best of times,"
print(tale.count('i'))
print(tale.find('m'))
print(tale.index('f'))
print(3*'X'.count('XXX'))
print((3*'X').count('XXX'))
#string Indices
y='computer'
print(y[5])
print(y[2:])
print(y[2:5])
print(y[:6])
print(y[-1])
print(y[-2])
print(y[0])
print(len(y))
print(y.capitalize())
values=[5,7,9,22,6,8]
print(values)
print(values[1])
print(values[1:4])

s="word"
print("The full string is:",s)
n=len(s)
for i in range(n):
    print()
    print("i=",i)
    print('The letter is:',s[i])

#trial
name="MegaPython"
n=len(name)
for i in range(n):
    print(i,name[i],sep=": ")
#Split Function
tales='This is the best if times.'
print(tale.split())#In this case split use the whitespace in between words to split the tales object
place="Mississippi"
print(place.split('i')) #In this case i is been used to split the place object
print(place.split())

line="Go: tear some strings apart!"
seq=line.split()
print(seq)
print(line.split(":"))
print(line.split("ar"))
newLine="This includes\\nsome new\\nlines."
print(newLine)
print(newLine.split())
line="This is line one. \nThis is line two. \nThis is line three."
print(line)
print(line.split())

#Join Function
#Join is roughly the reverse of split
line="Get: Tear some strings apart!"
seq=line.split()
print(seq)
print(''.join(seq))
num="789"
print('+254'.join(num))
name="Spartacus is not my name"
newName='$'.join(name)
print(newName)
print(newName.split("$"))
num=':'.join(['one','two','three'])
print(num)
num=['one','two','three','four']
n=len(num)
for i in range(n):
    print(i,num[i],sep=":")

#Exercise
x='the best one'
y=x.split()
y='_'.join(y)
print(y)

# while True:
# acro=input('Enter the string to get the acronym:')
acro="The best one"
acro=acro.split()
n=len(acro)
letter=[]
for i in range(n):
    l=acro[i][0].upper()
    letter.append(l)
n=''.join(letter)
print(n)

#Appending to a list
words=list()
print(words)
words.append('animal')
print(words)
words.append("food")
print(words)
words.append('city')
print(words)

#Trial
# count=0
# while count<10:
#     word=[]
#     for i in range(10):
#         name=input("Enter a word:")
#         word.append(name)
#     print(word)

def multiplyAll(numList,multiplier):
    newList=list()
    for num in numList:
        newList.append(num*multiplier)
    return newList
print(multiplyAll([3,1,7],5))

def divideAll(numList,dividor):
    result=[]
    for i in numList:
        result.append(i/dividor)
    return result
print(divideAll([100,50,25],5))
print(divideAll([80],5))

def addAll(numList,numToBeAdded):
    sum=[]
    for n in numList:
        sum.append(n+numToBeAdded)
    return sum
print(addAll([85],5))

def subAll(numList,numToBeSub):
    result=[]
    for p in numList:
        result.append(p-numToBeSub)
    return result
print(subAll([80],70))



















