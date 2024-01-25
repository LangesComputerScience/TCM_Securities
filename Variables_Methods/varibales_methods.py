#Programmer: Mr. Lange
#Program: Varibles & Methods
#Date: 1.11.2024

quote = "All is fair in love and war!"
print(quote)
print(quote.upper()) #Uppercase Method
print(quote.lower()) #Lowercase Method
print(quote.title()) #Titlecase Method
print(len(quote)) #Counts Characters

name = "Mr. Lange" #string
age = 25 #int
gpa = 3.7 #float

print(age)
print(int(gpa)) #cast a float into an int

print("\nMy name is " + name + " and I am " + str(age) + " with a GPA of " + str(gpa) + ".") #Concatenate variables while Casting Int to Str

print("\nMy name is",name,"and I am",age,"with a GPA of", str(gpa) + ".") #Concating using a Comma instead of a + while casting our gpa variable into a string to account for the spacing before the period

print("")

age += 1 #adds one to the variable age
print(age)

print("")

age += 10 #adds ten to the variable age
print(age)

print("")

birthday = 1
age += birthday #We can add two variables with the values as Int together
print(age)
