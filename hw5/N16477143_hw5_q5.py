pword=input("Enter a password: ");

up=0;
low=0;
length=0;
special=0;

temp=0;

for i in range(len(pword)):
    temp=ord(pword[i])
    if (temp>=65 and temp<=90):
        up+=1;
    elif (temp>=95 and temp<=122):
        low+=1;
    else:
        special+=1;

length=len(pword)
if up>=2 and low>=2 and special>=1 and length>=2:
    print(pword," is a valid password");
else:
    print(pword," is not a valid password");
