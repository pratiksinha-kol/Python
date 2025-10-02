# Prompt the user for a date in MM/DD/YYYY format or in Month is words
# Then output the date in "Year-Month-Date" format
# Handle invalid inputs gracefully
# For example, if the user inputs "3/4/2023", the program should output "March 4, 2023"
# If the user inputs "13/4/2023" or "3/32/2023", the program should not crash
# For Invalid inputs, the program should simply prompt the user again for a valid date


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")

    try:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)

        if month < 1 or month > 12:
            raise ValueError

        if day < 1 or day > 31:
            raise ValueError

        if year < 0:
            raise ValueError
        
        # if month == 2 and day > 29:
        #     raise ValueError

        print(f"{year}-{month:02}-{day:02}")
        break
    except (ValueError, IndexError):
        try:
            month_str, day, year = date.split(" ")
            if not day.endswith(","):
                raise ValueError
            month_str = month_str.capitalize()
            day = int(day.rstrip(","))
            year = int(year)

            if month_str not in months:
                raise ValueError

            month = months.index(month_str) + 1

            if day < 1 or day > 31:
                raise ValueError

            if year < 0:
                raise ValueError
            
            # if month == 2 and day > 29:
            #     raise ValueError

            print(f"{year}-{month:02}-{day:02}")
            break
        except (ValueError, IndexError):
            continue 