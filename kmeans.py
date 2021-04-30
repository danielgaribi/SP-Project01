import sys

DEBUG_INPUT = False

def readArgs():
    assert(2 <= len(sys.argv) <= 3)

    try:
        k = int(sys.argv[1])
    except ValueError:
        print("K is not integer, exits...")
        exit(0)

    try:
        max_iter = 200 if len(sys.argv) == 2 else int(sys.argv[2])
    except ValueError:
        print("max_iter is not integer, exits...")
        exit(0)

    return k, max_iter

def readPointsFromFile():
    pointsArray = []
    while True:
        try:
            line = input()
            point = [float(n) for n in line.split(',')]
            pointsArray.append(point)
        except EOFError:
            break
    return pointsArray

def kmean(pointsArray, k, max_iter):
    pass

def main():
    k, max_iter = readArgs()
    pointsArray = readPointsFromFile()

    if (DEBUG_INPUT):
        print(f"k: {k}\nmax_iter: {max_iter}")
        print("points:")
        for point in pointsArray:
            print(point)

    kmean(pointsArray, k, max_iter)

main()
