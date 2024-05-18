#Find max and min through Ternary Operator given two number
print('Find max and min through Ternary Operator given two number')
a=float(input("Enter Number 1:"))
b=float(input("Enter Number 2:"))
min =a if a <b else b
print("Minimun Value:",min)
max =a if a > b else b
print("Maximum Value:",max)

#Find max and min through Ternary Operator given three number
print('Find max and min through Ternary Operator given three number')
a=float(input("Enter Number 1:"))
b=float(input("Enter Number 2:"))
c=float(input("Enter Number 3:"))
min = a if (a < b and a < c) else (b if b < c else c)
print("Minimun Value:",min)
max = a if (a > b and a > c) else (b if b > c else c)
print("Maximum Value:",max)

