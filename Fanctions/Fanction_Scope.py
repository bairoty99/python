#----------------------------------
#--------  Fanctionscope  ---------
#----------------------------------

x=10 # global scope

def scopeFan():
    global x
    x=100
    print(f"the number of fanction is: {x}")
    
def scopeFann():
    x=20 # Local scope
    print(f"the number from fanction scope is: {x}")

print(x)
scopeFan()
print(x)
scopeFann()