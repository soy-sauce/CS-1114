import random

n=random.randint(1,101);
print("I thought of a number between 1 and 100");
print(n)
val=int(input("Try to guess what is is: "))

while(val!=n):
    if(val>n):
        print("Wrong guess, try a smaller number");
    else:
        print("Wrong guess, try to larger number");
    val = int(input("Try to guess what is is: "));

print("Congrats! You guess my number")