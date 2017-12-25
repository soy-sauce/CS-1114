def consecutive_chars(s, n):
    print(s,end="")
    line=""
    for i in range(n):
        s=(chr(ord(s)+1));
        if ord(s)<123:
            print(s,end="");
            line=""
        else:
            s=(chr(ord(s)-26));
            print(s,end="");
            line=""



consecutive_chars('a',50)