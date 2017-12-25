val=int(input("Enter a positive integer: "));
sum=0

for i in range (0,val+1):
    if (i%2==0):
        sum=sum-i;
    else:
        sum=sum+i

print(sum)

