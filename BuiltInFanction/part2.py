#-------------------------------------
#--------  Built In Fanction ---------
#-------------------------------------

# sum()
# round()
# range()
# print()
#=====================================

# sum(iterable,start)

a=[10,20,50,30]

print(sum(a,-10))

# round(number,numofdigits)
print(round(100.501)) 
print(round(100.601)) 
print(round(100.605,2)) 
print(round(100.65,1)) 

#range(start,end,step)

print(list(range(10)))
print(list(range(2,10)))
print(list(range(0,20,2)))

# print()

print("hello mohamad how are you")
print("hello","mohamad","how","are","you")
print("hello","mohamad","how","are","you",sep=" | ")

print("="*20)

print("first line ",end="this is new end insted of \\n ")
print("secound line", end=" ")
print("third line")
