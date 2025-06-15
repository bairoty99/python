#--------------------------------------
#--------  Fanction Recursion ---------
#--------------------------------------

myWord="MMMMooohhhaaaammmmmaaaaaddddd"

def wordCleaner(word):
    if len(word)==1 or len(word)==0:
        return word
    else:
        if word[0]==word[1]:
            return wordCleaner(word[1:]) 
        else:
            return word[0]+ wordCleaner(word[1:]) 

print(wordCleaner(myWord))


def recursionNumber(n1):
    if type(n1)!= int:
        print("Wrong Format Only Integers Accepted")
    else:
        if n1==1 or n1==0 :
            return n1
        else:
            return n1*recursionNumber(n1-1)

print(recursionNumber(4))