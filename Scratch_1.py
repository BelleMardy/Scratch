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
ADDITION = 2
MULTIPLICATION = 3
SUBTRACTION = 6
DIVISION = 3


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
    number += ADDITION
    return number


def second_multiplication(number):
    number *= MULTIPLICATION
    return number


def third_subtraction(number):
    number -= SUBTRACTION
    return number


def forth_subtraction(number):
    number /= DIVISION
    return number

main()


MAN = 1
MULTIPLE = 7
WIFE = 1
SACK = 1
CAT = 1
KITTEN = 1


def main():
    wives = wife()
    print("{:>4d}".format(wives))
    sacks_wives = wives * sack()
    print("{:>4d}".format(sacks_wives))
    cats_sacks_wives = sacks_wives * cat()
    print("{:>4d}".format(cats_sacks_wives))
    kittens_cats_sacks_wives = cats_sacks_wives * kitten()
    print("{:>4d}".format(kittens_cats_sacks_wives))
    total = MAN + wives + sacks_wives + cats_sacks_wives + kittens_cats_sacks_wives
    print("Wives {}, sacks {}, cats {}, kittens {}, total travelled {}.".format(wives, sacks_wives, cats_sacks_wives,
                                                                                kittens_cats_sacks_wives, total))


def wife():
    wives = WIFE * MULTIPLE
    return wives


def sack():
    sacks = SACK * MULTIPLE
    return sacks


def cat():
    cats = CAT * MULTIPLE
    return cats


def kitten():
    kittens = KITTEN * MULTIPLE
    return kittens


main()


def main():
    number = input("Enter a number: ")
    print(str(number), int(number), float(number), sep=", ")

main()