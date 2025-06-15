#-----------------------------------------------------------
#string methods
#-----------------------------------------------------------

# spilt(),rsplit()
a="I love Python and c#"
print(a.split())#diffulte is space
a="I-love-Python-and-c#"
print(a.split())
print(a.split("-"))
a="I-love-Python-and-c#-and-c++"
print(a.split("-",3))
print(a.rsplit("-",3))

# center()
name="MOHAMAD"
print(name.center(11))
print(name.lower().center(11,"*"))

# count()
f="I love Python and c# Because c# is Easy"
print(f.count("c#")) #search for c#
print(f.count("c#",0,25)) # start search from 0 to 25 index

# swacase()
g="I Love Python"
print(g.swapcase())

# startswith() , endswith()

v="I love Python and c#"
print(v.startswith("I"))
print(v.startswith("d"))
print(v.startswith("l",2,6))

print(v.endswith("#"))
print(v.endswith("# "))
print(v.endswith("n",7,13))
