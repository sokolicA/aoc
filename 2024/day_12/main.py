def get_input():
    with open("2024/day_12/input.txt") as file:
        result = dict()
        for j, line in enumerate(file):
            line = line.strip()
            result = result | {(i, j): line[i] for i in range(len(line))}
        return result


def find_neighbours(point, farm):
    neighbours = []
    pts = [
        (point[0] + 1, point[1]),
        (point[0] - 1, point[1]),
        (point[0], point[1] + 1),
        (point[0], point[1] - 1),
    ]
    for pt in pts:
        if farm[point] == farm.get(pt):
            neighbours.append(pt)
    return neighbours


def get_region(point, farm: dict):
    region = [point]
    for el in region:
        for x in find_neighbours(el, farm):
            if x not in region:
                region.append(x)
        farm.pop(el)
    return region


def get_regions(farm):
    regions = {}
    while len(farm) > 0:
        point = list(farm.keys())[0]
        l = farm[point]
        if l in regions:
            regions[l].append(get_region(point, farm))
        else:
            regions[l] = [get_region(point, farm)]
    return regions


def count_borders(points):
    count = 0
    for point in points:
        pts = [
            (point[0] + 1, point[1]),
            (point[0] - 1, point[1]),
            (point[0], point[1] + 1),
            (point[0], point[1] - 1),
        ]
        count += 4 - sum(1 for pt in pts if pt in points)
    return count


def count_corners(region):
    count = 0
    for pt in region:
        x, y = pt
        
        north = (x, y-1) not in region
        south = (x, y+1) not in region
        east = (x+1, y) not in region
        west = (x-1, y) not in region

        # Check diagonal neighbors
        ne = (x+1, y-1) in region
        nw = (x-1, y-1) in region
        se = (x+1, y+1) in region
        sw = (x-1, y+1) in region


        if north:
            if west:
                count += 1
            if east:
                count += 1
            if nw and not west:
                count += 1
            if ne and not east:
                count += 1

        if south:
            if west:
                count += 1
            if east:
                count += 1
            if sw and not west:
                count += 1
            if se and not east:
                count += 1
    return count


def count_corners2(region):
    count = 0
    for pt in region:
        x, y = pt
        # Check missing cardinal neighbors (N, E, S, W)
        north = (x, y-1) not in region
        south = (x, y+1) not in region
        east = (x+1, y) not in region
        west = (x-1, y) not in region

        # Check diagonal neighbors
        ne = (x+1, y-1) in region
        nw = (x-1, y-1) in region
        se = (x+1, y+1) in region
        sw = (x-1, y+1) in region

        # North corners
        if north and west and not nw: count += 1
        if north and east and not ne: count += 1

        # South corners
        if south and west and not sw: count += 1
        if south and east and not se: count += 1

        if north and nw:count += 1
        if north and ne:count += 1
        if south and nw:count += 1
        if south and ne:count += 1

    return count

def calculate_price_1(points):
    return len(points) * count_borders(points)


def p1():
    farm = get_input()
    regions = get_regions(farm)
    price = 0
    for name in regions:
        for region in regions[name]:
            price += calculate_price_1(region)
            print(region)

    print(price)


def p2():
    farm = get_input()
    regions = get_regions(farm)
    price = 0
    for name in regions:
        for region in regions[name]:
            # print("region:", name, ": ", count_corners(region))
            price += count_corners(region) * len(region)
    print(price)


if __name__ == "__main__":
    p1()
    p2()
