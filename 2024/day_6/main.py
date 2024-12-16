DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


class Direction:
    DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self, direction):
        # if direction not in self.DIRECTIONS:
        #     raise ValueError("Direction not allowed.")
        self.direction = self.DIRECTIONS.index(direction)

    def get(self):
        return self.DIRECTIONS[self.direction]

    def get_x(self):
        return self.DIRECTIONS[self.direction][0]

    def get_y(self):
        return self.DIRECTIONS[self.direction][1]

    def next(self):
        if self.direction == 3:
            self.direction = 0
        else:
            self.direction += 1


def get_grid():
    with open("2024/day_6/input.txt", "r") as file:
        grid = [line.strip() for line in file]
    return grid


def get_start_position(grid):
    START = "^"
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == START:
                return (x, y)


def traverse_grid(grid, start, direction):
    positions = set()
    positions.add(start)
    direction = Direction(direction)
    x = start[0]
    y = start[1]
    while 0 < x < (len(grid[0]) - 1) and 0 < y < (len(grid) - 1) and grid[y][x] != "#":
        while grid[y + direction.get_y()][x + direction.get_x()] == "#":
            direction.next()
        x = x + direction.get_x()
        y = y + direction.get_y()
        positions.add((x, y))
    return positions


def is_loop(grid, start, direction):
    positions = set()
    positions.add((start, direction))
    direction = Direction(direction)
    x = start[0]
    y = start[1]
    while 0 < x < (len(grid[0]) - 1) and 0 < y < (len(grid) - 1) and grid[y][x] != "#":
        while grid[y + direction.get_y()][x + direction.get_x()] == "#":
            direction.next()
        x = x + direction.get_x()
        y = y + direction.get_y()
        new = ((x, y), direction.get())
        if new in positions:
            return True
        positions.add(new)
    return False

def traverse_grid_2(grid, start, direction):
    direction = Direction(direction)
    x = start[0]
    y = start[1]
    result = set()
    while 0 < x < (len(grid[0]) - 1) and 0 < y < (len(grid) - 1):
        while grid[y + direction.get_y()][x + direction.get_x()] == "#":
            direction.next()
        x = x + direction.get_x()
        y = y + direction.get_y()
        grid_copy = [x for x in grid]
        grid_copy[y] = grid[y][:x] +  "#" + grid[y][x+1:]
        if is_loop(grid_copy, start, (0, -1)):
            result.add((x, y))
    return result


def part_1():
    grid = get_grid()
    start = get_start_position(grid)
    result = traverse_grid(grid, start, (0, -1))
    print(len(result))


def part_2():
    # loop: Če si v neki točki že bil in postaviš obstruction in je naslednja smer enaka kot 3 nazaj
    # v za vsako točko (x, y) shraniš točko in smer in
    #  daš obstruction v naslednjo točko, določiš novo smer in preveriš, če se to že ponovi 3 korake nazaj
    grid=get_grid()
    start = get_start_position(grid)
    result = traverse_grid_2(grid, start, (0, -1))
    print(len(result))

if __name__ == "__main__":
    part_1()
    part_2()
