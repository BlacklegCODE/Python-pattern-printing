import time

# mini project for practice
# Attempting to print patterns with time limit

a = input("Sign :")

b = int(input("Enter the number of rows :"))

c = int(input("1: Upper triangle, 2: Lower triangle  \n Enter your choice"))

z = int(input("Enter time in seconds :"))



while c != 0:

    if c == 1:
        for i in range(1, b + 1):
           time.sleep(z)
           print(a * i)



    elif c ==2:
     for i in range(b,0,-1):
         time.sleep(z)
         print(a * i)


    else:
        print("Invalid choice !")

    c = int(input("Enter choice again :"))
