import re


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Robot:
    def __init__(self, position, velocity, grid):
        self.position = position
        self.velocity = velocity
        self.grid = grid

    def move(self):
        x = self.position[0] + self.velocity[0]
        y = self.position[1] + self.velocity[1]
        w, h = self.grid.width, self.grid.height
        if x < 0:
            x += w
        elif x >= w:
            x -= w
        if y < 0:
            y += h
        elif y >= h:
            y -= h

        self.position = (x, y)

    def quadrant(self):
        v = self.grid.width // 2
        h = self.grid.height // 2
        x, y = self.position
        if x < v and y < h:
            return 1
        if x < v and y > h:
            return 3
        if x > v and y < h:
            return 2
        if x > v and y > h:
            return 4
        return 0


def get_robots(grid):
    with open("2024/day_14/input.txt") as file:
        robots = []
        for i, line in enumerate(file):
            match = re.match(
                r"^p=(?P<px>-?\d+),(?P<py>-?\d+) v=(?P<vx>-?\d+),(?P<vy>-?\d+)", line
            )
            m = match.groupdict()
            position = (int(m["px"]), int(m["py"]))
            velocity = (int(m["vx"]), int(m["vy"]))
            robots.append(Robot(position, velocity, grid))

    return robots


def move_robots(robots, seconds):
    for _ in range(seconds):
        for r in robots:
            r.move()

def quadrants_count(robots):
    counts = {i: 0 for i in range(5)}
    for r in robots:
        counts[r.quadrant()] += 1
    return counts

def calculate_safety_factor(counts):
    res = 1
    for q, c in counts.items():
        if 0 < q < 5:
            res *= c
    return res


def p1():
    # grid = Grid(11, 7)
    grid = Grid(101, 103)
    robots = get_robots(grid)
    move_robots(robots, 100)
    counts = quadrants_count(robots)
    print(counts)
    print(calculate_safety_factor(counts))

    # r = Robot((2, 4), (2, -3), grid)
    # for _ in range(6):
    #     r.move()
    #     print(r.position)


def p2(): ...


if __name__ == "__main__":
    p1()
    p2()
