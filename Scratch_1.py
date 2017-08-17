# def main():
#     print("Hello Mardy")
#
# main()
#
# def main():
#     pet_name = input("What is your pets name: ")
#     print("Your pet's name is {:>10s}.".format(pet_name))
#
# main()


def main():
    number = float(input("Input a number: "))
    number = first_addition(number)
    print(float(number))
    number = second_multiplication(number)
    print(float(number))
    number = third_subtraction(number)
    print(float(number))
    number = forth_subtraction(number)
    print("This has now reverted to the number you started with, {:.2f}".format(float(number)))


def first_addition(number):
    number += 2
    return number


def second_multiplication(number):
    number *= 3
    return number


def third_subtraction(number):
    number -= 6
    return number


def forth_subtraction(number):
    number /= 3
    return number

main()
