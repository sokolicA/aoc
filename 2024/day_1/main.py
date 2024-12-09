import os


DIR = os.path.dirname(__file__)


def main():
    left = []
    right = []
    with open(os.path.join(DIR, "input.txt")) as f:
        rows = f.readlines()
        for row in rows:
            l, r = row.split("   ")
            left.append(int(l))
            right.append(int(r))
    
    left.sort()
    right.sort()
    diff = 0
    
    for idx in range(len(left)):
        diff += abs(left[idx]-right[idx])
    print("Part 1:", diff)

    similiarity=0
    ir = 0
    print(left[1:10])
    print(right[1:10])
    for il in range(len(left)):
        count = 0
        while ir < len(right):
            if left[il] == right[ir]:
                count += 1
                ir += 1
            elif left[il] < right[ir]:
                break
            else:
                ir += 1
        similiarity += left[il] * count
        
    print("Part 2:", similiarity)
        


if __name__=="__main__":
    main()