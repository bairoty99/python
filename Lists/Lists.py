#---------------------------
#-----------Lists-----------
#---------------------------

myList=["one","two","one",10,5.66,True]

print(myList)
print(myList[0])
print(myList[-1])
print(myList[-3])

print(myList[1:4])
print(myList[:4])
print(myList[2:])

print(myList[::1])
print(myList[::2])

print(myList)
myList[1]=2
print(myList)
myList[0:3]=["mohamad","sfsa",88]
print(myList)
myList[0:3]=["mohamad"]
print(myList)
myList[0:3]=[]
print(myList)

