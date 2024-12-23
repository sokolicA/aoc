DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def get_map():
    with open("2024/day_10/input.txt") as file:
        return [[int(x) for x in line.strip()] for line in file]


def get_height(grid, x, y):
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        return grid[y][x]


def get_trailheads(grid, start_x, start_y):
    trailheads = []
    current_height = grid[start_y][start_x]
    if current_height == 9:
        return [(start_x, start_y)]
    else:
        for d in DIRECTIONS:
            next_x = start_x + d[0]
            next_y = start_y + d[1]
            if get_height(grid, next_x, next_y) == (current_height + 1):
                trailheads += get_trailheads(grid, next_x, next_y)
    return trailheads


def get_starts(m):
    starts = []
    for y, row in enumerate(m):
        for x, height in enumerate(row):
            if height == 0:
                starts.append((x, y))
    return starts


def p1():
    m = get_map()
    starts = get_starts(m)
    score = sum([len(set(get_trailheads(m, x, y))) for x, y in starts])
    print(score)


def p2():
    m = get_map()
    starts = get_starts(m)
    score = sum([len(get_trailheads(m, x, y)) for x, y in starts])
    print(score)


if __name__ == "__main__":
    p1()
    p2()
