import math 
import numpy

def findDistance(obj1, obj2):
    distance = 0
    for i in range(len(obj1)):
        distance += (obj1[i] - obj2[i])**2
    return math.sqrt(distance)

def findCluster(obj1, cent1, cent2, cent3):
    distances = []
    distances.append(findDistance(obj1, cent1))
    distances.append(findDistance(obj1, cent2))
    distances.append(findDistance(obj1, cent3))
    return distances.index(min(distances)) + 1

def findMean(cluster):
    xval = yval = 0
    for obj in cluster:
        xval += obj[0]
        yval += obj[1]
    size = len(cluster)
    return [(xval/size), (yval/size)]

# taking input from file
dataSet = []
dataFile = open("dataSet1.txt", "r")
for line in dataFile:
    obj = list(map(int, line.strip().split(",")))
    dataSet.append(obj)

# initialize centroid values
cent =  numpy.array([[2,10],[5,8],[1,2]])

cluster1 = []
cluster2 = []
cluster3 = []
i = 1

while True:
    flag = 0
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

    newCent = numpy.array([findMean(cluster1), findMean(cluster2), findMean(cluster3)])

    compare = cent == newCent

    if compare.all() :
        break
    else:
   
        cent = numpy.delete(cent,[0,1,2],0)
        cent = newCent
        print("\niteration: " + (str)(i))
        print(cluster1)
        print(cluster2)
        print(cluster3)
        print("centroids: ")
        print(newCent)
        i += 1

print("\niteration: final")
print(cluster1)
print(cluster2)
print(cluster3)