s=input("Please enter a string s: ")
sub1=""
sub2=""
count=0
sub=s[0]
x=0

if len(s)<4:
    print ("There are no repeating substrings in aba")
else:
    while x<int(len(s)):

        if s[x] != s[0]:
            sub += s[x]
        else:
            print (str(sub))
        x += 1
    print ("The substring " + sub + " repeated " + str(count) + " times in " + s)