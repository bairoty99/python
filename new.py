# ------------------------------------------------------------------
# age=int(input("enter you age: "))
# if age>=20 and age<=40 :
#     print("your age is : "+ str(age))
# else:
#     print("try again later")
# ------------------------------------------------------------------
# userName_list=["mohamad","ali","odai","nadia","ola","aziz"]
# password="tryHackme"
# userName=str(input("Enter your username: "))
# if userName in userName_list:
#     passW=str(input("Enter your password: "))
#     if passW==password:
#         print("you have access to this device.")
#     else:
#         print("Incorect password try later...")
# else:
#     print("FK u bsh")
# ------------------------------------------------------------------
# def test_fun():
#     print("Hello am testing this function")
# def welcomeMessage(name):
#     print("welcome {} in this testing code" .format(str(name)))
#     print(f"you have permision to pass {name}")
# test_fun()
# welcomeMessage("mohamad")

#-------------------------------------
suspatios_IpaAddresses=["192.168.166.89","82.145.36.1","48.155.6.94"]
#Fanction to get first 3 ip addresses and add it to new list
def getf3ips(x):
    newIpAddresses=[]
    for ip in x:
        newIpAddresses.append(ip[:ip.index(".")])
    return newIpAddresses

print(getf3ips(suspatios_IpaAddresses))