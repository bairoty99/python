#--------------------------------
#-------Dictionary_methods-------
#--------------------------------

# setdeffault()
user={
    "name":"bairoty"
}

print(user)
print(user.setdefault("name","ali"))
print(user.setdefault("age",21))
print(user)

print("="*20)#########

#popitem()
user_2={
    "name":"mohamad",
    "age":21,
    "country":"syria",
    "rating":10.6,
    "skils":["html","python","c#"]
}

print(user_2.popitem())
user_2["language"]="arabic"
print(user_2.popitem())

print("="*20)#########

#items()
user_3={
    "name":"jana",
    "age":35
}
x=user_3.items()
print(x)

print("="*20)#########

#dict.fromkeys()

a=('keyone',"keytwo",20)
b="x"
print(dict.fromkeys(a,b))