#--------------------------------
#-----------Dictionary-----------
#--------------------------------

user={
    "name":"mohamad",
    "age":21,
    "country":"syria",
    "rating":10.6,
    "skils":["html","python","c#"]
}
print(user)
print(user["country"])
print(user.get("age"))
print(user.keys())
print(user.values())

print("="*20)#########

#two-Dimensional Dictionary
languages={
    "js":{
        "rating":"Bad",
        "progress":"10"
        },
    "css":{
        "rating":"Good",
        "progress":"70%"
    },
    "html":{
        "rating":"very Good",
        "progress":"100%"
    }
    
}
print(languages)
print("="*20)#########
print(languages["css"])
print("="*20)#########
print(languages["css"]["progress"])
print("="*20)#########

print(len(languages))
print(len(languages["html"]))
print("="*20)#########

# creat Dictionary from variables
frameworkOne={
    "name":"sql inj",
    "progress":"80%"
}

frameworkTwo={
    "name":"xss",
    "progress":"20%"
}

frameworkThree={
    "name":"file uploud",
    "progress":"50%"
}

allframeworks={
    "first":frameworkOne,
    "secound":frameworkTwo,
    "theird":frameworkThree
}
print(allframeworks)