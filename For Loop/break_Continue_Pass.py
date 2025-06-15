numbers=[1,2,3,5,8,9,10,11,12,15,16]
for num in numbers:
    if num==10:
        continue
    print(num)

print("#"*20)
for num in numbers:
    if num==10:
        break
    print(num)

print("#"*20)
for num in numbers:
    if num==10:
        pass
    print(num)
