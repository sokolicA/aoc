import re


def main():
    with open("day_1/input.txt") as f:
        lines = [line.rstrip() for line in f.readlines()]
        result = 0
        for line in lines:
            tmp = find_first_and_last_number(line)
            result += int(tmp)
        print(result)


def find_first_and_last_number(string):
    NUMBERS = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    pattern = re.compile("|".join("^" + re.escape(value) for value in NUMBERS))

    i = 0
    first = None
    last = None

    while i < len(string):
        if string[i] in NUMBERS.values():
            if first is None:
                first = string[i]
            last = string[i]
        elif match := pattern.search(string[i:]):
            last = NUMBERS[match.group()]
            if first is None:
                first = last
            i += len(last) - 1
        i += 1

    return first + last


if __name__ == "__main__":
    main()
