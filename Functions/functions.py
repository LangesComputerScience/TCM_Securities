#Programmer: Mr. Lange
#Program: Functions
#Date: 1.19.2024

def nl(): #New Line Function
	print('\n')

def who_am_i(): #this is a functions w/out parameters 
 	name = "Mr. Lange" #local variable
 	age = 67
 	print("My name is",name,"and I am",age,"years old.")

who_am_i()

nl()

def addOneHundred(num): #num is a Parameter
	print(num + 100)
	
addOneHundred(1500) #1500 is the Argument which inserts itself into the Parameter

nl()

addOneHundred(0)

nl()

def add(x,y):
	print(x + y)
	
add(8,5)

nl()
