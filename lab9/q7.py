def find_mean(lst):
    return sum(lst)/len(lst);

def remove_below_avg(lst):
    mean=find_mean(lst);
    for i in range(len(lst)-1,-1,-1):
        if lst[i]<mean:
            lst.pop(i);

    return lst;

def main():
    lst=[2,3,5,1,-4,8,0,-1];
    print(remove_below_avg(lst));

main()
