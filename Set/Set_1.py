#--------------------------------
#-----------set methods----------
#--------------------------------

#Clear()
aset={10,20,30,"one","two",True}
aset.clear()
print(aset)

# Union()

aset={10,30,"one","two",True}
bset={"abcd","sad"}
cset={12,45,8}
# aset.union(bset) # or can union it print(aset | bset)
print(aset | bset)
print(aset.union(bset,cset))
print(aset)

# add()
aset.add("asd") 
print(aset)

#update
aset.update(bset)
print(aset)
bset.update(cset)
print(bset)
#===============================
print("--"*10)
aset.clear()
bset.clear()
cset.clear()

#pop
aset={10,30,"one","two",True}
bset={"abcd","sad"}
cset={12,8}

print(aset.pop())
print(aset.pop())
print(aset)


# remove(),discard()
aset={10,30,"one","two",True}

aset.remove("one")
# aset.remove(7) # Error
print(aset)

aset.discard("two")
aset.discard(20) # No Error
print(aset)

#copy()
aset={10,30,"one","two",True}
bset={"abcd","sad"}
cset=aset.copy()
print(aset)
print(cset)
