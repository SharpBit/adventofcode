import itertools

from utils import timed, read_lines

tiles = [tuple(int(i) for i in line.split(',')) for line in read_lines('day09.txt')]

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def rect_edges(p1, p2):
    return (
        (p1, (p1[0], p2[1])),
        ((p1[0], p2[1]), p2),
        (p2, (p2[0], p1[1])),
        ((p2[0], p1[1]), p1)
    )

def is_on_edge(point, u, v):
    '''Returns True if point is on edge (u, v)'''
    px, py = point
    min_x = min(u[0], v[0])
    max_x = max(u[0], v[0])
    min_y = min(u[1], v[1])
    max_y = max(u[1], v[1])
    return ((px == min_x == max_x) and (min_y <= py <= max_y)) or (py == min_y == max_y) and (min_x <= px <= max_x)

def is_point_in_polygon(point, edges):
    '''Determines if a point is inside a polygon using the ray casting algorithm'''
    x, y = point
    inside = False

    for (u, v) in edges:
        if is_on_edge(point, u, v):
            return True

        xi, yi = u
        xj, yj = v
        
        # Check for intersection between the ray (extending right from point) and edge (u, v)
        
        # Check if the edge straddles the horizontal line at y (one vertex is above y, the other is below)
        #                (xi, yi)
        #                   |
        #       (x, y)      |
        #                   |
        #                (xj, yj)
        intersect_y = ((yi > y) != (yj > y))

        if intersect_y:
            # Check if the intersection point is strictly to the right of point.x
            # Formula calculates the x-coordinate where the edge crosses horizontal line y
            intersect_x = (xj - xi) * (y - yi) / (yj - yi) + xi

            # Starts with False
            # an even number of intersections will result in False
            # an odd number of intersections will result in True (point is within the polygon)
            if x < intersect_x:
                inside = not inside
        
    return inside

def check_intersect(e, edges):
    '''Checks for a perpendicular intersect. Does not count if they intersect at a vertex.'''
    for f in edges:
        if (f[0][0] == f[1][0] and e[0][0] == e[1][0]) or \
            (f[0][1] == f[1][1] and e[0][1] == e[1][1]):
            # lines are parallel
            continue

        # f = (0,0),  (5,0)
        # e = (2,-3), (2,3)
        min_fx = min(f[0][0], f[1][0])
        max_fx = max(f[0][0], f[1][0])
        min_ey = min(e[0][1], e[1][1])
        max_ey = max(e[0][1], e[1][1])
        if (min_fx < e[0][0] < max_fx) and (min_ey < f[0][1] < max_ey):
            return True

        # f = (2,-3), (2,3)
        # e = (0,0),  (5,0)
        min_ex = min(e[0][0], e[1][0])
        max_ex = max(e[0][0], e[1][0])
        min_fy = min(f[0][1], f[1][1])
        max_fy = max(f[0][1], f[1][1])
        if (min_fy < e[0][1] < max_fy) and (min_ex < f[0][0] < max_ex):
            return True

    return False

@timed
def part_one():
    areas = [(area(p1, p2), p1, p2) for p1, p2 in itertools.combinations(tiles, 2)]
    return max(areas)[0]

@timed
def part_two():
    edges = [(tiles[i - 1], tiles[i]) for i in range(len(tiles))]
    areas = []
    for p1, p2 in itertools.combinations(tiles, 2):
        other_verts = ((p1[0], p2[1]), (p2[0], p1[1]))
        if not all(is_point_in_polygon(v, edges) for v in other_verts):
            # At least one corner of the rectangle is outside the polygon
            continue

        min_x = min(p1[0], p2[0])
        max_x = max(p1[0], p2[0])
        min_y = min(p1[1], p2[1])
        max_y = max(p1[1], p2[1])
        # Check if any vertex in polygon P is fully within the rectangle formed by p1, p2
        if any((min_x < v[0] < max_x) and (min_y < v[1] < max_y) for v in tiles):
            continue

        # Check if any of the rectangle's edges intersect(cross) the polygon's edges (like an X)
        if any(check_intersect(e, edges) for e in rect_edges(p1, p2)):
            continue

        areas.append((area(p1, p2), p1, p2))
    return max(areas)[0]

print(part_one())
print(part_two())
