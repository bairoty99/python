#---------------------------------
#--------  File Handling ---------
#---------------------------------

myFile=open(r"D:\work\python\File_handling\testwithwrite.txt","w")

myFile.write("Hello from python file with love\n")
myFile.write("Hello from python file with no love\n")
myFile.write("Hello from python file with no thing")

# write mode creating new file and add items to it and if it exists it will delete all items to add new items in fanction

myFriends=["ghaith\n","laith\n","omar\n","foad\n"]

myFile2=open(r"D:\work\python\File_handling\MyFriends.txt","w")
myFile2.writelines(myFriends)

myFile3=open(r"D:\work\python\File_handling\MyFriends.txt","a")
myFile3.write("hello from append mode")
myFile3.write("hello from append mode\n")