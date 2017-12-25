def find_max_even_index(lst):
    index=-1
    max=0
    for i in range(len(lst)):
        if ((lst[i]%2)==0):
            if((lst[i])>max):
                index=i;
                max=lst[i]
    return index

def main():
    lst=[56,24,58,10,33,95];
    print(find_max_even_index(lst));

main()