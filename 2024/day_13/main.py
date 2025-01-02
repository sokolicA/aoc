def get_input():
    with open("2024/day_13/input.txt") as file:
        result = []
        for i, line in enumerate(file):
            line = line.strip()
            if i % 4 == 0:
                game = dict()
                game["A"] = (int(line[12:14]), int(line[-2:]))
            elif i % 4 == 1:
                game["B"] = (int(line[12:14]), int(line[-2:]))
            elif i % 4 == 2:
                game["point"] = (
                    int(line[line.find("X=") + 2 : line.find(",")]),
                    int(line[line.find("Y=") + 2 :]),
                )
                result.append(game)
            else:
                ...
        return result


def calculate_cost(game):
    start_b = min(
        [game["point"][0] // game["B"][0], game["point"][1] // game["B"][1], 100]
    )
    # print(start_b)
    for b in range(start_b, -1, -1):
        dx = game["point"][0] - b * game["B"][0]
        dy = game["point"][1] - b * game["B"][1]
        a = 1
        while a <= 100:
            if (dx - (game["A"][0] * a)) == (dy - (game["A"][1] * a)) == 0:
                # return (a, b)
                return a * 3 + b
            if dx < 0 or dy < 0:
                break
            a += 1
    return 0


def solve_system_2_equations(eq1, eq2):
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2

    denom = a1 * b2 - b1 * a2
    if denom == 0:
        return None

    x = (c1 * b2 - b1 * c2) / (a1 * b2 - b1 * a2)
    y = (a1 * c2 - c1 * a2) / (a1 * b2 - b1 * a2)

    return x, y


def p1():
    games = get_input()
    cost = 0
    for game in games:
        cost += calculate_cost(game)

    print(cost)


def p2():
    games = get_input()
    cost = 0
    for game in games:
        eq1 = game["A"][0], game["B"][0], game["point"][0] + 10000000000000
        eq2 = game["A"][1], game["B"][1], game["point"][1] + 10000000000000
        a, b = solve_system_2_equations(eq1, eq2)
        if a.is_integer() and b.is_integer():
            cost += 3 * int(a) + int(b)
    print(cost)


if __name__ == "__main__":
    p1()
    p2()
