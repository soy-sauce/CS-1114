s=input("Enter a string: ");

n=len(s)
s2="";
temp=0

while temp<n:
    if s[temp].isupper():
        s2=s2+s[temp].lower();
    else:
        s2 = s2 + s[temp].upper();
    temp+=1;

print(s2)