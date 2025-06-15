#--------------------------------
#----------List methods----------
#--------------------------------

#append()
myFriends=["ali","rady","omar"]
myOldFriends=["ghaith","laith","raaed"]
print(myFriends)
myFriends.append("fouad")
print(myFriends)
myFriends.append("007")
print(myFriends)
myFriends.append(myOldFriends)
print(myFriends)

print("#----------------------------------#")
print("#----------------------------------#")
print(myFriends[2])
print(myFriends[4])
print(myFriends[5])
print(myFriends[5][2])
print(myFriends[2][:3])

#extend()
a=[1,2,3,4]
b=["one","two"]
c=[10,True]
a.extend(b)
print(a)
a.extend(c)
print(a)


#remove()

x=[1,2,3,4,5,"ali","omar",True,"omar","omar"]
x.remove("omar")
print(x)

#sort() 
y=[10,20,-6,5,100,-1000,3]
y.sort(reverse=False)#can do recerse=True
print(y)

#reverse
z=[10,1,9,80,100,"ali",654]
z.reverse()
print(z)

