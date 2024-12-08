from sys import exit
from cs50 import get_string


def check_luhn_algorithm(card_number: str) -> bool:
    counter = 0
    for i in reversed(range(0, len(card_number), 2)):
        number = int(card_number[i]) * 2
        counter += number if number < 10 else (number // 10 + number % 10)

    for i in reversed(range(1, len(card_number), 2)):
        counter += int(card_number[i])
    return True if counter != 0 and counter % 10 == 0 else False


def main():
    while True:
        card_number = get_string("Card Number: ")
        if len(card_number) == 16:
            break

    if not check_luhn_algorithm(card_number):
        print("INVALID")
        exit(0)

    if card_number.startswith(("34", "37")):
        print("AMEX")
    elif card_number.startswith(("51", "52", "53", "54", "55")):
        print("MASTERCARD")
    elif card_number.startswith("4"):
        print("VISA")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
