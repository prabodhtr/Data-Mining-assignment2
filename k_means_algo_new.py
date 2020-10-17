import math 
import numpy
import random

def findDistance(obj1, obj2):
    distance = 0
    for i in range(len(obj1)):
        distance += (obj1[i] - obj2[i])**2
    return math.sqrt(distance)

def findSquaredDistance(obj1, obj2):
    distance = 0
    for i in range(len(obj1)):
        distance += (obj1[i] - obj2[i])**2
    return distance

def findCluster(obj1, cent1, cent2):
    distances = []
    distances.append(findDistance(obj1, cent1))
    distances.append(findDistance(obj1, cent2))
    return distances.index(min(distances)) + 1

def findMean(cluster):
    uval = wval = xval = yval = 0
    for obj in cluster:
        uval += obj[0]
        wval += obj[1]
        xval += obj[2]
        yval += obj[3]
    size = len(cluster)
    return [(uval/size), (wval/size), (xval/size), (yval/size)]

def findSSE(centroids, clusters):
    sse = 0
    for i in range(2):
        for obj in clusters["cluster" + str(i + 1)]:
            sse += findSquaredDistance(obj, centroids[i])
    return sse

def kMeansAlgo(bisectingCluster):
    finalClusters = {}
    minimalSSE = 0
    sseValues = []

    for i in range(50):
        # initialize centroid values for bisecting without repetition
        while True:
            cent =  numpy.array(random.sample(bisectingCluster, 2))
            if not numpy.array_equal(cent[0], cent[1]):
                break

        cluster1 = []
        cluster2 = []

        while True:
            cluster1.clear()
            cluster2.clear()
            for obj in bisectingCluster:
                cluster = findCluster(obj, cent[0], cent[1])
                if cluster == 1:
                    cluster1.append(obj)
                else:
                    cluster2.append(obj)

            newCent = numpy.array([findMean(cluster1), findMean(cluster2)])

            compare = cent == newCent

            if compare.all() :
                break
            else:
            
                cent = numpy.delete(cent,[0,1],0)
                cent = newCent

        # print("iteration: " + str(i))
        clusters = {}
        clusters["cluster1"] = cluster1
        clusters["cluster2"] = cluster2

        newSSE = findSSE(cent, clusters)

        if newSSE < minimalSSE or i == 0:
            minimalSSE = newSSE
            sseValues.append(newSSE)

            finalClusters.clear()
            finalClusters["cluster1"] = clusters["cluster1"]
            finalClusters["cluster2"] = clusters["cluster2"]
            finalClusters["cent1"] = list(cent[0])
            finalClusters["cent2"] = list(cent[1])
        else:
            sseValues.append(sseValues[-1])

    return finalClusters