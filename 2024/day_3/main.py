import re


def calculate_1(string):
    pattern = r"mul\(([0-9]+,[0-9]+)\)"
    matches = re.findall(pattern, string)
    pairs = [match.split(",") for match in matches]
    products = [int(pair[0]) * int(pair[1]) for pair in pairs]
    return sum(products)


def calculate_2(string):
    pattern = r"do\(\).*?don't\(\)"
    matches = re.findall(pattern, "do()" + string + "don't()", re.DOTALL)
    result = 0
    for m in matches:
        result += calculate_1(m)
        print(calculate_1(m))

    return result


def main():
    with open("2024/day_3/input.txt", "r") as file:
        result_1 = 0
        result_2 = 0
        text = "".join(file.readlines())
        result_1 += calculate_1(text)
        result_2 += calculate_2(text)

        print("Part 1:", result_1)
        print("Part 2:", result_2)


if __name__ == "__main__":
    main()
