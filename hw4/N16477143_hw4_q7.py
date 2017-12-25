import random

n=random.randint(1,101);
print("I thought of a number between 1 and 100");
print(n)
val=int(input("Try to guess what is is: "))
times=0
low=1
high=100

for i in range(5):
    while(val!=n and time<0):
        if(val>n):
            if(val>low and val<high):
                high=val;
            print("Range: ",low,", ",high)
            print("Wrong guess, try a smaller number");
            i+=1
        else:
            if (val > low and val < high):
                low = val;
            print("Range: ", low, ", ", high)
            print("Wrong guess, try to larger number");
            i+=1
        val = int(input("Try to guess what is is: "));
    print("Congrats! You guess my number in ",times);

#Sorry I had a lot of trouble with this lab, and did not have enough time to
#finish it. I was able to get the range estimator, but I can't get it to
#restrict it to 5 guesses. I do know that in order to to do, another loop
#must be used so that after each iteration, that a counter will go up.
#once it reaches 5, the loop ends and so does the game.