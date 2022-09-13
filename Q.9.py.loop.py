i = 1
sum = 0
while i <= 5:
    num = int(input("enter the number"))
    sum = sum + num
    i = i + 1
print(sum)
average = sum / 11
print(average)
if average % 5 == 0:
    print("it is the multiple of 5")
else:
    print("no its not the multiple of 5")