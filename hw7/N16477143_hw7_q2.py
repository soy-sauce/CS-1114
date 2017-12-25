lst=['a', 'b', '10', 'bab', 'a'];

def find_all(lst, val):
    findpos=[];
    for i in range(len(lst)):
        if lst[i] == val:
            findpos.append(i);
    return findpos;

print(find_all(lst, 'a'));
