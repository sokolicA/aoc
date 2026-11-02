def read_file(filepath: str) -> tuple:
    ranges = []
    available = []
    active = ranges
    with open(filepath, "r") as f:
        while line := f.readline():
            l = line.strip()
            if l == "":
                active = available
                continue
            active.append(l)

    return ranges, available


def parse_ranges(ranges: list[str]) -> list[list]:
    return [rng.split("-") for rng in ranges]


def get_available_ids(available: list[str]) -> set:
    return {int(x) for x in available}


def solve_p1(filepath: str) -> int:
    ranges, avail = read_file(filepath)
    ranges = parse_ranges(ranges)
    # print("fresh ids", ranges)
    avail = get_available_ids(avail)

    counter = 0
    for el in avail:
        for r in ranges:
            if int(r[0]) <= el <= int(r[1]):
                counter += 1
                break

    return counter


def solve_p2(filepath: str) -> int:
    ranges, _ = read_file(filepath)
    ranges = parse_ranges(ranges)
    sr = sorted(ranges, key=lambda x: int(x[0]))
    # print(sr)

    max_n = int(sr[0][0])

    count = 0

    for r in sr:
        if int(r[1]) < max_n:
            continue
        left = max(max_n, int(r[0]))
        count += int(r[1]) - left + 1
        print("range:", r, "Added:", int(r[1]) - left + 1)
        max_n = int(r[1]) + 1

    return count


if __name__ == "__main__":
    print(solve_p1("2025/d5/p1.txt"))
    print(solve_p2("2025/d5/p1.txt"))
