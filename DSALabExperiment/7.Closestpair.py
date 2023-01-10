import math

def closest_pair(points, n):
    if n <= 3:
        return brute_force(points, n)

    mid = n // 2
    mid_point = points[mid]
    dl = closest_pair(points[:mid], mid)
    dr = closest_pair(points[mid:], n - mid)
    d = min(dl, dr)

    strip = []
    for i in range(n):
        if abs(points[i][0] - mid_point[0]) < d:
            strip.append(points[i])

    return min(d, closest_strip(strip, len(strip), d))

def closest_strip(strip, size, d):
    strip.sort(key = lambda x: x[1])
    for i in range(size):
        for j in range(i+1, min(i + 8, size)):
            if (strip[j][1] - strip[i][1]) >= d:
                break
            d = min(d, dist(strip[i], strip[j]))
    return d

def brute_force(points, n):
    d = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            d = min(d, dist(points[i], points[j]))
    return d

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

points = [[1, 3], [15, 29], [30, 40], [5, 1], [12, 10], [2, 3]]
n = len(points)

print("Minimum distance: ", closest_pair(points, n))
