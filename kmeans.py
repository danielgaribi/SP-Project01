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

def kmean(pointArray, K, MAXITER):
    DVECTOR = len(pointArray[0]) 
    N = len(pointArray)
    centroids = [pointArray[index] for index in range(K)]

    for Iter in range(MAXITER):
        newCentroids = computeClaster(K, N, DVECTOR, centroids, pointArray)
        if (isArraysEquel(centroids, newCentroids)):
            break
        centroids = newCentroids
    return centroids

def computeClaster(K, N, DVECTOR, centroids, pointArray): 
    clusterArr = [[] for index in range(K)] 
    for pointIndex in range(N): 
        closestIndex = 0
        closestDist = 0
        for clusterIndex in range(K):
            currDist = computeDist(centroids[clusterIndex], pointArray[pointIndex], DVector)
            if (currDist < closestDist): 
                closestIndex = clusterIndex
                closestDist = currDist
        clusterArr[closestIndex] = pointArray[pointIndex]
    
    newCentroids = []
    for i in range(K): 
        newCentroids.append(sum(clusterArr[K]) / len(clusterArr[K]))
    return newCentroids

def computeDist(point1, point2, DVector): 
    dist = 0
    for i in range(0:DVector): 
        dist += pow(point1[i] - point2[i],2)
    return dist

def isArraysEquel(centroids, newCentroids) # centroids = [[],[],[]]
    return false

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
