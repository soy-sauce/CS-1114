def circular_shift_list1(lst,k):
    lst2=[];
    lst3=[]
    final=[]
    lst2=lst[(len(lst)-k):];
    lst3=lst[:(len(lst)-k)];
    final=lst2+lst3;
    return final;

def main():
    lst=[1,2,3,4,5,6,7,8];
    k=3;
    print(circular_shift_list1(lst,k));

main()