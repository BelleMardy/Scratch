def main():
    number = int(input("Enter a number: "))
    print(odd_even(number))
    if odd_even(number) == 0:
        print("The number {}, is even.".format(number, odd_even(number)))
    else:
        print("The number {}, is odd.".format(number, odd_even(number)))


def odd_even(number):
    number_calculted = number % 2
    return number_calculted

main()

# 86 400 seconds in a day
SECONDS = 60
MINUTES = 60


def main():
    seconds = int(input("Enter seconds: "))
    minutes = seconds // SECONDS
    seconds_left_after_minutes_calculated = seconds % SECONDS
    hours = minutes // MINUTES
    minutes_left_after_hours_calculated = minutes % MINUTES
    print("In {} there are {} hours, {} minutes, {} seconds,".format(seconds, hours,
                                                                     minutes_left_after_hours_calculated,
                                                                     seconds_left_after_minutes_calculated))


#     seconds = int(input("Input number of seconds: "))
#     print(int(minutes(seconds)))
#     remaining_seconds = seconds % SECONDS
#     print(int(remaining_seconds))
#
#     print(int(hours(minutes)))
#
#
# def minutes(seconds):
#     minutes = int(seconds // SECONDS)
#     return minutes
#
#
# # def hours(minutes):
#     hours = int(minutes // MINUTES)
#     return hours

main()

