def generateNSizedGraph(n):
    if n <= 2:
        # do something special for board sizes 2 and 1
        pass

    graph = [[] for i in range(getSmallestCellNumber(n))]

    graph[0] = [1, 2, 3, 4, 8]
    graph[1] = [0, 2, 4, 5, 6]
    graph[2] = [0, 1, 6, 7, 8]

    depth = 3
    while (depth <= n):
        # Original Cells:
        smallest = getSmallestCellNumber(depth - 1)
        biggest = getSmallestCellNumber(depth)
        for i in range(smallest, biggest):
            if i != biggest - 1:
                graph[i].append(i + 1)
            else:
                graph[i].append(smallest)

            if i != smallest:
                graph[i].append(i - 1)
            else:
                graph[i].append(biggest - 1)

            if isCorner(i, depth - 1) and depth != n:
                cornerNum = cornerNumber(i, depth - 1)
                nextCorner = getCorner(cornerNum, depth)
                graph[i].append(nextCorner)
                graph[i].append(nextCorner + 1)
                if nextCorner == biggest:
                    graph[i].append(getSmallestCellNumber(depth + 1) - 1)
                else:
                    graph[i].append(nextCorner - 1)
            elif depth != n:
                c = cornerNumber(lastCorner(i, depth - 1), depth - 1)
                multiple = (depth - 1) * 3
                graph[i].append(i + multiple + c)
                graph[i].append(i + multiple + c + 1)

        depth += 1

    graph = pairUpGraph(graph)
    return graph

def pairUpGraph(graph):
    g = graph[:]
    for i in range(len(g)):
        for j in range(len(g[i])):
            res = g[i][j]
            if not i in g[res]:
                g[res].append(i)
        g[i].sort()
    return g

def getSmallestCellNumber(n):
    return int(3 * (n - 1) * n/2)


def isCorner(x, depth):
    smallestCell = getSmallestCellNumber(depth)
    if x == smallestCell:
        return True
    if x == smallestCell + depth:
        return True
    if x == smallestCell + depth * 2:
        return True
    return False


def cornerNumber(x, depth):
    smallestCell = getSmallestCellNumber(depth)
    if x == smallestCell:
        return 0
    if x == smallestCell + depth:
        return 1
    if x == smallestCell + depth * 2:
        return 2


def getCorner(num, depth):
    smallestCell = getSmallestCellNumber(depth)
    return smallestCell + depth * num

def lastCorner(x, depth):
    first = getCorner(0, depth)
    second = getCorner(1, depth)
    third = getCorner(2, depth)
    if x < second: return first
    if x < third: return second
    return third

