import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy


def plot4DGraph(clusters):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    iter = 0
    for cluster in clusters:
        u_val = [obj[0] for obj in clusters[cluster]]
        v_val = [obj[1] for obj in clusters[cluster]]
        w_val = [obj[2] for obj in clusters[cluster]]
        x_val = [obj[3] for obj in clusters[cluster]]

        if iter == 0:
            img1 = ax.scatter(u_val, v_val, w_val, s = 75, c = x_val, cmap = plt.winter(), label = 'cluster1')
            cbar = fig.colorbar(img1, shrink = 0.5, aspect = 10)
        elif iter == 1:
            img2 = ax.scatter(u_val, v_val, w_val, s = 75, c = x_val, cmap = plt.spring(), label = 'cluster2')
            cbar = fig.colorbar(img2, shrink = 0.5, aspect = 10)
        else:
            img3 = ax.scatter(u_val, v_val, w_val, s = 75, c = x_val, cmap = plt.gray(), label = 'cluster3')
            cbar = fig.colorbar(img3, shrink = 0.5, aspect = 10)
        
        iter += 1
        cbar.ax.get_yaxis().labelpad = 15
        cbar.ax.set_ylabel('petal width in cm')
        cbar.ax.get_xaxis().labelpad = 15
        cbar.ax.set_xlabel('cluster' + str(iter))

    ax.set_xlabel('sepal length in cm', rotation=150)
    ax.set_ylabel('sepal width in cm')
    ax.set_zlabel(r'petal length in cm', rotation=60)

    
    plt.title("4D representation of clustering solution")
    plt.show()

def plot3DGraph(clusters):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colorArray = ['red', 'green', 'blue']
    iter = 0

    for cluster in clusters:
        u_val = [obj[0] for obj in clusters[cluster]]
        v_val = [obj[1] for obj in clusters[cluster]]
        w_val = [obj[2] for obj in clusters[cluster]]

        ax.scatter(u_val, v_val, w_val, s = 75, c = colorArray[iter], label = 'cluster' + str(iter + 1))
        iter += 1

    plt.legend()
    ax.set_xlabel('sepal length in cm', fontsize=13, rotation=150)
    ax.set_ylabel('sepal width in cm', fontsize=13)
    ax.set_zlabel(r'petal length in cm', fontsize=13, rotation=60)
    plt.title("3D representation of clustering solution")
    plt.show()

def plotSSEGraph(sseValues):

    x_val = numpy.arange(1,151,1)
    y_val = sseValues
    plt.plot(x_val, y_val)
    plt.scatter(x_val, y_val, c = "red", marker= '+', label = "sse value")

    plt.xlabel("iteration")
    plt.ylabel("SSE values")
    plt.title("iteration vs SSE values")
    plt.grid()
    plt.legend()
    plt.show()

def plot2DGraph(clusters):

    colorArray = ['red', 'green', 'blue']
    attributes = ["sepal length", "sepal width", "petal length", "petal width"]
    for i in range(0,3,2):
        iter = 0
        for cluster in clusters:
            u_val = [obj[0 + i] for obj in clusters[cluster]]
            v_val = [obj[1 + i] for obj in clusters[cluster]]

            plt.scatter(u_val, v_val, s = 50, c = colorArray[iter], label = "cluster" + str(iter + 1))
            iter += 1

        # plt.grid()
        plt.xlabel(attributes[0 + i] + "(cm)", fontsize = 15)
        plt.ylabel(attributes[1 + i] + "(cm)", fontsize = 15)
        plt.title(attributes[0 + i] + " vs " + attributes[1 + i] + " of clusters", fontsize = 20)
        plt.show()

