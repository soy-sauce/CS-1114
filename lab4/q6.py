n=int(input("Enter a number: "));

for i in range (1,n+1):
    for j in range(1,n+1):
        if(j==i):
            print("o", end=" ");
        else:
         print("x", end =" ");
    print();