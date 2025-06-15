#--------------------------------
#-------------Tuple--------------
#--------------------------------

#tuple with one element 

myTuple=("moohamad")
myTuple2="moohamad"
myTuple3=("moohamad",)
myTuple4="moohamad",

print(type(myTuple))
print(type(myTuple2))
print(type(myTuple3))
print(type(myTuple4))

# Tuple concatination 
a=(1,2,3,4,5)
b=(6,7)

c=a+b
d=a+(True , "asda",'asd',77)+b

print(d)
print(c)

#Tuple , List ,String Repeat(*)

MyTuple=("a","A","d")
MyList=[110,203,"sa"]
MyString="dasda"

print(MyList*4)
print(MyTuple*4)
print(MyString*4)

#Methods => Count()
a=(1,2,3,4,5,4,1,1)
print(a.count(1))

#Methods => index()
b=(1,2,3,4,5,6,7,8)

# print("The Position of Index Is:" + b.index(7)) # Error
print("The Position of Index Is:{:d}"  .format(b.index(7))) 
print(f"The Position of Index Is: {b.index(7)}") 

#Tuple Destruct
x=("A","B","c")
x,y,z=x
x1=("A","B",20,"c")
x,y,_,z=x1
print(x)
print(y)
print(z)