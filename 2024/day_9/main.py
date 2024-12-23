def read_input():
    with open("2024/day_9/input.txt", "r") as file:
        return file.readline().strip()


def extend_map(disk_map):
    extended_map = []
    for i in range(len(disk_map)):
        char = disk_map[i]
        times = int(char)
        if i % 2 == 0:
            extended_map += times * [str(i // 2)]
        else:
            extended_map += times * ["."]
    return extended_map


def parse_input(disk_map):
    disk = {"files": [], "space": []}
    pos = 0
    for i, length in enumerate(map(int, disk_map)):
        if length == 0:
            continue
        if i % 2 == 0:
            disk["files"].append((pos, length, i // 2))
        else:
            disk["space"].append((pos, length))
        pos += length
    return disk


def concat_map(m):
    result = ""
    for i in range(len(m)):
        result += m[i][0]
    return result


def switch(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr


def compact_disk(extended_map):
    l = 0
    r = len(extended_map) - 1
    while l < r:
        if extended_map[l] == ".":
            while extended_map[r] == "." and r > l:
                r -= 1
            switch(extended_map, l, r)
        l += 1
    return extended_map


def compact_disk_2(disk):
    for j in range(len(disk["files"]) - 1, 0, -1):
        f = disk["files"][j]
        for i in range(len(disk["space"])):
            s = disk["space"][i]
            if s[0] > f[0]:
                break
            if s[1] < f[1]:
                continue
            disk["files"][j] = (
                disk["space"][i][0],
                disk["files"][j][1],
                disk["files"][j][2],
            )
            disk["space"][i] = (
                disk["space"][i][0] + disk["files"][j][1],
                disk["space"][i][1] - disk["files"][j][1],
            )
            break
    return disk


def calculate_checksum(disk):
    result = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            result += i * int(disk[i])
    return result


def calculate_checksum_2(files):
    result = 0
    for i in range(len(files)):
        result += sum(
            files[i][2] * k for k in range(files[i][0], files[i][0] + files[i][1])
        )
    return result


def part_1():
    disk_map = read_input()
    extended_map = extend_map(disk_map)
    compact = compact_disk(extended_map)
    print(calculate_checksum(compact))


def part_2():
    disk_map = read_input()
    extended_map = parse_input(disk_map)
    compact = compact_disk_2(extended_map)
    print(calculate_checksum_2(compact["files"]))


if __name__ == "__main__":
    part_1()
    part_2()
