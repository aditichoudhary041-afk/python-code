 print("Hello, World!")
this is a simple python program to perform arithmetic operations
a=2
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)#
#relationoal operators
a=40
b=80
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
#assignment operators
num=10
num+=10 #num=num+10
print(num)
num-=5 #num=num-5
print(num)
num*=2 #num=num*2
print(num)
num/=5 #num=num/5
print(num)

#logical operators
#not operator
print(not False) #true
print(not True) #false
a=50
b=30
print(not (a>b))#false
print(not (a<b))#true
print(not (a==b))#true
print(not (a!=b))#false

#and operator
val1=True
val2=True
print("and  operator :" + str(val1 and val2)) #true
val1=True
val2=False
print("and operator :" + str(val1 and val2)) #false

 #or  operator
val1=True
val2=False
print("or operator :" + str(val1 or val2)) #true

#type conversion
a=2
b=3.5
print("sum of a and b is :" ,(a+b))

#input in python
name = input("enter your name :")
print("welcome" , name)

val =input("enter a some value :")
print(type(val) , val) #by default input is string

val= float(input("enter a some value:"))
print(type(val) , val) #type conversion to float

name  =input("enter your name :")
age = int(input("enter your age :"))
marks = float(input("enter your marks :"))
print("your deatails are:")
print("name is :", name)
print("age is :", age)
print("marks is :", marks)
