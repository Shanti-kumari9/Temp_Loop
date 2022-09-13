# i = 0
# num = int(input("Enter your number:- "))
# while(0 > num):
#     if(num > 0):
    #     print("it is positive")
    #     break
    # elif(num < 0):
    #     print("it is negetive")
    #     break
    # else :
    #     print("zero")
    #     break
    # i = i + 1



a=[1,2,3,4,5,6,7,8,9,10]
b=[]
i=0
while i<len(a):
    if a[i] / 2 == 0:
       b.append(a[i]) 
    i=i+1
print(b)
