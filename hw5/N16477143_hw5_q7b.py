n = int(input("Please enter a positive integer: "))
line = ""

while n > 0:
    if n >= 1000:
        line += "M"
        n -= 1000
    elif n >= 500:
        line += "D"
        n -= 500
    elif n >= 100:
        line += "C"
        n -= 100
    elif n >= 50:
        line += "L"
        n -= 50
    elif n >= 10:
        line += "X"
        n -= 10
    elif n >= 5:
        line += "V"
        n -= 5
    elif n >= 1:
        line += "I"
        n -= 1

print(line)