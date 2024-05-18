# Conditional Statements
'''1) if
 if condition : statement
 OR
 if condition :
 statement-1
 statement-2
 statement-3
If condition is true then statements will be executed.'''

name=input("Enter Name:")
if name == 'SHAMAR':
    print("Hello",name, "Good Morning")
print("How are you?", name,'!')



name1=input("Enter Name:")
if name1 == "PROTIVA":
    print("Hello",name1, "Good Morning")
else:
    print("How are you?", name1,'!')

#if-elif-else

city=input("Enter Your Favourite City:")
if city=="DHAKA":
  print("It is",city,"City")
elif city=="RAJSHAI":
   print("It is", city, "City")
elif city=="SHYLET":
   print("It is", city, "City")
else:
     print('This is not your Favourite City')

#find Biggest of given 2 Numbers from the Commad Prompt
print('find Biggest of given 2 Numbers from the Commad Prompt')
n1=float(input("Enter First Number:"))
n2=float(input("Enter Second Number:"))
if n1>n2:
  print("Biggest Number is:",n1)
else:
  print("Biggest Number is:",n2)

#  find Biggest of given 3 Numbers from the
#  Commad Prompt
print('find Biggest of given 3 Numbers')
n1=float(input("Enter First Number:"))
n2=float(input("Enter Second Number:"))
n3=float(input("Enter Thrid Number:"))
if n1>n2 and n1>n3:
  print("Biggest Number is:",n1)
elif n2>n3:
    print("Biggest Number is:", n2)
else:
  print("Biggest Number is:",n3)

#Check whether the given Number is in between 1 and 100?

print('Check whether the given Number is in between 1 and 100?')
n=float(input("Enter Number:"))
if n>=1 and n<=100:
    print("The number",n,"is in between 1 to 100")
else:
    print("The number", n, "is not in between 1 to 100")

