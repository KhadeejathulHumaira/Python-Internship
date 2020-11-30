#Todays Task
#Day 8
#ERRORS

def errors():
    try:
        a=1
        b=0
        assert b!=0
        print(a*b) #Assertion Error
    except AssertionError:
        print("b cannot be zero")

    try:
        num1=10
        num1.append(3) #AttributeError
    except AttributeError:
        print("Check the asigned value")

    try:
        from math import cube #import error
    except ImportError:
        print("Check the import")
    try:
        import cube #ModuleNotFoundError
    except ModuleNotFoundError:
        print("module is not found")

    try:
        lis=[1,2,3]
        print(lis[4]) #Index error
    except IndexError:
        print("Index is out of bound")

    try:
        print(name) #Name error
    except NameError:
        print("Name is not defined")

    try:
        x=1
        y=0
        print(x/y) #ZeroDivisionError
    except:
        print("denominator should not be zero")

    try:
        print(2+"2") #TypeError
    except TypeError:
        print("Int and string cannot be added")
    try:
        a=int(input("Enter the value"))
        print(a) #ValueError
    except ValueError:
        print("Enter the proper value")

    try:
        dict1={"John":7,"Mahi":7,"Sanam":6}
        print(dict1["Rithi"]) #KeyError
    except KeyError:
        print("value is not there")
errors()

#2)calculator with try and exception
def calculator(a,b):
    try:
        val=int(input("What you want to do?\n1.add\n2.sub\n3.divide\n4.multiplication\nEnter your choice \t"))
        if val==1:
          print(f"The sum of a and b :{a+b}")
        elif val==2:
          print(f"The difference of a and b:{a-b}")
        elif val==3:
          print(f"The division of a and b:{a//b}")
        elif val==4:
          print(f"The multiplication of a and b:{a*b}")
        else:
          print("invalid")
    except ZeroDivisionError:
        print("Divisor should not be 0")

try:
    a=int(input("Enter the a value (calculator):"))#Enter the value of a
    b=int(input("Enter the b value (calculator):")) #Enter the value of b
    calculator(a, b)
except ValueError:
    print("Enter a valid number")
except :
    print("something went wrong")

#3) Try With two exception:
def try_two_except():
    a=input("Enter tha a value")
    num=int(input("Enter the Number"))
    try:
        if a=="Hello":
            b=a
        print(b)
        if num>=0:
            print(num)
        else:
            raise
    except NameError:
        print("Variable is not defined")
    except:
        print("Something went wrong")

try_two_except()

#4)
"""When you don't want your program to break in the middle because of handling errors """

#5)input inside the try
try:
    value=int(input("Enter the value:"))
    if value<20:
        print("The number is given")
    else:
        raise
except:
    print("Error in input value")