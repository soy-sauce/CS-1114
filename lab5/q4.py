import turtle;

n=int(input("Enter a number of sides: "));

n2=n;
deg=((n-2)*180)/n;

for i in range(0,n2):
    turtle.forward(100)
    turtle.right(180-deg)
    n2-=1

turtle.done();
