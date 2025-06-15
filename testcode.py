print("\t\t hello!~welcome~")

name = "mohamad"
age = 20
# we can't add number with string with '+'
print("my name is : "+name) 
print(f"1.my name is {name} and my age {age}")
print("2.my name is {} and my age {}".format(name,age))
print("3.my name is {0:s} and my age {1:.1f}".format(name,age))
print("4.my name is {0:s} and my age {1:d}".format(name,age))
print("5.my name is %s and my age %d" %(name,age) )


number =5+10j
print(type(number))
print(f"the Real number is : {number.real} ")
print(f"the imagnary number is : {number.imag}")

number_2 = 10 
print(type(number_2))
print(float(number_2))
print(complex(number_2))
print(str(number_2).zfill(4)) 
lis=[10, 20, 30, 40, 50, 60, 70, 80 ]
# lis.append("mohamd")
# lis.sort() cannot work with strings in arrays
# lis.pop()
print(lis)
# lis.clear()
