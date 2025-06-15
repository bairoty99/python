#--------------------------------
#-----------set methods----------
#--------------------------------

#issuperset()
a={1,2,3,4}
b={1,2,3}
c={1,2,3,4,5}

print(a.issuperset(b))
print(a.issuperset(c))

print("="*20)#########

#issubset()
a={1,2,3,4}
b={1,2,3}
c={1,2,3,4,5}

print(a.issubset(b))
print(a.issubset(c))

print("="*20)#########

#isdisjoint()
a={1,2,3,4}
b={1,2,3}
c={10,20,30}

print(a.isdisjoint(b))
print(a.isdisjoint(c))