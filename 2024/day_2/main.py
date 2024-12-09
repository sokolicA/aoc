def is_safe(vals: list[int]):
    increasing = (vals[1] - vals[0]) > 0
    val = vals[0]
    for v in vals[1:]:
        safe = True
        diff = v - val
        if (1 <= abs(diff) <= 3) and increasing == (diff > 0):
            val = v
        else:
            safe = False
            break
    return safe


def is_safe_2(vals: list[int]):
    safe = False
    for i in range(len(vals)):
        safe = safe or is_safe(vals[:i] + vals[i + 1 :])
    return safe


def main():
    with open("2024/day_2/input.txt", "r") as f:
        number_safe_1 = 0
        number_safe_2 = 0
        while line := f.readline().strip():
            vals = line.split(" ")
            vals = [int(val) for val in vals]
            number_safe_1 += is_safe(vals)
            number_safe_2 += is_safe(vals) or is_safe_2(vals)

        print("Part 1:", number_safe_1)
        print("Part 2:", number_safe_2)


if __name__ == "__main__":
    main()
