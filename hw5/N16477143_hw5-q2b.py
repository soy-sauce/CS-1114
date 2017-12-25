s=input("Enter a character: ");
ord=ord(s);


if (ord>=65 and ord<=90):
    print(s," is an upper case letter");
elif (ord>=95 and ord<=122):
    print(s," is a lower case letter");
elif (ord >= 48 and ord <= 57):
    print(s, " is a digit");
else:
    print(s, " is a non alphanumeric character")