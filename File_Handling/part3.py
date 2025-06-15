#---------------------------------
#--------  File Handling ---------
#---------------------------------

myFile=open(r"D:\work\python\File_handling\testwithwrite.txt","a")

myFile.truncate(5)

print(myFile.tell()) # curser position *newline have 2bit

File=open(r"D:\work\python\File_handling\test.txt","r")

File.seek(7)
print(File.read())

