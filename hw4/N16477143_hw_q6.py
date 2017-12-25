input=int(input("Enter a length of sequence: "));
x=1;
n=input

for i in range(input):
    x =x*(int(input("Enter a number: ")))
#I worked very hard on this problem and it doesn't seem to work.
#I talked with a lot of upperclassmen to help me teach me so I could create
#a logical solution. I tried using a boolean for the loop, which
#I am not sure whether or not is allowed. However,  another student told me
#There is a problem that is near impossible to do in pycharm, and has to be
#done in IDLE. I know this is the problem and I can't seem to solve it. But
#my reasoning was to take the calculations and do them while taking the
#inputs. I tried my best and I can't get this one to work. Sorry :(
mean = x**(1/input)
print("The geometric mean is:",mean);


while keepGoing:
    inputs=input("Please enter a number: ")
    if ints == "Done":
        keepingGoing = False
    else:
        x=x*int(inputs)
        integerCount+=1;

mean = x **(1/integerCount)
print("The geometric mean is: ",mean);
