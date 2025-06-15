#-----------------------------------------------------------
#string methods
#-----------------------------------------------------------


#index(substring,start,end)
a="I Love Python"
print(a.index("P"))
print(a.index("P",0,10))
# print(a.index("P",0,5))#substring not found error

#find(substring,start,end)
b="I Love Python"
print(a.find("P"))
print(a.find("P",0,10))
print(a.find("P",0,5))#this get -1 insted of error

# rjust(width,fill char), ljust(width,fill char)
c="Mohamad"
print(c.rjust(10))
print(c.rjust(10,"$"))

print(c.ljust(10))
print(c.ljust(10,"$"))

#splitlines()
e="""first line
secound line
third line
"""
print(e.splitlines())

f="first line \nsecoundline\nthird line"
print(f.splitlines())

g="Hello\tWorld\tI\tlove \tpython"
print(g.expandtabs(5))

#istitle(), isspace(), islower()

one="I Love Python And 5G"
two="I love python And 5g"
print(one.istitle())
print(two.istitle())

three=" "
four=""
print(three.isspace())
print(four.isspace())

five="alixa"
six="Mohamad"
print(five.islower())
print(six.islower())
print(six.isupper())

#isidentifier()
z="mohamad_bairoty"
x="mohamad_bairoty99"
c="mohamad--bairoty100"
print(z.isidentifier())
print(x.isidentifier())
print(c.isidentifier())

#isalpha() just alphabit
v="lksajafbi"
print(v.isalpha())
v="lksajafbi6584"
print(v.isalpha())

#isalnum() alphabit and numbers
n="asdasdfw"
print(n.isalnum())
n="asdasdfw546"
print(n.isalnum())


