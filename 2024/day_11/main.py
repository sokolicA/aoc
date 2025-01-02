

def add_stone(d: dict, stone, n):
    if d.get(stone):
        d[stone] += n
    else:
        d[stone] = n
    return d

def get_input():
    with open("2024/day_11/input.txt") as file:
        stones =dict()
        for line in file:
            for x in line.strip().split(" "):
                add_stone(stones, int(x), 1)
    return stones


def number_of_digits(num):
    n = 1
    while num % 10**n != num:
        n += 1
    return n
    # return len(str(num))


def get_right_digits(num, n_digits):
    return num % 10**n_digits
    # return int(str(num)[n_digits:])


def get_left_digits(num, n_digits):
    while num >= 10**n_digits:
        num //= 10
    return num
    # return int(str(num)[:n_digits])



def transform_stone(stone):
    if stone == 0:
        result = [1]
    elif (n := number_of_digits(stone)) % 2 == 0:
        result = [
            get_left_digits(stone, n // 2),
            get_right_digits(stone, n // 2),
        ]
    else:
        result = [stone * 2024]
    return result


def blink(stones: dict):
    result = dict()
    for stone in stones:
        transf = transform_stone(stone)
        for s in transf:
            add_stone(result, s, stones[stone])
    return result
        
    

def p1():
    stones = get_input()
    blinks = 0
    while blinks < 75:
        stones = blink(stones)
        # print(stones)
        blinks += 1
    print(sum(n for n in stones.values()))


def p2(): ...


if __name__ == "__main__":
    p1()
    p2()

