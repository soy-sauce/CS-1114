import random
def create_permutation(n):
    lst=[];
    compare=0;
    for i in range(n+1):
        compare=random.randint(0,n);
        while compare in lst:
            compare=random.randint(0,n);
        lst.append(compare)
    return lst

def scramble_word(word):
    n=(len(word)-1)
    lst=create_permutation(n)
    scrambled="";
    for i in lst:
        scrambled=scrambled+word[i]+' ';
    return scrambled

def main():
    f=open('wordbank.txt','r'); #I renamed the file to wordbank in folder
    lines=f.readlines()
    lines=[f.strip('\n') for f in lines]
    rand=random.randint(0,len(lines)+1)
    print(lines)
    original=lines[rand]
    scrambled=scramble_word(original)
    print("Unscramble the word: ",scrambled)
    word=input("Try #1: ")
    n=1;
    while word != original:
        print("wrong!")
        n+=1
        print("Try #",n)
        word=input("")
    print("Yay! You got it!")
    f.close()

main()
