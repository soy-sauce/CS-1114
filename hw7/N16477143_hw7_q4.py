lst=[2,4,6,8,10];

def create_prefix_lists(lst):
    lst2=[];
    for i in range(len(lst)):
        lst2.append(lst[0:i]);
    return lst2

print(create_prefix_lists(lst));