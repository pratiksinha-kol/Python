#########################################
#
# Convert time into decimal
# Use the decimal to determine meal time
#
#########################################


def main():
    current_time = input("What time is it? ").strip()
    converted_time = convert(current_time)
    # print(converted_time)
    if converted_time >= 7 and converted_time <= 8:
        print("breakfast time")
    elif converted_time >= 12 and converted_time <= 13:
        print("lunch time")
    elif converted_time >= 18 and converted_time <= 19:
        print("dinner time")

def convert(time):
    time_parts = time.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])

    # Convert it into decimal hours
    return hours + minutes / 60

if __name__ == "__main__":
    main()
