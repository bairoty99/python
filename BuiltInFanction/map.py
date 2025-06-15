#--------------------------------------------
#--------  Built In Fanction => Map ---------
#--------------------------------------------

#use Map with predefined Fanction

def formatText(text):
    return f"- {text.strip().capitalize().center(10," ")} -"
myTexts=["  Ali ","Mohamad","  Aziz      "]

myformatedData=map(formatText,myTexts)

for name in myformatedData:
    print(name)

print("="*20)

for name in map(formatText,myTexts):
    print(name)

print("="*20)

for name in list(map(formatText,myTexts)):
    print(name)

print("="*20)
# use Map with lambda Fanction
myTexts=["  Ali ","Mohamad","  Aziz     ","Omar"]

for name in map(lambda text: f"- {text.strip().capitalize().center(10," ")} -",myTexts):
    print(name)
