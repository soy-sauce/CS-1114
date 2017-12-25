def encodeBinary(s):
    counter=1
    s=s+' '
    for i in range (len(s)-1):
        if s[i]==s[i+1]:
          counter+=1;
        else:
            print(counter, s[i],"'s")
            counter=1;

encodeBinary('1111000110')