import random
import math 
import numpy
import k_means_algo_new as km
import graphToolKit as gtk

def findSquaredDistance(obj1, obj2):
    distance = 0
    for i in range(len(obj1)):
        distance += (obj1[i] - obj2[i])**2
    return distance

def findSSE(clusterList, clusterListLen):
    sseList = findICD(clusterList, clusterListLen)
    # print(sseList)
    return sum(sseList)    

def findICD(clusterList, clusterListLen):
    sseList = []
    for i in range(clusterListLen):
        sse = 0
        centroid = clusterList["cent" + str(i + 1)]
        for obj in clusterList["cluster" + str(i + 1)]:
            sse += findSquaredDistance(obj, centroid)
        sseList.append(sse)
    return sseList

# taking input from file
dataSet = []
dataFile = open("iris.data", "r")
for line in dataFile:
    obj = []
    x = line.strip().split(",")
    for i in range(4):
        obj.append((float)(x[i]))
    dataSet.append(obj)
random.shuffle(dataSet)

# gtk.plot2DGraphOriginal(dataSet)

finalClusters = {}
minimalSSE = 0
sseValues = []

for i in range(500):
    clusterList = {}
    clusterListLen = 1
    clusterList["cluster1"] = dataSet

    while True:
        # cluster = random.randrange(clusterListLen) + 1
        if clusterListLen == 1:
            cluster = 1
        else:
            sseList = findICD(clusterList, 2)
            cluster = sseList.index(max(sseList)) + 1
        bisectingCluster = clusterList["cluster" + str(cluster)]

        # returns a dictionary with best clustering sln and their centroids
        # {
        # "cent1" : value1,
        # "cent2" : value2,
        # "cluster1": cluster1,
        # "cluster2": cluster2
        # }

        bisectedClusters = km.kMeansAlgo(bisectingCluster)

        # update the clusterList
        clusterListLen += 1
        clusterList["cluster" + str(cluster)] = bisectedClusters["cluster1"]
        clusterList["cent" + str(cluster)] = bisectedClusters["cent1"]
        clusterList["cluster" + str(clusterListLen)] = bisectedClusters["cluster2"]
        clusterList["cent" + str(clusterListLen)] = list(bisectedClusters["cent2"])

        if clusterListLen == 3:
            break

    newSSE = findSSE(clusterList, clusterListLen)

    if newSSE < minimalSSE or i == 0:
        minimalSSE = newSSE
        sseValues.append(newSSE)

        finalClusters["cluster1"] = clusterList["cluster1"]
        finalClusters["cluster2"] = clusterList["cluster2"]
        finalClusters["cluster3"] = clusterList["cluster3"]
    else:
        sseValues.append(sseValues[-1])

print("minimalSSE in bisecting k means= " + str(minimalSSE))
for cluster in finalClusters:
    print(cluster)
    print(finalClusters[cluster])

gtk.plotSSEGraphToCompare(sseValues, 500)
# gtk.plot4DGraph(finalClusters)
# gtk.plot3DGraph(finalClusters)
# gtk.plot2DGraph(finalClusters)
gtk.plotSSEGraph(sseValues, 500)