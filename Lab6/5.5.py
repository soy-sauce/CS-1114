s=input("Please enter a string s: ")
count=0
sub=""+s[0]
x=0

if len(s) < 4:
    print ("There are no repeating substrings in aba")
else:
    while x < int((len(s)/2)):
        if s[x]!=s[0]:
            sub+=s[x]
        else:
            for i in range(0, len(sub)):
                 if s[i]==sub[0]:
                    print(str(sub))
            count+=1
        x+=1
    print ("The substring " + sub + " repeated " + str(count+1) + " times in " + s)