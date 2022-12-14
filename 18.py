cubes = set()
nbr_pairs = 0

min_v = 1
max_v = 10

with open('18_input.txt', 'r') as f:
    for line in f.readlines():
        x,y,z = (int(a) for a in line.split(','))
        for k in (x, y, z):
            min_v = min(min_v, k)
            max_v = max(max_v, k)
        cubes.add((x,y,z))

        for delta in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            nbr = (x+delta[0], y+delta[1], z+delta[2])
            if nbr in cubes:
                nbr_pairs += 1

# part 1
print(6*len(cubes) - 2*nbr_pairs)

lower_bound = min_v - 1
upper_bound = max_v + 1


def get_nbrs(pos):
    x, y, z = pos
    nbrs = []
    for delta in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
        nbr = (x + delta[0], y + delta[1], z + delta[2])
        for k in nbr:
            if not (lower_bound <= k <= upper_bound):
                break
        else:
            nbrs.append(nbr)
    return nbrs

# dfs
def dfs(start):
    q = [start]
    closed_set = set()
    closed_set.add(start)

    while q:
        current = q.pop()

        for nbr in get_nbrs(current):
            if nbr in closed_set:
                continue
            if nbr in cubes:
                continue
            q.append(nbr)
            closed_set.add(nbr)

    return closed_set

# part 2
steam_cells = dfs((lower_bound, lower_bound, lower_bound))

result = 0
for cube in cubes:
    for nbr in get_nbrs(cube):
        if nbr in steam_cells:
            result += 1

print(result)