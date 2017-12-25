input=input("Enter a string of lowercase letters: ");

order=True;

for i in range(1, len(input)):
    if input[i] > input[i-1]:
        order=True;
    else:
        order=False;
        break

if order==True:
    print(input," is increasing");
else:
    print(input," is not increasing");