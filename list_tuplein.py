marks=[12.7 , 45.8 ,13.5 ,19.7 , 23.5 , 45.8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[3])
print(len(marks))
#if i create a student list  
student=["aditi" , 19 , "bca" , "5'5" , "female"]
print(student)

#slicing in list
marks=[34 , 56 , 12 , 13 , 114 ]
print(marks[0:4])

#list methods
list=[12 , 14 , 7 , 9 , 5 , 6]
list.append(10) #adding an element at the end of the list
print(list)

list.sort() #sorting the list in ascending order
print(list)

list.sort(reverse=True) #sorting the list in descending order
print(list)

list.insert(2,13) #inserting an element at a specific index
print(list)

list.remove(14) #removing an element from the list
print(list)

list.pop() #removing the last element from the list
print(list)


#tuples
tup=(12, 13 , 14 , 15)
print(type(tup))

#write  a program to ask the user to enter name  of  their 3  fav movie and store them in a list
movie1=input("enter a first movie name:")
movie2=input("enter a second movie name:")
movie3=input("enter a third movie name:")
movie=[movie1, movie2, movie3]
print(movie)

#count the number of student with the number of grade "A" in the following tuples
grade=("A" ,"B" ,"C" , "A" , "B" , "A")
print(grade.count("A"))

#store the above values in a list and sort them "A" to "D"
grades=("A" ,"B" ,"C" , "A" , "B" , "A")
print(sorted(grades))