#-----------------------------------------------------------
#-------string formating-------------
#-----------------------------------------------------------

name="mohamad"
age=23
number=963933091499

print("My Name Is: "+name)

#print("My Name Is: "+name +"My Age Is: "+age)-------- #this will return error

#%s->string
#%d->integer
#%f->flout
print("My Name Is: %s" %"mohamad")
print("My Name Is: %s" %name)

print("My Name Is: %s And My Age Is: %d" %(name,age))
print("My Name Is: %s And My Age Is: %f And my number is: %d" %(name,age,number))


n="mohamad"
l="python"
y=10

print("My name is %s I'm %s Developer with %d year of Exp" %(n,l,y))

#control floating point number
numbeer=10
print("My number is %d" %numbeer)
print("My number is %f" %numbeer)
print("My number is %.2f" %numbeer)

#truncate string
mylongstring="Hello people of my learing schoool i heat you "
print("message is %s" %mylongstring)
print("message is %.10s" %mylongstring)

#-----------------------------------------------------------
#-----------New formating string----------------
#-----------------------------------------------------------
