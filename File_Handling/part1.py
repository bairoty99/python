#---------------------------------
#--------  File Handling ---------
#---------------------------------

# "a" Append Open file For append value, creat file if not exists
# "r" Read   [Default Value] open file for read and give Error if file is not exists
# "w" Write  Open file for Writing, creat file if not exists
# "x" Creat  creat file, give Error if file is exists
#======================================================================================
import os
print(os.getcwd()) # main working Directory
print(os.path.dirname(os.path.abspath(__file__) )) # Directoru for the opened file
print(os.path.abspath(__file__)) # Directoru for the opened file with name
# os.chdir() # to change directory for the current file to the new dir i want 

File=open(r"D:\work\python\File_handling\test.txt","r")

# print(File) # file data object
# print(File.name)
# print(File.mode)
# print(File.encoding)


# print(File.read())
# print("#"*20)

# print(File.read(5))
# print("#"*20)

# print(File.read(6))
# print("#"*20)

# print(File.readline())
# print(File.readline())
# print(File.readline())
# print("#"*20)

# print(File.readline(5))
# print("#"*20)


print(File.readlines())

File.close()