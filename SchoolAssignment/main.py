

import sys
#import resource
from sys import argv

#resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
#sys.setrecursionlimit(0x100000)


def load(file):
    with open(file+".txt") as f:
        data = f.readlines()
    res = []
    for row in data:
        res.append([])
        for element in row:
            if element != "\n" and element != " ":
                res[-1].append(element)

    return res


def findLargest(data):
    visited = []
    area = []
    length = 0
    movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def recScan(x, y, scanArea):
        visited.append((x, y))
        scanArea.append((x, y))

        for dx, dy in movement:
            newX, newY = x + dx, y + dy
            if newX >= 0 and newY >= 0 and newX < len(data) and newY < len(data[newX]):
                if data[x][y] == data[newX][newY] and (not (newX, newY) in visited):
                    recScan(newX, newY, scanArea)
        return scanArea

    for x in range(len(data)):
        for y in range(len(data[x])):
            if (x, y) not in visited:
                newArea = recScan(x, y, [])
                if len(newArea) > length:
                    length = len(newArea)
                    area = newArea
    return length




if __name__ == '__main__':
    for file in argv[1:]:
        data = load(file)
        print(findLargest(data))



