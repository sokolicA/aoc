paths = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]

diag = [((1, 1), (-1, -1)), ((1, -1), (-1, 1))]


def part_1():
    with open("2024/day_4/input.txt", "r") as file:
        grid = [line.strip() for line in file]
        dim_i = len(grid[0])
        dim_j = len(grid)
        find = "XMAS"
        found = 0
        for i in range(dim_i):
            for j in range(dim_j):
                if grid[i][j] == find[0]:
                    for path in paths:
                        point = [i, j]
                        for k in range(1, len(find)):
                            point[0] += path[0]
                            point[1] += path[1]
                            if point[0] < 0 or point[0] >= dim_i:
                                break
                            if point[1] < 0 or point[1] >= dim_j:
                                break
                            if grid[point[0]][point[1]] != find[k]:
                                break
                            if k == len(find) - 1:
                                found += 1
        print(found)


def part_2():
    with open("2024/day_4/input.txt", "r") as file:
        grid = [line.strip() for line in file]
        dim_i = len(grid[0]) - 1
        dim_j = len(grid) - 1
        found = 0
        for i in range(1, dim_i):
            for j in range(1, dim_j):
                if grid[i][j] == "A":
                    found_current=False
                    for d in diag:
                        point = [i, j]                    
                        p1= [point[0]+d[0][0], point[1]+d[0][1]]
                        p2= [point[0]+d[1][0], point[1]+d[1][1]]
                        chars = [grid[p1[0]][p1[1]], grid[p2[0]][p2[1]]]
                        if not ("M" in chars and "S" in chars):
                            break
                        if found_current:
                            found += 1
                        found_current=True
        print(found)


if __name__ == "__main__":
    part_1()
    part_2()
