num=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
m=0
l=0
while(i<len(num)):
    if(num[i]>20 and num[i]<40):
        m=m+1
    else:
        l=l+1
    i=i+1
print(m)
print(l)