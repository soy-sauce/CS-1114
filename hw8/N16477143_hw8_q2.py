def clean_data(complete_weather_filename, cleaned_weather_filename):

    infile=open(complete_weather_filename,"r")
    outfile=open(cleaned_weather_filename,"w")
    for line in infile:

        if line != "\n":

            line=line.strip("\n")
            weather=line.split(",")

            if weather[8]=="T":
                weather[8]="0"
            outfile.write(weather[0]+","+weather[1]+","+weather[2]+","+weather[3]+","+weather[8]+"\n")
    infile.close()
    outfile.close()

def f_to_c(f_temperature):
        f_temperature=float(f_temperature)
        c_temperature=str((f_temperature-32)*(5/9))
        return c_temperature

def in_to_cm(inches):
    inches=float(inches)
    cm=str(inches*2.54)
    return cm

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    infile=open(imperial_weather_filename,"r")
    outfile=open(metric_weather_filename,"w")
    outfile.write("City,Date,High,Low,Precipitation\n")
    line_count=0
    for line in infile:
        if line_count==0:
            pass
        elif line =="\n":
            pass
        else:
            line=line.strip("\n")
            data=line.split(",")
            outfile.write(data[0]+","+data[1]+","+f_to_c(data[2])+","+f_to_c(data[3])+","+in_to_cm(data[4])+"\n")
        line_count+=1
    infile.close()
    outfile.close()

def print_averages_per_month(city, weather_filename,unit_type):
    high_list=[]
    low_list=[]
    for i in range(1,13):
        infile=open(weather_filename,"r")
        high=0
        low=0
        count=0
        for line in infile:
            line=line.strip("\n")
            weather=line.split(",")
            date=weather[1].split("/")
            month=date[0]
            if city==weather[0]:
                if int(month)==i:
                    high += float(weather[2])
                    low+=float(weather[3])
                    count+=1
        high_list.append(round(high/count,3))
        low_list.append(round(low/count,3))

    if unit_type=="metric":
        unit="C"
    else:
        unit="F"

    print("\nAverage temperatures for "+str(city)+":\n")
    print("January: "+str(high_list[0])+unit+" High, "+str(low_list[0])+unit+" Low")
    print("February: "+str(high_list[1])+unit+" High, "+str(low_list[1])+unit+" Low")
    print("March: "+str(high_list[2])+unit+" High, "+str(low_list[2])+unit+" Low")
    print("April: "+str(high_list[3])+unit+" High, "+str(low_list[3])+unit+" Low")
    print("May: "+str(high_list[4])+unit+" High, "+str(low_list[4])+unit+" Low")
    print("June: "+str(high_list[5])+unit+" High, "+str(low_list[5])+unit+" Low")
    print("July: "+str(high_list[6])+unit+" High, "+str(low_list[6])+unit+" Low")
    print("August: "+str(high_list[7])+unit+" High, "+str(low_list[7])+unit+" Low")
    print("September: "+str(high_list[8])+unit+" High, "+str(low_list[8])+unit+" Low")
    print("October: "+str(high_list[9])+unit+" High, "+str(low_list[9])+unit+" Low")
    print("November: "+str(high_list[10])+unit+" High, "+str(low_list[10])+unit+" Low")
    print("December: "+str(high_list[11])+unit+" High, "+str(low_list[11])+unit+" Low")

    infile.close()

def average_precipitation(weather_filename,new_filename,unit_type,city):
    outfile=open(new_filename,"w")
    precip={}
    for i in range(1,13):
        infile=open(weather_filename,"r")
        precip_total=0
        count=0
        for line in infile:
            line=line.strip("\n")
            weather=line.split(",")
            date=weather[1].split("/")
            month=date[0]
            if city==weather[0]:
                if int(month)==i:
                    precip_total+=float(weather[4])
                    count+=1
        precip[i]=round(precip_total/count,4)

    if unit_type=="metric":
        unit="cm"
    else:
        unit="in"

    outfile.write("Precipitation Averages for Each Month in "+str(city)+"\n")
    outfile.write("January: "+str(precip[1])+unit+"\n")
    outfile.write("February: "+str(precip[2])+unit+"\n")
    outfile.write("March: "+str(precip[3])+unit+"\n")
    outfile.write("April: "+str(precip[4])+unit+"\n")
    outfile.write("May: "+str(precip[5])+unit+"\n")
    outfile.write("June: "+str(precip[6])+unit+"\n")
    outfile.write("July: "+str(precip[7])+unit+"\n")
    outfile.write("August: "+str(precip[8])+unit+"\n")
    outfile.write("September: "+str(precip[9])+unit+"\n")
    outfile.write("October: "+str(precip[10])+unit+"\n")
    outfile.write("November: "+str(precip[11])+unit+"\n")
    outfile.write("December: "+str(precip[12])+unit+"\n")

    infile.close()
    outfile.close()

def main():
    print("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")

    print("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")

    print("Running Part C")
    print_averages_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_averages_per_month("New York", "weather in metric.csv", "metric")
    print_averages_per_month("San Jose", "weather in imperial.csv", "imperial")

    print("Running Part D")
    average_precipitation("weather in metric.csv","precipitation.text","metric","New York")

main()