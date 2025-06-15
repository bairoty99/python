name=str(input("Enter Your name: ")).strip().capitalize()
email=str(input("Enter Your Email: ")).strip()
password=str(input("Enter Your Password: ")).strip()

print(f"Welcome {name.strip()} In Bairoty acadimy \nYour username is:@{email[:email.index("@")]}\nYour password is :{password[0]}"+"*"*(len(password)-2)+password[-1])

