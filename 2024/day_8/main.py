def get_input():
    with open("2024/day_8/input.txt", "r") as file:
        return [line.strip() for line in file]


def get_locations(grid):
    locations = {}
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            char = grid[j][i]
            if char.isalnum():
                if char in locations:
                    locations[char].append((i, j))
                else:
                    locations[char] = [(i, j)]
    return locations


def get_distance(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])


def find_antinodes(char_locations):
    antinodes = set()
    for i in range(len(char_locations) - 1):
        loc_i = char_locations[i]
        for j in range(i + 1, len(char_locations)):
            loc_j = char_locations[j]
            dist = get_distance(loc_i, loc_j)
            antinodes.add((loc_i[0] + dist[0], loc_i[1] + dist[1]))
            antinodes.add((loc_j[0] - dist[0], loc_j[1] - dist[1]))
    return antinodes

def find_antinodes_2(char_locations, dim):
    antinodes = set()
    for i in range(len(char_locations) - 1):
        loc_i = char_locations[i]
        for j in range(i + 1, len(char_locations)):
            loc_j = char_locations[j]
            dist = get_distance(loc_i, loc_j)
            k = (loc_j[1]-loc_i[1]) / (loc_j[0]-loc_i[0])
            n = loc_i[1] - k * loc_i[0]
            x = loc_i[0]
            xs = []
            while 0 <= x < dim[0]:
                xs.append(x)
                x = x + dist[0]
            x = loc_j[0]
            while 0 <= x < dim[0]:
                xs.append(x)
                x = x - dist[0]
            for x in xs:
                y = int(round(k * x + n))
                if 0 <= y < dim[1]:
                    antinodes.add((x, y))
    return antinodes


def part_1():
    # On both sides of the line #..A..A..# the distance between A and # is the distance between A and A
    # find positions of same alphanumeric characters.,. {"A": [(1, 1), ...]}
    # for each character find those that are in a straight line. Determine the locations of the antinodes
    # and check if they are on map. Remove the visited characters from the set
    grid = get_input()
    locations = get_locations(grid)
    antinodes = set()
    for char in locations:
        antinodes = antinodes.union(find_antinodes(locations[char]))

    result = set()
    for antinode in antinodes:
        if (
            antinode[0] < 0
            or antinode[0] >= len(grid[0])
            or antinode[1] < 0
            or antinode[1] >= len(grid)
        ):
            continue
        result.add(antinode)

    print(len(result))

def part_2():
    grid = get_input()
    locations = get_locations(grid)
    antinodes = set()
    for char in locations:
        antinodes = antinodes.union(find_antinodes_2(locations[char], (len(grid[0]), len(grid))))
    print(len(antinodes))


if __name__ == "__main__":
    part_1()
    part_2()
