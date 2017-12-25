def convert_to_bin(n):
    bin=""
    while n>0:
        bin+=str((n%2));
        n=n//2
    return bin

def find_complement(n):
    n=str(n);
    new=""
    sum=0
    for i in range(len(n)):
        if n[i]=='1':
            new=new+'0';
        else:
            new=new+'1';
    return new

num=int(input("Enter a number"))
x=bin(num)
x=x[2:]
print(x)
print(find_complement(x))
y=find_complement(x)
y=int(y, 2)
print(y)