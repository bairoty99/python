#-----------------------------
#-------  For Loop  ----------
#-----------------------------

numbers=[1,2,3,4,5,6,7,8,9]

for num in numbers:
    print(num)

print("#"*20)
for num in range(1,10):
    print(num)


# dictionary with for loop
mySkills={
    "Html":"100%",
    "JS":"10%",
    "Css":"70%",
    "PHP":"20%",
    "Python":"90%"
}

for skill in mySkills:
    #print(skill) # this will print keys of dict
    print(f"the progress for this skill=>[ {skill.upper()} ] is: {mySkills[skill]}")