#Today's Task
#Day 10
# Regular Expressions
#1)
import re
text=input("Enter text")
pattern=re.compile("[a-zA-Z0-9]+")
if pattern.fullmatch(text) is None:
    print("It contains special characters")
else:
    print("It has only certain characters")

#2)matches a word containing "ab"
text1="Abraka Dabra "
if re.search("ab",text1) :
    print("Match found")
else:
    print("Not found")

#3)check number at the end
text2= "The Number is 2019"
find=re.search("[0-9]$",text2)
if find:
    print("found")
else:
    print("not found")

#4)
number=re.finditer(r"([0-9]{1,3})","The Numbers are 2,3,4,567,8800 use them wisely")
print("The numbers are")
for i in number:
    print(i.group(0))

#5)
text3=input("Enter text")
pattern=re.compile("[A-Z]+")
if pattern.fullmatch(text3) is None:
    print("Match not found")
else:
    print("Match found")