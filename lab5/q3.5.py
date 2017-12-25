n1=int(input("Enter the first number: "));
n2=int(input("Enter the second number: "));
n1O=n1
n2O=n2
h=0;
pholder=0;
num=0;
temp=n1

while temp>0:
    temp=temp//10;
    num+=1;


while num>0:
    n1=n1O//((10**num)/10);
    n1=n1%(10**num);
    n1=n1-(n1%num);
    n2 = n2O // ((10 ** num) / 10);
    n2 = n2 % (10 ** num);
    n2 = n2 - (n2 % num);
    num-=1
    if(n1!=n2):
        print(n1,n2)
        h+=1;


print(h);
