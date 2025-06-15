#--------------------------------
#-------Dictionary_methods-------
#--------------------------------

# Clear()
user={
    "name":"mohamad",
    "age":21,
    "country":"syria",
    "rating":10.6,
    "skils":["html","python","c#"]
}
print(user)
user.clear()
print(user)

print("="*20)#########

# update()
member={
    "name":"ali"
}

print(member)
member["age"]=36
print(member)
member.update({"country":"syria","bank account":1236548955})
print(member)

print("="*20)#########

# copy()
main={
    "name":"mohamad"
}
b=main.copy()
c=main

print(b)
print(c)

main.update({"skil":"xss&sql"})
print(b)
print(c)

print("="*20)#########

