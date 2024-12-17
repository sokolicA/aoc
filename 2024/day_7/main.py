import itertools


def parse_input():
    data = []
    with open("2024/day_7/input.txt", "r") as file:
        for line in file:
            l, r = line.strip().split(": ")
            r = r.split(" ")
            data.append([l] + r)
    return data

def get_combinations(values, len):
    return list(itertools.product(values, repeat=len))

def part_1():
    equations = parse_input()
    OPERATORS = ["*", "+"]
    result = 0
    for eq in equations:
        left = eq[0]
        combinations = get_combinations(OPERATORS, len(eq[1:])-1)
        found = False
        for combination in combinations:
            if found:
                break
            current = eq[1]
            for i in range(len(combination)):
                tmp = current + combination[i] + eq[i+2]
                current = str(eval(tmp))
            
            if left == current:
                found = True
                result += int(left)
    print(result)

def part_2():
    equations = parse_input()
    OPERATORS = ["*", "+", ""]
    result = 0
    for eq in equations:
        left = eq[0]
        combinations = get_combinations(OPERATORS, len(eq[1:])-1)
        found = False
        for combination in combinations:
            if found:
                break
            current = eq[1]
            for i in range(len(combination)):
                tmp = current + combination[i] + eq[i+2]
                current = str(eval(tmp))
            
            if left == current:
                found = True
                result += int(left)
    print(result)




if __name__ == "__main__":
    part_1()
    part_2()