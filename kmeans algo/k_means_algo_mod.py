import math 
import numpy
import random
import graphToolKit as gtk

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

def findCluster(obj1, cent1, cent2, cent3):
    distances = []
    distances.append(findDistance(obj1, cent1))
    distances.append(findDistance(obj1, cent2))
    distances.append(findDistance(obj1, cent3))
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
    for i in range(3):
        for obj in clusters["cluster" + str(i + 1)]:
            sse += findSquaredDistance(obj, centroids[i])
    return sse

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

finalClusters = {}
minimalSSE = 0
sseValues = []

for i in range(200):
    # initialize centroid values
    cent =  numpy.array(random.sample(dataSet, 3))
    # print(cent)
    flag = "all_good"
    cluster1 = []
    cluster2 = []
    cluster3 = []

    while True:
        cluster1.clear()
        cluster2.clear()
        cluster3.clear()
        for obj in dataSet:
            cluster = findCluster(obj, cent[0], cent[1], cent[2])
            if cluster == 1:
                cluster1.append(obj)
            elif cluster == 2:
                cluster2.append(obj)
            else:
                cluster3.append(obj)

        if len(cluster1) == 0 or len(cluster2) == 0 or len(cluster3) == 0:
            flag = "empty_cluster"
            break

        newCent = numpy.array([findMean(cluster1), findMean(cluster2), findMean(cluster3)])

        compare = cent == newCent

        if compare.all() :
            break
        else:
        
            cent = numpy.delete(cent,[0,1,2],0)
            cent = newCent

    if flag == "empty_cluster":
        print("invalid clustering...iteration skipped!")
        continue

    # print("iteration: " + str(i))
    clusters = {}
    clusters["cluster1"] = cluster1
    clusters["cluster2"] = cluster2
    clusters["cluster3"] = cluster3

    newSSE = findSSE(cent, clusters)
    sseValues.append(newSSE)
    # print(newSSE)

    if newSSE < minimalSSE or i == 0:
        minimalSSE = newSSE
        finalClusters.clear()
        for cluster in clusters:
            finalClusters.update({cluster : clusters[cluster]})


print("minimal SSE = " + str(minimalSSE))
for cluster in finalClusters:
        print(cluster)
        print(finalClusters[cluster])

# gtk.plot3DGraph(clusters)
# gtk.plot4DGraph(clusters)
gtk.plotSSEGraph(sseValues)
# gtk.plot2DGraph(clusters)