MOVEMENT_CODELIST = {
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
    "^": (0, -1),
}


class Box:
    def __init__(self, positions: list):
        self.positions = positions

    def move(self, direction):
        dx, dy = direction
        self.positions = [(p[0] + dx, p[1] + dy) for p in self.positions]
        return self.positions


class Warehouse:
    MOVEMENT_CODELIST = {
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
        "^": (0, -1),
    }

    def __init__(self, grid: dict):
        self.grid = grid
        self.robot_position = self.find_robot()

    def find_robot(self):
        for p in self.grid:
            if self.grid[p] == "@":
                return p

    def rearrange(self, directions):
        for d in directions:
            self.move_robot(d)

    def move_robot(self, direction):
        dx, dy = direction
        x, y = self.robot_position
        x, y = x + dx, y + dy
        if self.grid[(x, y)] == "#":
            return False
        elif self.grid[(x, y)] == ".":
            return True

    def move_h(self, position, direction):
        dx, dy = direction
        x, y = position
        x, y = x + dx, y + dy

        if self.grid[(x, y)] == "#":
            return False
        elif self.grid[(x, y)] == ".":
            allow = True
        else:
            allow = self.move_h((x + dx, y + dy), direction)

        if allow:
            el = self.grid[position]
            if isinstance(el, Box):
                new_pos = el.move(direction)
                for pos in new_pos:
                    self.grid[pos] = el
                self.grid[(position[0] - dx, position[1] - dy)] = "."
            else:  # robot
                self.grid[position] = "."
                self.grid[(x, y)] = "@"
                self.robot_position = (x, y)
        return allow

    def move_v(self, positions: list, direction):
        dx, dy = direction
        all_positions = set()
        for pos in positions:
            all_positions.add(pos)
            if isinstance(self.grid[pos], Box):
                for p in self.grid[pos].positions:
                    all_positions.add(p)
        new_pos = [(p[0] + dx, p[1] + dy) for p in all_positions]

        if any(self.grid[p] == "#" for p in new_pos):
            return False
        elif all(self.grid[p] == "." for p in new_pos):
            allow = True
        else:
            n = set()
            for p in new_pos:
                if isinstance(self.grid[p], Box):
                    n.add(p)
            allow = self.move_v(n, direction)

        if allow:
            while len(all_positions) > 0:
                p = next(iter(all_positions))
                el = self.grid[p]
                if isinstance(el, Box):
                    bpos = el.positions
                    new_pos = el.move(direction)
                    for pos in new_pos:
                        self.grid[pos] = el
                    for bp in bpos:
                        self.grid[(bp[0], bp[1])] = "."
                    for bp in bpos:
                        all_positions.remove(bp)
                else:  # robot
                    self.grid[p] = "."
                    self.grid[new_pos[0]] = "@"
                    self.robot_position = new_pos[0]
                    all_positions.remove(p)
        return allow

    def get_movement_direction(self, code):
        return self.MOVEMENT_CODELIST[code]

    def calculate_gps_2(self):
        result = 0
        for pt, el in self.grid.items():
            if isinstance(el, Box) and pt == el.positions[0]:
                result += pt[0] + 100 * pt[1]
        return result

    def print(self):
        line = 0
        for p in self.grid:
            if line == p[1]:
                if isinstance(self.grid[p], Box):
                    box = self.grid[p]
                    if p == box.positions[0]:
                        print("[", end="")
                    else:
                        print("]", end="")
                else:
                    print(self.grid[p], end="")
            else:
                print("")
                if isinstance(self.grid[p], Box):
                    box = self.grid[p]
                    if p == box.positions[0]:
                        print("[", end="")
                    else:
                        print("]", end="")
                else:
                    print(self.grid[p], end="")
                line += 1
        print("\n")


def get_input():
    grid = list()
    movements = list()
    with open("2024/day_15/input.txt", "r") as file:
        in_grid = True
        for line in file:
            line = line.strip()
            if line == "":
                in_grid = False
                continue
            if in_grid:
                grid.append(line)
            else:
                movements.append(line)
    return grid, "".join(movements)


def parse_grid_1(grid):
    result = dict()
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            result[(j, i)] = c
    return result


def parse_grid_2(grid):
    result = dict()
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "#":
                result[(2 * j, i)] = "#"
                result[(2 * j + 1, i)] = "#"
            elif c == ".":
                result[(2 * j, i)] = "."
                result[(2 * j + 1, i)] = "."
            elif c == "@":
                result[(2 * j, i)] = "@"
                result[(2 * j + 1, i)] = "."
            elif c == "O":
                b = Box([(2 * j, i), (2 * j + 1, i)])
                result[(2 * j, i)] = b
                result[(2 * j + 1, i)] = b
    return result


def get_initial_position(grid):
    for p in grid:
        if grid[p] == "@":
            return p


def move(position, direction, grid):
    x, y = position
    dx, dy = direction
    dest_x, dest_y = x + dx, y + dy
    x = dest_x
    y = dest_y
    while grid[(x, y)] == "O":
        x += dx
        y += dy
    if grid[(x, y)] == "#":
        return position
    grid[(x, y)] = grid[(dest_x, dest_y)]
    grid[(dest_x, dest_y)] = "@"
    return (dest_x, dest_y)


def gps_coordinate(point):
    return point[0] + 100 * point[1]


def p1():
    grid, movements = get_input()
    grid = parse_grid_1(grid)
    pos = get_initial_position(grid)
    for mov in movements:
        pos = move(pos, MOVEMENT_CODELIST[mov], grid)

    gps_total = 0
    for p, el in grid.items():
        if el == "O":
            gps_total += gps_coordinate(p)
    print(gps_total)


def p2():
    grid, movements = get_input()
    grid = parse_grid_2(grid)
    w = Warehouse(grid)
    for mov in movements:
        if mov == "<" or mov == ">":
            w.move_h(w.robot_position, MOVEMENT_CODELIST[mov])
        else:
            w.move_v({w.robot_position}, MOVEMENT_CODELIST[mov])
    print(w.calculate_gps_2())


if __name__ == "__main__":
    p1()
    p2()
