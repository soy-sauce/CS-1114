n=int(input("Enter a number: "));


for i in range(1, n+1):
    even = 0;
    odd = 0;
    temp = i;
    while(temp>0):
        n1=temp%10;
        if(n1%2==0):
            even+=1;
        else:
            odd+=1;
        temp=temp//10
    if (even>odd):
        print(i);

