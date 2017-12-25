def n_powers(n):
    lst=[];
    while n>0:
        lst.insert(0,(2**n));
        n-=1;
    return lst;

def main():
    n=4;
    print(n_powers(4));

main()