number=int(input("enter the number"))
i=1
max=0
while i<number:
    num=int(input("enter the number"))
    if num>max:
        max=num
    i=i+1
print("Greater number:",max)