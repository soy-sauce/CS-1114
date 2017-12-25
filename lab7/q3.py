s=(input("Enter Ascii to Text"));


def convertAsciiToText(n):
    str = "";
    for i in range(len(n)//2):
        str=str+(chr(int(n[i*2:2+(i*2)])));
    return str

print(convertAsciiToText(s))