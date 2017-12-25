a=input("Enter string: ");
a=a+" "
n=len(a);
temp=0;
n2=0
s2="";

while n2<n:
    if a[n2] == " ":
        s2=a[(temp):(n2)] [::-1]
        print(s2,end=" ")
        temp=n2;
        n2+=1
        s2=""
    else:
        n2+=1;




