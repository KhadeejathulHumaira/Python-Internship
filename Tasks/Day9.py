# Today's Task
# Day 9
# Lambda and Map
# 1)Multiply two numbers using lambda
product =lambda a, b:a*b
print(product(2, 3))

# 2)Fibonacci Series using lambda
from functools import reduce
fib =lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(" ".join([str(i) for i in fib(5)]))

# 3)Multiply list elements with given value
list1=[1, 2, 3, 4, 5]
a=int(input("Enter a number"))
multi=list(map(lambda n: n*a, list1))
print(multi)

# 4)Print the numbers divisible by 9
list2=[9, 12, 18, 27, 87, 91, 81, 90, 76, 54]
multiple_9=list(filter(lambda n: n % 9==0, list2))
print(multiple_9)

# 5)Count the even numbers in a list
list3=[2, 3, 4, 5, 6, 7, 8, 9, 0]
even=len(list(filter(lambda n: n % 2==0, list3)))
print(even)