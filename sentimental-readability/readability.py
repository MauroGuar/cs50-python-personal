from gc import is_finalized
from operator import index
from re import split as re_split
from cs50 import get_string


def main():
    while True:
        text = get_string("Text: ")
        if text.strip() != "":
            break

    number_of_letters = get_number_letters(text)
    number_of_sentences = get_number_sentences(text)
    number_of_words = get_number_words(text)

    l = (number_of_letters / number_of_words) * 100
    s = (number_of_sentences / number_of_words) * 100
    index = round(0.0588 * l - 0.296 * s - 15.8)

    if index <= 1:
        grade = 1
    elif index <= 16:
        grade = round(index)
    else:
        grade = "16+"
    print(grade)


def get_number_letters(text: str) -> int:
    letters = 0
    for letter in text:
        if letter.isalpha():
            letters += 1
    return letters


def get_number_sentences(text: str) -> int:
    sentences = 0
    for sentence in re_split('[.!?]', text):
        if sentence.strip() != '':
            sentences += 1
    return sentences


def get_number_words(text: str) -> int:
    words = 0
    for word in text.split():
        if word.strip() != '':
            words += 1
    return words


if __name__ == "__main__":
    main()
