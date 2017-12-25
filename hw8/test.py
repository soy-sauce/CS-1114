def clean_data(complete_weather_filename, cleaned_weather_filename):
    # Complete this function to clean the CSV.
    # It should create a new file as specified in the assignment specs.
    infile = open(complete_weather_filename, "r")  # opens file to read
    outfile = open(cleaned_weather_filename, "w")  # opens file to write in
    for line in infile:  # loop to look at each line
        if line != "\n":  # if line is not empty, continue
            line = line.strip("\n")  # take out "\n" in the end that creates new line
            weather = line.split(",")  # create a list out of each line of data
            if weather[8] == "T":  # if precipitation = "T", then change it to 0
                weather[8] = "0"
            outfile.write(weather[0] + "," + weather[1] + "," + weather[2] + "," + weather[3] + "," + weather[
                8] + "\n")  # write the needed categories into outfile
    infile.close()  # close file being read
    outfile.close()  # close file being written in


# Part B
def f_to_c(f_temperature):
    f_temperature = float(f_temperature)  # converts the string to a float
    c_temperature = str((f_temperature - 32) * (5 / 9))  # formula to convert fahrenheit to celsius
    return c_temperature  # return the celsius temp


def in_to_cm(inches):
    inches = float(inches)  # converts the string to a float
    cm = str(inches * 2.54)  # formula to convert inches to cm
    return cm  # returns the cm


def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    infile = open(imperial_weather_filename, "r")  # open file to read
    outfile = open(metric_weather_filename, "w")  # open file to write
    outfile.write("City,Date,High,Low,Precipitation\n")  # write heading
    line_count = 0  # count lines
    for line in infile:  # read lines from read file
        if line_count == 0:  # if line is heading, skip it
            pass
        elif line == "\n":  # if line is emtpy, skip it
            pass
        else:
            line = line.strip("\n")  # take out "\n" in the end that creates new line
            data = line.split(",")  # split each line to create list of data
            outfile.write(data[0] + "," + data[1] + "," + f_to_c(data[2]) + "," + f_to_c(data[3]) + "," + in_to_cm(
                data[4]) + "\n")  # write the data onto write file
        line_count += 1  # increase line count by 1
    infile.close()  # close infile
    outfile.close()  # close outfile


# Part C
def print_average_temps_per_month(city, weather_filename, unit_type):
    high_list = []  # list of average high values for each month
    low_list = []  # list of average low values for each month
    for i in range(1, 13):  # range of months from 1-12
        infile = open(weather_filename, "r")  # open the file each time because loop ends it at the last line
        high = 0  # value holder to find total high values for each month
        low = 0  # value holder to find total low values for each month
        count = 0  # count occurences to use to find average
        for line in infile:  # look at each line in the read file
            line = line.strip("\n")  # take away the "\n" creating a new line at the end of each line
            weather = line.split(",")  # split each line into a list to have separate data points
            date = weather[1].split("/")  # split the date using a list to get the month
            month = date[0]  # the first index of 'date' is the month e.g. 10/5/2015 "10" is month
            if city == weather[0]:  # if the city is equal to the city on the line, keep going
                if int(month) == i:  # if month is equal to the number on the loop, keep going
                    high += float(weather[2])  # add weather[2] which is the high value for that day
                    low += float(weather[3])  # add weather[3] which is the low value for that day
                    count += 1  # add a count to count the occurence
        high_list.append(round(high / count, 3))  # add the average high to the list and round to 3 places
        low_list.append(round(low / count, 3))  # add the average low to the list and round to 3 places

    if unit_type == "metric":  # if unit_type is metric, use C, if not use F
        unit = "C"
    else:
        unit = "F"

    print("\nAverage temperatures for " + str(city) + ":\n")  # print the heading and values for each month
    print("January: " + str(high_list[0]) + unit + " High, " + str(low_list[0]) + unit + " Low")
    print("February: " + str(high_list[1]) + unit + " High, " + str(low_list[1]) + unit + " Low")
    print("March: " + str(high_list[2]) + unit + " High, " + str(low_list[2]) + unit + " Low")
    print("April: " + str(high_list[3]) + unit + " High, " + str(low_list[3]) + unit + " Low")
    print("May: " + str(high_list[4]) + unit + " High, " + str(low_list[4]) + unit + " Low")
    print("June: " + str(high_list[5]) + unit + " High, " + str(low_list[5]) + unit + " Low")
    print("July: " + str(high_list[6]) + unit + " High, " + str(low_list[6]) + unit + " Low")
    print("August: " + str(high_list[7]) + unit + " High, " + str(low_list[7]) + unit + " Low")
    print("September: " + str(high_list[8]) + unit + " High, " + str(low_list[8]) + unit + " Low")
    print("October: " + str(high_list[9]) + unit + " High, " + str(low_list[9]) + unit + " Low")
    print("November: " + str(high_list[10]) + unit + " High, " + str(low_list[10]) + unit + " Low")
    print("December: " + str(high_list[11]) + unit + " High, " + str(low_list[11]) + unit + " Low")

    infile.close()  # close the file


