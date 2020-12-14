#Dictionaries are simply a collection of words matched with their definations.
#Dict are usually made up of key and values
spanish=dict()
spanish['hello']='hola'
spanish['yes']='si'
print(spanish,type(spanish),sep="|")

#Trial two
name=dict()
name['David']=23
name["Jane"]=32
name['John']=42
print(name,type(name),sep="|")
print(name["John"])

def createDictionary():
    spanish=dict()
    spanish['hello']='hola'
    spanish['yes']='si'
    return spanish
def Main():
    dictionary=createDictionary()
    print(dictionary["hello"])
Main()

#trial
def createNameDict():
    coders=dict()
    coders["David"]="Python"
    coders["John"]="Java"
    coders["Jane"]="C"
    return coders
def Main():
    details=createNameDict()
    print(details["John"],type(details),sep="|")
Main()
