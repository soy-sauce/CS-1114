def count(lst, item):
    counter=0;
    for i in lst:
        if i==item:
            counter+=1;
    return counter;

def main():
    lst=[0,32,'a','0','4',15,'q','0'];
    print(count(lst,'0'));

main()