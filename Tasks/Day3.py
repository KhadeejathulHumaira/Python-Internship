#Todays Task
#1)
dict1={"company":"Best Enlist" ,"challenge":"30 days 30 hours"}
dict2={"day1":"completed","day2":"completed","day3":"yet to complete"}
dict1.update(dict2)
print(dict1)
#2)
dict2.pop("day3") #This will remove the element with specified key
print(dict2)
dict1.popitem() #This will remove the last inserted key
print(dict1)
#3)
fruits=["Apple","Banana","Grapes"]
colour=["Red","Yellow","Purple"]
new_dictionary=dict(zip(fruits,colour))
print(new_dictionary)
#4)
set_A={"python","java","C","C++","R",}
print(len(set_A))
#5)
set_B={"python","koltin","js","html","css","java"}
print(set_A-set_B)

