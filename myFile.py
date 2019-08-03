x = 15
y = 3
z = "this is a string"

print("x / y = ", x / y) 
print(z)

a = "hello"
b = "world"
c = "again"

mylist = [1, 2, 3, 4, 5]

for i in mylist:
    print (i)

def myPrint(words):     
    print(words, ", ok.")

def myFunction(vList):
    for i in vList:
        print(i)

def myRecursiveFunction(vList):
    if len(vList) > 0:
        print(vList.pop())
        myRecursiveFunction(vList)

while(x > 0):
        print(x)
        x = x - 1

myRecursiveFunction(["hello", 1, True, 3.1415])
