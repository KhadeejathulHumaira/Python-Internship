#Todays Task
#Day5
#1)
def calculator(a,b):
    print(f"Addition of two number is:{a+b}\nSubraction of two number is:{a-b}\nDivision of two number is:{a//b}\nMultiplication of two number is:{a*b}")
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
calculator(a,b)

def covid(name,body_temperature=98):
    print(f"Name:"+name,"\nBody Temperature:"+str(body_temperature))
covid("Harry")
covid("Ron",98.6)
