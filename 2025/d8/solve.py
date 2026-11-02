# read lines into tuples. dict tuples: None (za shranit krog)
# f calc dist
# greš skozi vse točke. Če je že v krogu pustiš. Sicer poiščeš najkrajšo razdaljo. Če sosed ni v krogu ustvariš novega, sicer dodaš nov krog


def read_file(filepath: str) -> dict:
    with open(filepath, "r") as f:
        lines = f.readlines()

    return {tuple(int(x) for x in line.split(",")): None for line in lines}


def calculate_dist(p1: tuple, p2: tuple) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** (
        1 / 2
    )


def closest_point(p1: tuple, p2: list[tuple]) -> tuple:
    m = 99999999999
    t = ()
    for p in p2:
        if p != p1:
            d = calculate_dist(p, p1)
            print(p, p1, d)
            if d < m:
                m = d
                t = p
    return t


def closest_points(points: list[tuple]) -> list[tuple]:
    m = 999999999
    closest = []
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            d = calculate_dist(points[i], points[j])
            if d < m:
                m = d
                closest = [points[i], points[j]]

    return closest


def distances(points: list[tuple]) -> dict:
    dist = {}
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            dist[(points[i], points[j])] = calculate_dist(points[i], points[j])
    return dist


def solve_p1(filepath: str) -> int:
    podatki = read_file(filepath)
    tocke = [x for x in podatki.keys()]
    skupaj = [(k, v) for k, v in distances(tocke).items()]
    urejeni = sorted(skupaj, key=lambda x: x[1])
    krogi = {}
    # for par in urejeni[:1000]:
    for par in urejeni:
        p1 = par[0][0]
        p2 = par[0][1]
        k1 = podatki[p1]
        k2 = podatki[p2]
        if k1 is None and k2 is None:  # oba nista v krogu
            nasl = max(int(x) for x in krogi.keys() or "0") + 1
            n = str(nasl)
            krogi[n] = [p1, p2]
            podatki[p1] = n
            podatki[p2] = n
            continue

        if k1 is not None and k2 is not None:  # oba sta v krogu
            if k1 == k2:
                continue
            krogi[k1].extend(krogi[k2])
            for p in krogi[k2]:
                podatki[p] = k1
            del krogi[k2]
        elif k1:
            podatki[p2] = k1
            krogi[k1].append(p2)
        else:
            podatki[p1] = k2
            krogi[k2].append(p1)

        if len(krogi.get(k1, [])) == len(tocke) or len(krogi.get(k2, [])) == len(tocke):
            print(f"Vsi v enem krogu. Rezultat: {p1[0] * p2[0]}")

    # print(krogi)
    # sor = sorted(list(krogi.values()), key=lambda x: -len(x))
    # return len(sor[0]) * len(sor[1]) * len(sor[2])


def solve_p2(filepath: str) -> int: ...


if __name__ == "__main__":
    print(solve_p1("2025/d8/p1.txt"))
