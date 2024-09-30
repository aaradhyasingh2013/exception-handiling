try:
    n= int(input("enter a number"))
    print(n)
except ValueError as er:
    print("exception: ",er)