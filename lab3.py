#string data type
myString ="This is a string"
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))


#Concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


#working with inputs
name = input("What is your name? ")
print(name)


#formatting output strings
color = input("What is your favourite color ")
animal = input("What is you favourite animal ")
print("{}, you like a {} {}!".format(name,color,animal))