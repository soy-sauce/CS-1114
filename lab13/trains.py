def read_trains(filename):
    file=open(filename,'r')
    schedule={}
    trains=[]
    stops=[]
    file.readlines()
    for line in file:
        line=line.strip('\n')
        parts=line.split(',')
        if parts[0][0] not in trains:
            trains.append(parts[0][0])
            if parts[2] not in stops:
                stops.append(parts[2])
        else:
            if parts[2] not in stops:
                stops.append(parts[2])
                stops=[]

        schedule[parts[0][0]]=stops
        stops=[]
    print(schedule)
    file.close()
def main():
    read_trains('trains.csv')

main()