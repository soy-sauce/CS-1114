input=input("Enter a word: ");
vow=0;
con=0;

for i in range(len(input)):
    if (input[i].lower()== "a" or input[i].lower()== "e" or input[i].lower() == "i" or input[i].lower()== "o" or input[i].lower()== "u"):
        vow+=1;
    else:
        con+=1;

print(input," has ",vow," vowels and ",con," consonants");
