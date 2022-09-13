a = 4
i = 1
while i <= 5:
    num = int(input("enter the number"))
    if num < a:
        print("aap ka number chota h! ek aur bar try karo")
    elif num > a:
        print("aap ka number bada h ")
    else:  
        print("waah! guess sahi h ")
    i = i + 1
