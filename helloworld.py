myText = "Hello, world!"
print(myText)
#Data types
myNumber = 30
myNumberAsAString = "29"
print(myNumber*2)
print(myNumberAsAString*2)
myFloat = 29.20
myBool = True
print(True - True)
#Conditionals
print(myNumber == 28)
print(myNumber <= 28)
print(not myNumber != 28)

if myNumber <= 28:
    print("You are still young")
elif myNumber > 40:
    print("You are old")
else:
    print("What are you?")
#Loops
myArray = ["apple", "banana", "cherry"]
print(myArray[0])

for x in myArray:
    print(x)

# for x in myText:
#     print(x)

for x in myArray:
    if x[0] == "a":
        print(x)
    else:
        print("Bad fruit")

#functions
def my_function():
    print("Hello from a function")

for x in range(6):
    my_function()

def sum(x,y):
    print(x+y)

for x in range(6):
    sum(5,x)