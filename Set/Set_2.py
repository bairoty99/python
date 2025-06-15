#--------------------------------
#-----------set methods----------
#--------------------------------

#defference()

a={1,2,3,4}
b={1,2,"ali","omar"}
print(a)
print(a.difference(b)) # a-b no edite
print(a)

print("="*20)##############

#difference_update()
a={1,2,3,4}
b={1,2,"ali","omar"}
print(a)
a.difference_update(b) # a-b with edit set
print(a)

print("="*20)##############

#intersection()
a={1,2,3,4,"ali"}
b={5,2,"ali","omar"}
print(a)
print(a.intersection(b)) # a&b no edite
print(a)

print("="*20)##############

#intersection_update()
a={1,2,3,4,"ali"}
b={5,2,"ali","omar"}
print(a)
a.intersection_update(b) # a&b with edite
print(a)

print("="*20)##############

#symmetric_difference()
a={1,2,3,4,"ali"}
b={1,2,"ali","omar"}
print(a)
print(a.symmetric_difference(b)) # a^b without edite
print(a)

print("="*20)##############

#symmetric_difference()
a={1,2,3,4,"ali"}
b={1,2,"ali","omar"}
print(a)
a.symmetric_difference_update(b) # a^b with edite
print(a)