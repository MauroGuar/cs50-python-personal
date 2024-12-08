from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height in range(1, 9):
            break

    for i in range(height):
        blank_spaces_before = height - (i + 1)
        blank_spaces_after = i + 1
        print(" " * blank_spaces_before, end="")
        print("#" * blank_spaces_after, end="")
        print("  ", end="")
        print("#" * blank_spaces_after)


if __name__ == "__main__":
    main()