#-----------------------------------------------------------
#string methods
#-----------------------------------------------------------

#replace(old value,new value ,count)
a="Hello one two three one one"
print(a.replace("one","1"))
print(a.replace("one","1",1))
print(a.replace("one","1",2))

#join(iterable)
mylist=["osama","ali","mohamad"]
print("-".join(mylist))
print(" ".join(mylist))
print(", ".join(mylist))