studentinfo ={
    "name" : "aditi",
    "age" : 19,
    "course" : "bca",
    "height" : "5'7\"" ,
    "gender" : "female",
    "college" : "SD groups of college college",
    "semester" : "1" ,
    "subjects" : ["maths" , "english" , "computer architecture" , "iks"],
 }
print(studentinfo["name"])
print(studentinfo["subjects"])
print(studentinfo["age"])
print(studentinfo["semester"])
print(studentinfo["height"])
print(studentinfo["college"])

print(type(studentinfo))
studentinfo["name"]="avni"
print(studentinfo)

null_dicti={}
print(null_dicti)

#nested dictionary
shop_prod={
    "cosmetic": "skin product",
    "price" :{
        "herbal" : "599",
        "organic" : "999",
        "imported" : "98$",
    }
}
print(shop_prod["price"]["organic"])

#Dictionary Methods
print(shop_prod.keys())
print(list(shop_prod.keys()))
print(shop_prod.items())
print(shop_prod.get("cosmetic"))
new_dic={"ayurvedic" : "1000"}
shop_prod.update(new_dic)
print(shop_prod)
new_dic={"cosmetic": "women care",}
shop_prod.update(new_dic)
print(new_dic)
print(shop_prod.values())

#set in python
collection={1,2,3,4,5,6, "Hello World", "Namaste"}
print(collection)
print(type(collection))
print(len(collection))

collection2={"hello" , "hello" , "namaste" , "welcome"}
print(collection2)
print(len(collection2)) #duplicate value not valid in sets of python

collection3=set() #synntax of empty sets

set=set()
set.add(4)#add
set.add(89)
set.add(9)
set.add(67)
set.add(4100)
set.add((1,3,5,))#we can add tuple
set.add("apna college")#we can add str #but we don't add dic,list
set.remove(89)#remove

print(set)

#set method
#union
#intersection
set1={1,2,3,3}
set2={4,2,7,4}#output is (1,3,4,7)
print(set1.union(set2))
print(set1.intersection(set2))

#Store the following word meanings in a Python dictionary:
dictionary={
"table": ["a piece of furniture","list of facts & figures",],
"cat": "a small animal",

}
print(dictionary)

#You are given a list of subjects for students. Assume one classroom is required for one subject. How many classrooms are needed by all students?
subjects={
"python", "java", "C++", "python", "javascript"
"java", "python", "java", "C++", "C"
}
print(subjects)
print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.
marks={}
x=int(input("enter chem:"))
marks.update({"chem": x})

x=int(input("enter bio:"))
marks.update({"bio": x})

x=int(input("enter computer:"))
marks.update({"computer": x})

print(marks)

#Figure out a way to store 9 and 9.0 as separate values in a set.

#(You can take help of built-in data types.)

value={9 ,"9.0"}
print(value)

# 2nd type
value={
    ("float",9.0),
    ("int",9),

}
print(value)