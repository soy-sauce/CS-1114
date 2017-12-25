s=input("Enter string:");
n=int(input("Enter an integer:"));

newStr="";
start=0;



for i in range((len(s)//2)):
    if (i%2==0):
        newStr = newStr+ s[i*n : i*n+n][::-1]
    else:
        newStr=newStr+s[i*n:i*n+n]
if(len(s)%2 != 0):
    newStr = newStr+s[(i+1)*n:]

print(newStr);

