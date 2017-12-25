n=input("Enter number in simplified Roman system: ");
sum=0

for i in range(len(n)):
    if n[i]=='M':
        sum=sum+1000;
    elif n[i]=='D':
        sum=sum+500;
    elif n[i]=='C':
        sum=sum+100;
    elif n[i]=='L':
        sum=sum+50;
    elif n[i]=='X':
        sum=sum+10;
    elif n[i]=='V':
        sum=sum+5;
    elif n[i]=='I':
        sum=sum+1;

print(n," is ",sum)