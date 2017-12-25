def get_common_element(lst1,lst2):
    lst3=[]
    for i in range(len(lst1)):
        for j in range(len(lst2)-1,-1,-1):
            if lst1[i]==lst2[j]:
                lst3.append(lst2[j]);
                lst2.pop(j)
    return lst3;


def main():
    lst1=[2,'S',3.13,3.13,'python'];
    lst2=['pythy',2,12,'hello',3.13];
    print(get_common_element(lst1,lst2))

main()