# Part D
# Find average precipation for a given city and given month and write it to a new file

def average_precipitation(weather_filename, new_filename, unit_type, city):
    outfile = open(new_filename, "w")  # open file to write in
    precip = {}  # dictionary to hold values for each month precipitation in the format {"1":5}
    for i in range(1, 13):  # loop to run through the months 1-12
        infile = open(weather_filename, "r")  # open file each time run loop because at end of loop end up at last line
        precip_total = 0  # value holder to store total precipitation
        count = 0  # count for total occurence
        for line in infile:  # read each line in the file
            line = line.strip("\n")  # take away the "\n" at the end of each line that creates a new line
            weather = line.split(",")  # split the line into a list to have separate data points
            date = weather[1].split("/")  # split the date to have the month
            month = date[0]  # the first index (0) is the month
            if city == weather[0]:  # if weather[0] (the city) is = to the city entered, keep going
                if int(month) == i:  # if the month is equal, keep going
                    precip_total += float(weather[4])  # add the float of weather[4] (precipitation) to the total
                    count += 1  # add count of occurence to help find average
        precip[i] = round(precip_total / count,
                          4)  # enter each as a key value term into the dictionary so it can be called for later on

    if unit_type == "metric":  # if unit type entered is metric, then use cm, else use in
        unit = "cm"
    else:
        unit = "in"

    outfile.write("Precipitation Averages for Each Month in " + str(
        city) + "\n")  # print heading and average precipitation for each month using key from dictionary
    outfile.write("January: " + str(precip[1]) + unit + "\n")
    outfile.write("February: " + str(precip[2]) + unit + "\n")
    outfile.write("March: " + str(precip[3]) + unit + "\n")
    outfile.write("April: " + str(precip[4]) + unit + "\n")
    outfile.write("May: " + str(precip[5]) + unit + "\n")
    outfile.write("June: " + str(precip[6]) + unit + "\n")
    outfile.write("July: " + str(precip[7]) + unit + "\n")
    outfile.write("August: " + str(precip[8]) + unit + "\n")
    outfile.write("September: " + str(precip[9]) + unit + "\n")
    outfile.write("October: " + str(precip[10]) + unit + "\n")
    outfile.write("November: " + str(precip[11]) + unit + "\n")
    outfile.write("December: " + str(precip[12]) + unit + "\n")

    infile.close()  # close in file
    outfile.close()  # close out file


def main():
    print("Running Part A")
    clean_data("weather.csv",
               "weather in imperial.csv")  # run part A using weather.csv and write into weather in imperial.csv

    print("Running Part B")
    convert_data_to_metric("weather in imperial.csv",
                           "weather in metric.csv")  # use Part B to convert weather in imperial.csv to metric and write into weather in metric.csv

    print("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv",
                                  "imperial")  # use Part C to find imperial average temps per month for San Francisco
    print_average_temps_per_month("New York", "weather in metric.csv",
                                  "metric")  # use Part C to find average temps per month for New York in metric
    print_average_temps_per_month("San Jose", "weather in imperial.csv",
                                  "imperial")  # use Part C to find imperial average temps per month for San Jose

    print("Running Part D")
    average_precipitation("weather in metric.csv", "precipitation.txt", "metric",
                          "New York")  # use part D to find average precipitation per month in New York in metric


main()  # call for main function