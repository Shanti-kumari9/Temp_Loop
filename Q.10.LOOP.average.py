i = 0
counter=0
string = "shnati"
print(len(string))
while (i < len(string)):
    i=i+1
    if string[i] == "a":
        continue

    elif string[i] == "n":
        continue
    counter=counter+1
 
print("The end", counter)