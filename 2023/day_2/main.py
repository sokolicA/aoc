import re


def main():
    with open("2023/day_2/input.txt") as f:
        result = 0
        for line in f:
            line = line.rstrip()
            game, samples = line.split(":")
            game = int(re.sub("Game ", "", game))
            samples = samples.split("; ")
            print(samples)
            max_red = 1
            max_green = 1
            max_blue = 1
            # max_red = 0
            # max_green = 0
            # max_blue = 0
            for sample in samples:
                print(sample)
                pattern = re.compile(r"(\d+)\s+(\w+)")
                matches = pattern.findall(sample)
                for m in matches:
                    print(m)
                    if m[1] == "red" and int(m[0]) > max_red:
                        max_red = int(m[0])
                    if m[1] == "green" and int(m[0]) > max_green:
                        max_green = int(m[0])
                    if m[1] == "blue" and int(m[0]) > max_blue:
                        max_blue = int(m[0])
            # if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            #     result += game
            result += max_red * max_green * max_blue
    print(result)


if __name__ == "__main__":
    main()
