#strings in python

str1="hello world"

str2='hello world'
str3="""hello world"""
print(str1 + "\n" + str2 + "\n" + str3)

str1="""hello"""
str2="""world"""
print(str1+str2)
print(len(str1))

str1="aditi rohal"
char=str1[3]
print(char)

str="apnacollege"
print(str[:4])

str="apple"
print(str[-3:-1])

str="i'm aditi rohal and im studying in bca first year"
print(str.capitalize())
print(str)

str="i'm aditi rohal and im studying in bca first year"
print(str.replace("and" ,"or"))

str="i'm aditi rohal and im studying in bca first year"
print(str.find("i"))

str="i'm aditi rohal and im studying in bca first year"
print(str.count("a"))

str=input("enter your first name:")
print(str)
print=len(str)

str="i'm a $ i want a $ $99.99 $ is a symbol of money"
print(str.count("$"))

#conditional statements in python
age=int(input("enter your age:"))
if(age>=18):
    print("you are eligible for license and vote")

else:
    print("you are not eligible for license or vote")

light="red"
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("get ready to move")
elif(light=="green"):
    print("go")
else:
    print("invalid color")

marks=int(input("enter your marks:"))
if(marks>=90):
    print("grade A")
elif(marks>=80):    
    print("grade B")

   # nesting

age=int(input("enter your age:"))
if(age>=18):
    if(age>=80):
        print("cannnot drive")
    else:
        print("can drive")
else:
    print("cannot drive")


#checking even or odd number

num=int(input("enter a number:"))
if(num%2==0):
    print("even number")
else:
    print("odd number")

#checking multiple of 7
    
value=int(input("enter a number:"))
if(value%7==0):
    print("yes,its a multiple of 7")
else:
    print("no,its not a multiple of 7")

a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
c=int(input("enter a third number:"))
if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
else:
    print("c is greater")
    