s=input("Enter a string: ");
n=len(s)
a=s[:n//2];
b=s[n//2:];
count=0;
temp=0
n2=n
n3=n

if (a==b):
    print("The substring ",a," repeats once in ",s);
else:
    while temp<n:
        while a[n2:(n2+1)]!=b[n3:n3+1]:
            n3+=1;
        count+=1;

print("The substring repeats ",count," times in ",s)