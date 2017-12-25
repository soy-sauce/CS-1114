#lst1=[1, 2, 3];
#lst2=[4, 5, 6];

def add_list(lst1, lst2):
    lst3=[];
    temp=0
    for i in range(len(lst1)):
        temp=int(lst1[i])+int(lst2[i]);
        lst3.append(temp);
    return lst3

#print(add_list(lst1, lst2));

def get_lst1():
    lst1 = [];
    val = (input("Enter a number for list 1, type 'done' to finish: "));
    while val!= 'done':
        lst1.append(val);
        val = (input("Enter a number for list 1, type 'done' to finish: "));
    return lst1;

def get_lst2():
    lst2 = [];
    val = (input("Enter a number for list 2, type 'done' to finish: "));
    while val!='done':
        lst2.append(val);
        val = (input("Enter a number for list 2, type 'done' to finish: "));
    return lst2

def main():
    print(add_list(get_lst1(), get_lst2()));

main()
