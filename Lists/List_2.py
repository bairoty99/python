#--------------------------------
#----------List methods----------
#--------------------------------

#clear()
a=[1,2,3,4]
a.clear()
print(a)

#copy()
b=[10,20,30]
c=b.copy()
print(b)
print(c) 


#count()
d=[1,2,3,4,3,9,10,1,2,1,2]
print(d.count(1))

#index()
myFriends=["ali","rady","omar","ghaith","omar","raaed"]
print(myFriends.index("omar"))

#insert()
x=[1,2,3,4,5,"ali","omar"]
x.insert(0,"xxx")
x.insert(-1,42)
print(x)

#pop()
g=[1,2,3,4,5,"ali","omar"]
print(g.pop(-1))
print(g)
