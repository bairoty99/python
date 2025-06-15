#-----------------------------------------------------------
#--------------------New formating string-------------------
#-----------------------------------------------------------

name="mohamad"
age=23
number=963933091499

print("My Name Is: "+name)

#print("My Name Is: "+name +"My Age Is: "+age)-------- #this will return error

#{:s}->string
#{:d}->integer
#{:f}->flout
print("My Name Is: {}" .format("mohamad"))
print("My Name Is: {}" .format(name))

print("My Name Is: {} And My Age Is: {}" .format(name,age))
print("My Name Is: {:s} And My Age Is: {:f} And my number is: {:d}" .format(name,age,number))


n="mohamad"
l="python"
y=10

print("My name is {:s} I'm {:s} Developer with {:d} year of Exp" .format(n,l,y))

#control floating point number
numbeer=10
print("My number is {:d}" .format(numbeer))
print("My number is {:f}" .format(numbeer))
print("My number is {:.2f}" .format(numbeer))

#truncate string
mylongstring="Hello people of my learing schoool i heat you "
print("message is {:s}" .format(mylongstring))
print("message is {:.10s}" .format(mylongstring))

#format money
my_money=6546551889465
print("money in my bank:{:d}".format(my_money))
print("money in my bank:{:,d}".format(my_money))
print("money in my bank:{:_d}".format(my_money))


#ReArrange items
a,b,c="one","two","three"
print("hello {} {} {}" .format(a,b,c))
print("hello {1} {2} {0}" .format(a,b,c))
print("hello {2} {0} {1}" .format(a,b,c))

z,x,c=10,20,30

print("Hello {} {} {}" .format(z,x,c))
print("Hello {1:f} {2:.2f} {0:d}" .format(z,x,c))
print("Hello {2:d} {0:f} {1:.1f}" .format(z,x,c))

#formating in version 3.6+

myName="odai"
myAge=26
print("My Name Is : {myName} And My Age Is: {myAge}")
print(f"My Name Is : {myName} And My Age Is: {myAge}")