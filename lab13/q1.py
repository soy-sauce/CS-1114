def add_entry(phonebook, name, phonenum):
    if name in phonebook:
        print(name, " already exists")

    elif not phonenum.isdigit() and len(phonenum) != 10:
        print("Not a valid phone number")

    else:
        phonebook[name]=phonenum

def lookup(phonebook, name):
    if name in phonebook:
        return phonebook[name]
    else:
        print("Does not exist")

def print_all(phonebook):
    for name in phonebook:
        print(name,phonebook[name])

def main():
    phonebook={}
    file=open('phonebook.txt','r')
    for line in file:
        line=line.strip('\n')
        lastname = line[:line.find(',')]
        phonenumber = line.split(' ')[-1]
        firstname = line.split(' ')[-2]
        add_entry(phonebook, firstname + ' ' + lastname, phonenumber)
    file.close()

    add_entry(phonebook,'Preston Moore','63699746000')
    print(phonebook)
    print(lookup(phonebook, 'Larry Page'))
    lookup(phonebook, 'Linda Sellie')
    print_all(phonebook)

main()