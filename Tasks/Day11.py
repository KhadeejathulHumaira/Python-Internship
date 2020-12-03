#Today's task
# Day 11
#Zip ,Map and Filter
#1)merged list of tuples
fruits=["Apple","Banana","Strawberry","Grapes","Orange"]
colors=["Red","Yellow","Redish","Purple","Orange"]
zip_list=list(zip(fruits,colors))
print(zip_list)

#2)New list of tuples
alphabets=["A","B","C","D","E","F","G","H"]
new=list(zip(range(1,8),alphabets))
print(new)

#3)Sort the list
list1=[12,3,45,6,78,9,4,13]
print(sorted(list1))

#4)Filter the even numbers
list4=[1,4,6,8,9,7,6,5,43]
odds=list(filter(lambda n: n%2!=0 , list4))
print(odds)

