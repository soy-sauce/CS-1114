val=int(input("Enter a positive integer"));
n=int(input("Enter number of digits"));
sum=0;
f=(10**n)/10
while (n>0):
    temp=(val%(10**(n)));
    sum+=temp//f;
    f=f//10;
    n-=1;


print("Sum is: ",sum);