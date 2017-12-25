a=input("Enter string a: ");
b=input("Enter string b: ");

countA=len(a)
countB=len(b)

if countA>countB:
    print(a,b,a,sep=(""));
else:
    print(b,a,b,sep=(""));