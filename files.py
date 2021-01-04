import json
outfile=open("sample.txt",'w')
outfile.write("This is my first output\n")
outfile.write("This is my first line in the output.")
outfile.close()

# myFile=open("coders.txt","w")
# nameList=[]
# langList2=[]
# for i in range(2):
#     name=input("Enter the name of the coder:")
#     lang=input("Enter the programming language:")
#     myDict={name:lang}
#     nameList.append(myDict)
# myFile.write(f"{nameList}")
#
# class Files:
#     def __init__(self):
#         """:arg
#         """
#     def WriteFile(self):
#         myFile=open('coderPass.html','w')
#         codersList=[]
#         for i in range(2):
#             name=input("Enter the name of the coder:")
#             age=eval(input("Enter the age:"))
#             salary=input("Enter the salary:")
#             language=input("Enter the coder's programming language:")
#             print()
#             codersDetails={"name":f"{name}",'age':age,"Salary":salary,"Programming Language":language}
#             codersList.append(codersDetails)
#         myFile.write(f"{codersList}")
#         myFile.close()
# day=Files()
# day.WriteFile()

x='{"name":"Day","Age":10}'
y=json.loads(x)
print(y)
print(y['name'])

outFile=open("samplePyFile.py",'w')
outFile.write("""#This Script was generated from the files.py script
import json
x='{"name":"Day","Age":10}'
y=json.loads(x)
print(y)
print(y['name'])
""")
outFile.close()

#Reading Files
inFile=open("sample3.txt",'w')
inFile.write("This File is meant to be read.")
inFile.write("\nI think i can add some stuff that will be displayed on my terminal window")
inFile.close()
inFile=open("sample3.txt",'r')
content=inFile.read()
print(content)

class FileIO:
    def __init__(self):
        """:arg"""
    def myFunc(self):
        myFile=open("JustDoit.txt",'w')
        myList=[]
        for i in range(2):
            name=input("Enter the name of the student:")
            age=input("Enter the age of the student:")
            print()
            Dict={f"Name:{name},Age:{age}"}
            myList.append(f"{Dict}")
        myFile.write(f"{myList}")
        myFile.close()
        readFile=open("JustDoit.txt",'r')
        content=readFile.read()
        print(content)
day=FileIO()
day.myFunc()



