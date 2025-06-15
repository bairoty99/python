myStringOne='this is sigel quote'
myStringTwo="this is double quotes"
print(myStringOne)
print(myStringTwo)

# i can use singel quote in double quote like this 
myStringThree="this is string 'with' single quote"
# i can use double quote in single quote like this 
myStringFour='this is string "with" double quote'
print(myStringThree)
print(myStringFour)

# multp line double and singel Quote
# can use double and singel in singel and double quote
myStringFive="""first
secound
third"""
print(myStringFive)

#-----------------------------------------------------------
# string indexing and slicing
#-----------------------------------------------------------

# indexing (Access singel item) 
my_string="I love Python"
print(my_string[0]) # index 0 => I
print(my_string[9]) # index 9 => t

print(my_string[-1])# index -1 => n  first character from end
print(my_string[-5])

# slicing ( Access Multiple sequence items)
# [start:end] end not included
# [start:end:steps] 
print(my_string[8:11])#yth
print(my_string[3:5])#ov

print(my_string[:10])#this start from zero
print(my_string[5:])#this will go to end
print(my_string[:])#full data

print(my_string[0::1])#full data
print(my_string[::1])#full data

print(my_string[::2])#two steps 
print(my_string[::3])#three steps

#-----------------------------------------------------------
#string methodes
#-----------------------------------------------------------

a="I love python" 
b="     I love python        " 
print(len(a))
print(len(b))

# strp(),rstrip(),lstrip()
# remove space char in deffult
print(b.strip())
print(b.rstrip())
print(b.lstrip())

c="######I love python######"
print(c.strip("#"))
print(c.lstrip("#"))
print(c.rstrip("#"))

d="#@#@#@I love python#@#@#@"
print(d.strip("#@"))
print(d.lstrip("#@"))
print(d.rstrip("#@"))


# title() and capitalize()
e = "I love 2d graphics and 3g Technology and python "
print(e.title())
print(e.capitalize())

# zfill()
f,g,h="1","11","122"
print(f.zfill(4))
print(g.zfill(4))
print(h.zfill(4))

# upper()
name="mohamad"
print(name.upper())
# lower()
name="MOhamad"
print(name.lower())
