import math 
import random
import numpy
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

def findSSE(centroids, cluster1, cluster2, cluster3):
    sse = 0
    for obj in cluster1:
        sse += findSquaredDistance(obj, centroids[0])
    for obj in cluster2:
        sse += findSquaredDistance(obj, centroids[1])
    for obj in cluster3:
        sse += findSquaredDistance(obj, centroids[2])
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

# initialise clusters
cluster1 = []
cluster2 = []
cluster3 = []

#loop till clusering is success
while True:

    #initialise variables
    sseValues = []
    flag = "all_good"
    i = 0

    # initialize centroid values with random data points
    cent =  numpy.array(random.sample(dataSet, 3))

    #loop till final clusters are found i.e., till means are the same
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
            flag == "empty_cluster"
            break

        newCent = numpy.array([findMean(cluster1), findMean(cluster2), findMean(cluster3)])
        compare = cent == newCent

        #break of means remain the same => final clustering found
        if compare.all() and i >= 150:
            break
        else:
            cent = numpy.delete(cent,[0,1,2],0)
            cent = newCent

        newSSE = findSSE(cent, cluster1, cluster2, cluster3)
        sseValues.append(newSSE)
        i += 1

    if(flag == "all_good"):
        break

# add the final clusters into a dictionary
clusters = {}
clusters["cluster1"] = cluster1
clusters["cluster2"] = cluster2
clusters["cluster3"] = cluster3

# print the final clusters
for cluster in clusters:
    print(cluster)
    print(clusters[cluster])

# plot the graphs
gtk.plot3DGraph(clusters)
gtk.plot4DGraph(clusters)
gtk.plotSSEGraph(sseValues)
gtk.plot2DGraph(clusters)