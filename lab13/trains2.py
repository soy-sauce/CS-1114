def list_stops(train_line, filename):
    infile = open(filename, "r")  # read file from filename
    trains = {}  # dictionary to define stops for 'train line' key
    stops_list = []  # list to hold stops
    for line in infile:  # read each line from the file
        line = line.strip()  # get rid of "\n" at end of each line
        data = line.split(",")  # split each line into a list
        train = data[0][0]  # first letter of first index of list
        train_stop = data[2]  # second index of list is train stop
        if train_line == train:  # if train line is equal to input keep going
            if train_stop not in stops_list:  # if train stop is not already in stops_list, keep going
                stops_list.append(train_stop)  # add to stops_list
    trains[train_line] = stops_list  # define key of the train line as the stops list
    stops_string = ""  # empty string to get rid of brackets for list
    for stops in stops_list:  # add each element in the list to the empty list
        stops_string += stops + ", "
    print(train_line + ": " + stops_string[:-2])  # get rid of last comma


def main():
    user_input = ""
    while user_input != "done":  # while not done, keep asking for input
        user_input = input("Please enter a train line, or 'done' to stop: ")
        if user_input != "done":
            list_stops(user_input, "trains.csv")  # call for function
            print("\n")


main()