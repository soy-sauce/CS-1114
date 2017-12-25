n1=int(input("Enter the first number: "));
n2=int(input("Enter the second number: "));
n3=n1
n4=n2
numsplace=0;
numsplace2=numsplace
n=numsplace
tempn=n1
h=0

while n>0:
    n3=n1//(10**numsplace)
    n4=n2//(10**numsplace)
    if(n3==n4):
         h+=1;
    n3=n%(10**numsplace)
    n4=n%(10 ** numsplace)
    n-=1;
    numsplace-=1;

print(h)
'''while numsplace>0:
    n1=(n1//(10*numsplace));
    n2=(n1//(10*numsplace));
    if(n1==n2):
        h+=1;
    else:

print(h);'''