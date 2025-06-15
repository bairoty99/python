#-----------------------------------
#--------  lambda Fanction ---------
#-----------------------------------

def sayHello(name): return f"hello {name}"

hello= lambda name: f"hello {name}"

print(sayHello("ali"))
print(hello("ali"))
print(hello.__name__)
print(type(hello))