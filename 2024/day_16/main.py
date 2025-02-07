import time


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        n = Node(value)
        if self.tail:
            self.tail.next = n
            self.tail = n
        else:
            self.head = n
            self.tail = n

    def dequeue(self):
        old = self.head
        self.head = self.head.next
        if self.head:
            old.next = None
        else:
            self.tail = None
        return old.value

    def print(self):
        el = self.head
        while el:
            print(el.value)
            el = el.next
        print("")


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def read_graph():
    with open("2024/day_16/input.txt", "r") as file:
        graph = {}
        for i, row in enumerate(file):
            for j, col in enumerate(row.strip()):
                if col != "#":
                    graph[(j, i)] = col
    return graph


# start len graph - 2, 1
# enqueue start, (1, 0), 0
# while queue:
# doloci smeri (naprej, levo, desno) in ceno (1, 1001, 1001)
# ce nova tocka ali obstoječa z višjo ceno: zapiši novo ceno, dodaj v queue


def bfs(graph):
    q = Queue()
    endpoints = {val: pos for pos, val in graph.items() if val in ["S", "E"]}
    graph[endpoints["S"]] = 0
    q.enqueue((endpoints["S"], (1, 0), 0))
    while q.head is not None:
        ((cx, cy), (dx, dy), c) = q.dequeue()
        new = [
            ((cx + d[0], cy + d[1]), d, c + 1 + 1000 * (1 - (dx * d[0] + dy * d[1])))
            for d in DIRECTIONS
            if (dx * d[0] + dy * d[1]) != -1
        ]

        for n in new:
            (pos, _, cost) = n
            if val := graph.get(pos):
                if isinstance(val, int) and val > cost or val in [".", "E"]:
                    graph[pos] = cost
                    q.enqueue(n)

    return graph[endpoints["E"]]


def find_paths(maze: dict, start: tuple, end: tuple, path_cost: int):
    paths = []
    maze[start][(1, 0)] = 0


    def dfs(maze: dict, point: tuple, direction: tuple, path: dict):
        nonlocal paths, path_cost
        if point in path:
            return
        cost = maze[point][direction]
        new_path = path | {point}
        if cost > path_cost:
            return 
        
        if point == end:
            if cost < path_cost:
                path_cost = cost
                paths = [new_path]
            elif cost == path_cost:
                paths.append(new_path)
            return

        (cx, cy), (dx, dy) = point, direction
        for d in DIRECTIONS:
            sp = dx * d[0] + dy * d[1]
            if sp == -1:
                continue
            n = (cx + d[0], cy + d[1])
            c = 1 + (1 - sp) * 1000
            if n not in maze:
                continue
            new_cost = cost + c
            if new_cost <= maze[n][d]:
                maze[n][d] = new_cost
                # print(point)
                dfs(maze, n, d, new_path)

    dfs(maze, start, (1, 0), set())

    return paths


def p1():
    st = time.time()
    graph = read_graph()
    print(bfs(graph))
    et = time.time()
    print(et - st)


def p2():
    st = time.time()
    graph = read_graph()
    min_cost = bfs(graph)
    graph = read_graph()
    endpoints = {val: pos for pos, val in graph.items() if val in ["S", "E"]}
    for n in graph:
        graph[n] = {d: float("inf") for d in DIRECTIONS}
    paths = find_paths(graph, endpoints["S"], endpoints["E"], min_cost)
    unique_points = set.union(*paths)
    print(len(unique_points))
    et = time.time()
    print(et - st)


if __name__ == "__main__":
    p1()
    p2()
