# empty list 
myfavWeb=[]

#max size 
maximumWeb=5

while maximumWeb>0:
    web=str(input("Enter Your Favorit Website Without https://"))
    myfavWeb.append(f"https://"+web.strip().lower())
    maximumWeb -= 1
    print(f"Your Webstie Has Been Added,You Have {maximumWeb} places to fill")
else:
    print("Your Bookmarks is full")
    
if len(myfavWeb)>0:
    
    #sort list 
    myfavWeb.sort()
    listlen=0
    print("listing element of your bookmarks")
    while listlen<len(myfavWeb):
        print(myfavWeb[listlen])
        listlen+=1