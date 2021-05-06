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

def kmean(pointArray, k, MAXITER): 
    DVECTOR = len(pointArray[0]) 
    N = len(pointArray)
    centroids = [pointArray[index] for index in range(k)]

    for Iter in range(MAXITER):
        newCentroids = computeCluster(k, N, DVECTOR, centroids, pointArray)
        if (isArraysEquel(centroids, newCentroids, k, DVECTOR)):
            break
        centroids = newCentroids
    
    return centroids

def computeCluster(k, N, DVECTOR, centroids, pointArray): 
    clusterArr = [[] for index in range(k)] 
    for pointIndex in range(N): 
        minIndex = 0
        minDist = sys.maxsize
        for clusterIndex in range(k):
            currDist = computeDist(centroids[clusterIndex], pointArray[pointIndex], DVECTOR)
            if (currDist < minDist): 
                minDist = currDist
                minIndex = clusterIndex
        clusterArr[minIndex].append(pointArray[pointIndex]) 
    return computeNewCentroids(clusterArr, k, DVECTOR) 

def computeDist(point1, point2, DVector): 
    dist = 0
    for i in range(DVector): 
        dist += pow(point1[i] - point2[i],2)
    return dist

def computeNewCentroids(clusterArr, k, DVECTOR): 
    newCentroids = [] 
    for clusterIndex in range(k): 
        centroidK = []
        countPointsInClusterK = len(clusterArr[clusterIndex]) 
        for i in range(DVECTOR): 
            cordinateXi = 0
            for point in clusterArr[clusterIndex]:
                cordinateXi += point[i] 
            centroidK.append(cordinateXi / countPointsInClusterK)
        
        newCentroids.append(centroidK)
    return newCentroids
            

def isArraysEquel(centroids, newCentroids, k, DVECTOR):
    for centroinIndex in range(k):
        for Xi in range(DVECTOR):
            if (centroids[centroinIndex][Xi] != newCentroids[centroinIndex][Xi]):
                return False
    return True

def printOutput(centroids): 
    str = ""
    for i in range(len(centroids)): 
        for d in range(len(centroids[0])): 
            str += "{}".format(format(centroids[i][d], '.4f'))
            str += ","
        str = str[:-1] + "\n"
    
    print(str[:-1])

def main():
    k, max_iter = readArgs()
    pointsArray = readPointsFromFile()

    if (DEBUG_INPUT):
        print(f"k: {k}\nmax_iter: {max_iter}")
        print("points:")
        for point in pointsArray:
            print(point)

    centroids = kmean(pointsArray, k, max_iter)
    printOutput(centroids)

main()
