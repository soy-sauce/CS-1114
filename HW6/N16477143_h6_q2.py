#q2a print_month_calendar(num_of_days, starting_day)
def print_month_calendar(num_of_days, starting_day):
    tab="\t"
    days=""
    daysBefore=0

    print("Mon\tTue\tWed\tThu\tFri\tSat\tSun");

    if starting_day == 2:
        days=days+tab;
        daysBefore=1;
    elif starting_day == 3:
        daysBefore=2
        days=days+(tab*daysBefore)
    elif starting_day == 4:
        daysBefore = 3
        days = days + (tab * daysBefore)
    elif starting_day == 5:
        daysBefore = 4
        days = days + (tab * daysBefore)
    elif starting_day == 6:
        daysBefore = 5
        days = days + (tab * daysBefore)
    elif starting_day == 37:
        daysBefore = 6
        days = days + (tab * daysBefore)

    for i in range(1, num_of_days+1):
        days=days+str(i)+tab;
        i=str(i);
        daysBefore+=1;

        if daysBefore==7:
            days=days+"\n"
            daysBefore=0;

    print(days)
    nextDay=daysBefore+1
    return nextDay

#q2b leap year
def leap_year(year):
    if year % 400 ==0:
        return True;
    if year % 100 ==0:
        return False;
    if year % 4 == 0:
        return True
    else:
        return False

#q2c print_year_calendar(year, starting_day)
def print_year_calendar(year, starting_day):
    print("\t\t\tJanuary", year)
    nextDay=print_month_calendar(31, starting_day);
    if leap_year(year)==True:
        print("\n\t\t\tFeburary", year)
        nextDay=print_month_calendar(29, nextDay);
    else:
        print("\n\t\t\tFebruary", year)
        nextDay = print_month_calendar(28, nextDay)
    print("\n\t\t\tMarch", year)
    nextDay = print_month_calendar(31, nextDay)
    print("\n\t\t\tApril", year)
    nextDay =print_month_calendar(30, nextDay)
    print("\n\t\t\tMay", year)
    nextDay = print_month_calendar(31, nextDay)
    print("\n\t\t\tJune", year)
    nextDay = print_month_calendar(30, nextDay)
    print("\n\t\t\tJuly", year)
    nextDay = print_month_calendar(31, nextDay)
    print("\n\t\t\tAugust", year)
    nextDay = print_month_calendar(31, nextDay)
    print("\n\t\t\tSeptember", year)
    nextDay =print_month_calendar(30, nextDay)
    print("\n\t\t\tOctober", year)
    nextDay = print_month_calendar(31, nextDay)
    print("\n\t\t\tNovember", year)
    nextDay = print_month_calendar(30, nextDay)
    print("\n\t\t\tDecember", year)
    nextDay = print_month_calendar(31, nextDay)

#q2d main()
def main():
    year=int(input("Enter a year: "));
    starting_day=input("Enter the day n of the week: ");
    print_year_calendar(year, starting_day)

main()
