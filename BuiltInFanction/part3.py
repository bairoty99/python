#-------------------------------------
#--------  Built In Fanction ---------
#-------------------------------------

# abs()
# pow()
# min()
# max()
# slice()
#=====================================

# abs()

print(abs(10))
print(abs(-10))
print(abs(-10.19))
print(abs(10.19))

# pow(base,exp,mod)
print(pow(10,3)) #(10*10*10)
print(pow(10,2,3)) #(10*10)%3

# min(item,item,item or iterator)
myNuber=(1,20,-52,-100,100)
print(min(1,10,15,-70,-50))
print(min("x","z","mohamad"))
print(min(myNuber))

# max(item,item,item or iterator)
myNuber=(1,20,-52,-100,100)
print(max(1,10,15,-70,-50))
print(max("x","z","mohamad"))
print(max(myNuber))

# slice(start, end ,step)

a=["A","B","C","D","E","F"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2,5)])