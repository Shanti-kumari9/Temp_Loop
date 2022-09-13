def Prime_num(num):
    i = 2
    c = 0
    while i < num:
        if num % i == 0:
            c = c + 1
        i = i + 1
    if c == 0:
        print("prime",num)
    else:
        print("not prime",num)
num = int(input("enter the number"))
Prime_num(num)


# +++++++++++++============SECOND METHOUD=============+++++++++++

# def Prime_num(num):
#     i = 2
#     c = 1
#     while i < num:
#         if num % i == 0:
#             c = c + 1
#         i = i + 1
#     if c == 1:
#         print("prime",num)
#     else:
#         print("not prime",num)
# num = int(input("enter the number"))
# Prime_num(num)