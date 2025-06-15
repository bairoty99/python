#--------------------------------
#---------------set--------------
#--------------------------------

# Set Items Are Not Orderd And Not Indexed
# Set Indexing And Slicing Cant Be done

mySet={10,20,30,"one","two",True}

print(type(mySet))
print(mySet)

# print(mySet[0]) # Error
# print(mySet[0:4]) # Error


# Has Only Immutable Data type(string,numbers,boolean,tuple) 
#List and Dict Are Not Immutable
mySet={10,20,30,"one","two",True}# no error
print(mySet)
mySet={10,20,30,"one","two",True,(12,"asd","wq")} #no error
print(mySet)
# mySet={10,20,30,"one","two",True,[12,"asd","wq"]} # TypeError: unhashable type: 'list'
# print(mySet)

#set Items is unique
mySet={1,2,"osama",1,"osama"}
print(mySet)
