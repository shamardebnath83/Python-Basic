#Using a For Loop
list= eval(input('Enter List For Loop:'))
sum_list=0
for x in list:
    sum_list=sum_list+x
print('The Sum for Loop=',sum_list)

#Using Numpy for Larger Arrays

import numpy as np

list1= eval(input('Enter List for numpy:'))
numbers = np.array(list1)
total = np.sum(numbers)
print('The Sum for np=',total)

#Using reduce from functools

from functools import reduce

list3= eval(input('Enter List for reduce:'))
total= reduce(lambda x,y: x+y,list3 )
print('The Sum for reduce=',total)

'''Step-by-Step Execution

For numbers = [1, 2, 3, 4, 5]:

    Initial Elements:
    1 and 2 are passed to the lambda function: lambda x, y: x + y
        Result: 1 + 2 = 3

    Next Step:
    The result 3 is then used with the next element 3:
        lambda 3, 3: 3 + 3 = 6

    Next Step:
    The result 6 is then used with the next element 4:
        lambda 6, 4: 6 + 4 = 10

    Final Step:
    The result 10 is then used with the final element 5:
        lambda 10, 5: 10 + 5 = 15

The final result of the reduce operation is 15, which is the sum of all elements in the list.'''


# Using List Comprehension with the sum Function

numbers = eval(input('Enter List for Comprehension:'))
total = sum(numbers)
print('The Sum for Comprehension=',total)
