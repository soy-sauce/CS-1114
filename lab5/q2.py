n=int(input("Please enter a number: "));
line="";
n2=1
dot="."
ndot=n

while n>0:
    while ndot>0:
        dot="."*n
        ndot-=1;
        dot=dot[:-1]
        line=dot+(str(n2)*n2)
        print(line)
        n-=1;
        n2+=1;