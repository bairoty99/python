#-----------------------------
#--------  Fanction  ---------
#-----------------------------

#========================
print("="*20)

def welcommsg():
    print("Hello World")
    
welcommsg()

#========================
print("="*20)

def returnfan():
    return "this string from fanction return"
txt=returnfan()
print(txt)

#========================
print("="*20)


def addition(n1,n2):
    if type(n1)!=int or type(n2)!=int:
        print("Wrong Input Only Int Or Float Numbers")
    else:
        print(n1+n2)
addition(10,25)

#========================
print("="*20)

def names(xx,*x):
    print(f"all {xx} friend's names:")
    for name in x:
        print(f">{name}")

names("ali","omar","aziz")

#========================
print("="*20)


# type of this **x is dict so we can add dict from outside of def or add key and value in arguments
fandict={
    "osama":"zero",
    "ahmad":"mohsen"
}
    

def names(xx,**x):
    print(f"all {xx} friend's names:")
    for name_key,name_value in x.items():
        print(f">{name_key} {name_value}")

names("ali",osama="zero",ahmad="mohsen")
names("mohamad",**fandict)
#========================
print("="*20)

def man_info(name="unknown",age="unknown",country="unknown"):
    print(f"Your name is: {name} & age is: {age} & country is: {country}")

man_info()

#========================
print("="*20)
