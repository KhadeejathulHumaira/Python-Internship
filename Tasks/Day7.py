#Todays Task
#Day7
#1)Create a module and import it
import mymod as md
print(md.list1)
for i in range(len(md.list1)):
   md.list1[i]=i+3
print(md.list1)
#2)Import pandas and use it
import pandas as pd
a=["Ron","John","Kiran"]
b=[24,25,22]
c=list(zip(a,b))
df=pd.DataFrame(data=c,columns=['Name','Age'])
print(df)
#3)Generate random number
import random as rd
print("Random Number:",rd.randint(1,100))
#4)Import sys
import sys
print("\n".join(sys.path))
#5) pip install numpy
#  pip uninstall numpy
