divd=int(input("Enter dividend"));
divs=int(input("Enter divisor"));
n=0;

while (divd>divs):
    divd=divd-divs;
    n+=1;

print("The quotient of ",divd," divided by ",divs," is: ",n);