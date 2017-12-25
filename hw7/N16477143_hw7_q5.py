def string_encoder(string):
    index = 0
    encoded = []
    letter_count = 0
    element = []
    while index < len(string):
        if string[index] == string[0]:
            letter_count += 1
            index += 1
        else:
            encoded.append([string[0],letter_count])
            string = string[index:]
            letter_count = 0
            index = 0
    encoded.append([string[0], letter_count])
    return encoded


def string_decoder(encoded):
    string = ""
    for x in encoded:
        string += x[0] * x[1]
    return string


def main():
    print(string_encoder('aadcccaa'));
    print(string_decoder([['a', 2], ['d', 1], ['c', 4], ['a', 2]]));


main()