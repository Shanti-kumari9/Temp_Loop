num = int(input("enter the number"))
i = 1
c = 0
while i < num:
    if num % i == 0:
        c = c + 1
    i = i + 1
if c == 1:
    print("prime",num)
else:
    print("not prime",num)
