def reverse_to_new_list(lst):
    index = len(lst)-1
    reverse_lst = []
    while index >= 0:
        reverse_lst.append(lst[index])
        index -= 1
    return reverse_lst

def reverse_in_place(lst):
    for x in range(0, len(lst)//2):
        lst[x], lst[len(lst)-1-x] = lst[len(lst)-1-x], lst[x]
    return lst


def main():
    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse_to_new_list(lst1)
    print("After reverse to new, lst is", lst1, " and the returned list is ", rev_lst1)
    lst2 = [1, 2, 3, 4, 5, 6]
    reverse_in_place(lst2)
    print("After reverse in place, lst is", lst2)

main()