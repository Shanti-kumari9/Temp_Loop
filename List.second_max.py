n=[100,40,50,54,9,40,5]
i = 0
max=0
while i < len(n):
    if n[i]>max:
        max = n[i]
    i = i + 1
max1=max
print("this is the max number",max1)
n.pop(0)
n1=n
i=0
second_max=0
while i<len(n1):
    if n[i]>second_max:
        second_max=n1[i]
    i=i+1
print("this is the second max number",second_max)