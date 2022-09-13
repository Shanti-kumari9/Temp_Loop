n=[100,40,50,54,9,40,5]
i = 0
max=0
while i < len(n):
    if n[i]> max:
        max = n[i]
    i = i + 1
print(max)