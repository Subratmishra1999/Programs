p = [(i, j)[::k] for i in (1, -1) for j in (2, -2) for k in (-1, 1)]
print(p)
i, j, n = map(int, input().split())
d = {(i, j)}
for _ in range(n):
    t = set()
    for i, j in d:
        print(d)
        for dx, dy in p:
            x, y = i + dx, j + dy
            if n >= x >= 1 <= y <= n:
                t.add((x, y))
    d = t
print(len(d),d)