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

