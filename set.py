#Traversing on set
s = {10, 20, 30, 40, 50}
for i in s:
    print(i)

# Set is an unordered collection of items
list=[1,2,3,4,5]
for i in range(len(list)):
    print(list[i])

#create set from list
lst=[1,2,3,4,5]
print(lst)
s=set(lst)
print(s)

#add
#Add an item to a set, if the item already exists, do nothing
s1={10,20,30}
s1.add(40) 
print(s1)

#union
#Return a set that contains all items from both sets, duplicates are excluded
s2={1,2,3,4,5,1,5}
s3={4,5,6,7,8}
s4=s2.union(s3)
print(s4)

#intersection
#Return a set that contains the items that exist in both set
fruits1={"apple","banana","cherry"}
fruits2={"banana","kiwi","orange"}
fruits3=fruits1.intersection(fruits2)
print(fruits3)

#differrance
#Return a set that contains the items that only exist in set A, and not in set B
animals1={"Cat","Dog","Elephant"}
animals2={"Dog","Tiger","Lion"}
animal=animals1.difference(animals2)
print(animal)