import re


def is_in_or_adjacent(number, interval):
    low, high = interval
    low -= 1
    high += 1
    return low <= number <= high


def main():
    with open("2023/day_3/input.txt") as f:
        result = 0
        grid = [line.rstrip() for line in f]
        p_dig = re.compile(r"(\d+)")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = 0
                if grid[i][j] == "*":
                    if i > 0:
                        matches = p_dig.finditer(grid[i - 1])
                        # for m in matches:
                        #     if m.span()

    #     p_sym = re.compile(r"[^\w\.]")
    #     for i, row in enumerate(grid):
    #         print(row)
    #         matches = p_dig.finditer(row)
    #         for m in matches:
    #             t = max(0, i - 1)
    #             b = min(len(grid), i + 2)
    #             l = max(0, m.span()[0] - 1)
    #             r = min(len(row), m.span()[1] + 1)
    #             for el in grid[t:b]:
    #                 print("el", el[l:r])
    #                 if p_sym.search(el[l:r]):
    #                     result += int(m.group(0))
    #                 print(result)

    # print(result)


if __name__ == "__main__":
    main()
