#Q1 PART A
def print_shifted_triangle(n, m, symbol):
    spc=" ";
    pattern=1;
    nspc=n-1;
    shift=m+2;

    for i in range(1, n+1):
        triangle=(shift*spc)+(pattern*symbol);
        print(triangle);
        pattern+=2;
        nspc-=1;
        shift-=1;

#Q1 PART B
def print_pine_tree(n, symbol):
    for i in range(1,n+1):
        print_shifted_triangle(i+1,n,symbol)

#Q1 PART C: MAIN FUNCTION
def main():
    n=int(input("Enter n number of triangles: "));
    symbol=input("Enter a character: ")
    print_pine_tree(n, symbol);
    
main()