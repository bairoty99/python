# Admin List
Admin_List=["Mohamad","Ali","Ghaith","Omar","Fouad"]

# input user

user=str(input("Enter Your UserName: ")).strip().capitalize()

if user in Admin_List:
    print("You Have Accsess To System........\nYou Want To Enter ==>Edit Mode*_*?")
    dession=str(input("Yes or Not: ")).strip().capitalize()
    if dession=="Yes" or dession=='Y':
        print("#"*50)
        print("You Are In Edit Mode*_*".center(50,"#"))
        print("#"*50)
        mode=str(input("You can Delete Or Update Your UserName What You Want To Do ?")).strip().capitalize()
        if mode=="Update" or mode =='U':
            newUser=str(input("Enter Your New UserName: ")).strip().capitalize()
            if newUser in Admin_List:
                print("You Are In list Alredy")
            else:
                Admin_List[Admin_List.index(user)]=newUser
                print("Your UserName Have Been Updated")
        elif mode=="Delete" or mode=='D':
            Admin_List.remove(user)
            print("Your UserName Have Been Deleted")
        else:
            print("Wrong Command,Try Againg...")
    elif dession=="No" or dession=='N':
        print("No Problem U Are In Normal Mode...")
    else:
        print("Wrong Command,Try Againg...")
else:
    print("you are not admin go to your boss and ask him to give you accsess to this section".title())