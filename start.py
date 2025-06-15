#----------------------
# first code in python
#----------------------
print("hello world")


print(type(5))
print(type(5.55))
print(type("mohamad"))
print(type(True))

myName="Mohamad Bairoty"
a,b,c=10,20,30
print("Hello " + myName +"\nthis is your name^^^^^")
print(a  ,b, c)


string = """
hello
welcome
in 
python
"""
string2= " welcom \
to \
python"

print(string +" " + string2 )

MyString="I Love Python"
print(MyString[2])
print(MyString[0])
print(MyString[-1])
print(MyString[-4])

print(MyString[2:6])
print(MyString[:])
print(MyString[1:7])


print(MyString[0::1])
print(MyString[0::2])

print(len(MyString))

MyString2="  i love py    "
MyString3="####i love py####"

print(MyString2.strip())
print(MyString2.lstrip())
print(MyString2.rstrip())
print(MyString3.lstrip("#"))
print(MyString3.rstrip("#"))

print("hello again")