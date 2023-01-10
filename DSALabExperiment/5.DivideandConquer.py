import math

def cross_product(p1, p2, p3):
    x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
    x2, y2 = p3[0] - p1[0], p3[1] - p1[1]
    return x1 * y2 - x2 * y1

def find_hull(points, start, end):
    if start == end:
        return []
    elif start + 1 == end:
        return [points[start], points[end]]

    mid = (start + end) // 2
    left_hull = find_hull(points, start, mid)
    right_hull = find_hull(points, mid, end)

    return merge_hulls(left_hull, right_hull)

def merge_hulls(left_hull, right_hull):
    n, m = len(left_hull), len(right_hull)
    i = 0
    j = 0
    lower_hull = []
    while i < n and j < m:
        if left_hull[i][0] < right_hull[j][0]:
            lower_hull.append(left_hull[i])
            i += 1
        else:
            lower_hull.append(right_hull[j])
            j += 1

    while i < n:
        lower_hull.append(left_hull[i])
        i += 1
    while j < m:
        lower_hull.append(right_hull[j])
        j += 1

    upper_hull = []
    i = j = 0
    while i < n and j < m:
        if left_hull[i][0] < right_hull[j][0]:
            upper_hull.append(left_hull[i])
            i += 1
        else:
            upper_hull.append(right_hull[j])
            j += 1
    while i < n:
        upper_hull.append(left_hull[i])
        i += 1
    while j < m:
        upper_hull.append(right_hull[j])
        j += 1

    upper_hull.reverse()
    hull = lower_hull + upper_hull[1:-1]
    return hull

points = [(0, 0), (0, 4), (-9, 0), (5, 0), (0, -9), (1, 0)]
points.sort()
convex_hull = find_hull(points, 0, len(points) - 1)

print("The Convex Hull is: ", convex_hull)