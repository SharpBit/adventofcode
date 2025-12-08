import heapq
import itertools
import math

from utils import timed, read_lines

points = [tuple(int(i) for i in line.split(',')) for line in read_lines('day08.txt')]

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.neighbors = set()

    @property
    def coords(self):
        return (self.x, self.y, self.z)
    
    def __repr__(self):
        return f'Point<{self.x}, {self.y}, {self.z}>'

def pair_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)


point_classes = {p: Point(*p) for p in points}

@timed
def part_one():
    distances = [(pair_distance(p1, p2), p1, p2) for p1, p2 in itertools.combinations(points, 2)]
    heapq.heapify(distances)
    for _ in range(1000):
        _, p1, p2 = heapq.heappop(distances)
        point_classes[p1].neighbors.add(p2)
        point_classes[p2].neighbors.add(p1)

    visited = set()
    circuit_sizes = []
    to_visit = set(point_classes.keys())

    def dfs(curr):
        nonlocal visited
        nonlocal to_visit
        visited.add(curr)
        if curr in to_visit:
            to_visit.remove(curr)

        for n in point_classes[curr].neighbors:
            if n not in visited:
                dfs(n)

    while to_visit:
        prev = len(visited)
        dfs(to_visit.pop())
        circuit_sizes.append(prev - len(visited))

    heapq.heapify(circuit_sizes)
    res = 1
    for _ in range(3):
        res *= -heapq.heappop(circuit_sizes)

    return res

@timed
def part_two():
    visited = set()

    start = points[0]
    visited.add(start)

    candidates = []
    mst_edges = []
    for p in points:
        if p is not start:
            heapq.heappush(candidates, (pair_distance(start, p), start, p))

    while candidates and len(visited) < len(points):
        dist, u, v = heapq.heappop(candidates)
        if v in visited:
            continue
        visited.add(v)
        mst_edges.append((dist, u, v))
        for p in points:
            if p not in visited:
                heapq.heappush(candidates, (pair_distance(v, p), v, p))

    _, u, v = max(mst_edges)
    return u[0] * v[0]

print(part_one())
print(part_two())
