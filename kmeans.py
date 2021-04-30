

def readArgs():
    pass

def readPointsFromFile(filename):
    pass

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
