#-----------------------------------------------
#--------  Built In Fanction => Filter ---------
#-----------------------------------------------
#filter work when condetion come True only

# Example 1

def checkNumber(n):
    return n>10

myNumber=[1,20,10,15,6,5,80]
fancresult=filter(checkNumber,myNumber)

for number in fancresult:
    print(number)

# Example 2
def checkNames(n):
    n=n.strip().capitalize()
    return n.startswith("M")

myFriends=["MOhamad","mohamad","Masoud ","ali","  Mansour"]

for names in filter(checkNames,myFriends):
    print(names)

print("#"*20)
# Example 3
myFriends=["MOhamad","mohamad","Masoud ","ali","  Mansour"]

for names in filter(lambda n: n.startswith("M"),myFriends):
    print(names)