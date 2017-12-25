s=input("Enter a character: ");
if s.isdigit():
    print(s," is a digit");
elif s.islower():
    print(s," is a lowercase letter")
elif s.isupper():
    print(s," is an upper case letter")
else:
    print(s," is a non-alphanumeric character")