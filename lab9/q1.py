def consec_int(myInt, n):
    lst=[];
    lst.append(myInt);
    while n>1:
        lst.append((int(myInt))+1);
        myInt+=1
        n-=1;
    return lst

def main():
    myInt=10
    n=5
    print(consec_int(myInt, n));

main()