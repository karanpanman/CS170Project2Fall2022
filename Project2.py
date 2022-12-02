import numpy as np
import random as rd
#kannon = np.array([2,4,6])
#print(kannon)
#Calculates the distance between 2 rows


def calculate_euclideanDistance(row1, row2, current_set):
    distance = .0
    for num in len(row1):
        if num not in current_set:
            row1[num] = 0
            row2[num] = 0
    for i in range(1, len(row1)):
        distance = distance + pow(row1[i] - row2[i],2)
    distance = np.sqrt(distance)
    return distance

#Make an list of the data and find closest neighbors
def find_Neighbors(data, current_set, feature_to_add):
    distanceList = []
    neighborList = []
    numCount = 0
    #print("Testing Row: ", currDataRow)
    for dataRow in data:
        eDistance = calculate_euclideanDistance(currDataRow, dataRow, current_set)
        #We want to make distanceList contain tuple with original row and euclid distance
        distanceList.append((dataRow, eDistance))
    distanceList.sort(key = lambda a : a[1])
    neighborList = distanceList[1:num+1]
    for i in range(num):
        if neighborList[i][0][0] == 1:
            numCount = numCount - 1
        else:
            numCount = numCount + 1
    if numCount < 0:
        guessVal = 1
    else:
        guessVal = 2

    print("Full Distance List: ", distanceList)
    print("Full Neighbors List: ", neighborList)
    print("Expected: ", guessVal)
    print("Actual: ", distanceList[0][0][0])

def calculateProbability(data, currentSet):
    totalNum = data.size/data[1].size

def leave_one_out_cross_validation(data, current_set, feature_to_add):
    number_correctly_classified = 0
    for i in range(len(data)):
        object_to_classify = data[i][1:]
        label_object_to_classify = data[i][0]
        #print("Row: ", object_to_classify)
        #print("Objects to classify", label_object_to_classify)
        nearest_neighbor_distance = 999
        nearest_neighbor_location = 999
        print("Looping over i, at the " + str(i) + " location")
        print("The "+ str(i) + "th object is in class " + str(label_object_to_classify))
        for j in range(len(data)):
            if j != i:
                dist = calculate_euclideanDistance(object_to_classify, data[j][1:], current_set)
                
    return rd.random()%100


def feature_search_demo(data):
    current_set = []

    for i in range (1,len(data[0])):
        print("On the " + str(i) + "th level of the search tree")
        feature_to_add_on_this_level = 0
        best_accuracy_so_far = 0

        for j in range (1,len(data[0])):
            if j not in current_set:
                print("--Considering adding the " + str(j) + " feature")
                accuracy = leave_one_out_cross_validation(data, current_set, j)
        
            if accuracy > best_accuracy_so_far:
                best_accuracy_so_far = accuracy
                feature_to_add_on_this_level = j

        print("On level " + str(i) + ", I added feature " + str(feature_to_add_on_this_level) + " to current set\n")
        current_set.append(feature_to_add_on_this_level)


print("Testing Output")
data = np.loadtxt('CS170_Small_Data__48.txt')
#print(data[])
current_set = []
numOfFeatures = data[1].size - 1

dataset = [[0,4,8],
	[0,10,5],
    [0, 5, 9],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]

dataset1 = [[2,4,8],
	[2,10,5],
    [1, 5, 9],
    [2, 3, 7],
    [1, 142, 8]]

leave_one_out_cross_validation(data, 0, 0)

"""
row0 = dataset1[0]
#for row in dataset:
	#distance = calculate_euclideanDistance(row0, row)
	#print(distance)
print(numOfFeatures)
find_Neighbors(dataset1, row0, 3)
#print(data.size/data[0].size)
feature_search_demo(data)
"""
