import numpy as np
import random as rd
import copy as dp

def calculate_euclideanDistance(row1, row2, current_set:list ):
    distance = .0
    #print("Feature List: ", current_set)
    #print("Row 1: ", row1)
    #print("Row 2: ", row2)
    for i in range(1,len(row1)+1):
        #print ("I value: ", i)
        if i in current_set:
            #print("Row 1 i: " + str(i) + "Row 1 at i = " + str(row1[i-1]))
            #print("Row 2 i: " + str(i) + "Row 2 at i = " + str(row2[i-1]))
            distance = distance + pow(row1[i-1] - row2[i-1],2)
    distance = np.sqrt(distance)
    return distance

#Make an list of the data and find closest neighbors
def find_Neighbors(data, current_set: list, feature_to_add):
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

def leave_one_out_cross_validation(data, current_set: list, feature_to_add):
    number_correctly_classified = 0
    print("Current Set looking like: ", current_set)
    feature_set = []
    for i in range(len(current_set)):
        feature_set.append(current_set[i])
    feature_set.append(feature_to_add)
    print("Feature Set to add looking like: ", feature_set)
    for i in range(len(data)):
        object_to_classify = data[i][1:]
        label_object_to_classify = data[i][0]
        nearest_neighbor_distance = 999
        nearest_neighbor_location = 999
        #print("Looping over i, at the " + str(i) + " location")
        #print("The "+ str(i) + "th object is in class " + str(label_object_to_classify))
        for j in range(len(data)):
            if j != i:
                dist = calculate_euclideanDistance(object_to_classify, data[j][1:], feature_set)
                #dist = np.sqrt(sum((object_to_classify - data[j][1:])**2))
                if dist < nearest_neighbor_distance:
                    nearest_neighbor_distance = dist
                    nearest_neighbor_location = j
                    nearest_neighbor_label = data[j][0]
        #print("Object " + str(i) + " is class " + str(label_object_to_classify))
        #print("Its nearest neighbor is " + str(nearest_neighbor_location) + " which is in class " + str(nearest_neighbor_label))
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified = number_correctly_classified + 1
    accuracy = number_correctly_classified/len(data)
    print("Accuracy: ", accuracy)
    return accuracy #rd.random()%100


def feature_search_demo(data):
    current_set = []
    final_set = []
    final_accuracy = 0

    for i in range (1,len(data[0])):
        print("On the " + str(i) + "th level of the search tree")
        feature_to_add_on_this_level = 0
        best_accuracy_so_far = 0

        for j in range (1,len(data[0])):
            print("J value: ", j)
            if j not in current_set:
                print("--Considering adding the " + str(j) + " feature")
                accuracy = leave_one_out_cross_validation(data, current_set, j)
                if accuracy > best_accuracy_so_far:
                    best_accuracy_so_far = accuracy
                    feature_to_add_on_this_level = j

        print("On level " + str(i) + ", I added feature " + str(feature_to_add_on_this_level) + " to current set\n")
        current_set.append(feature_to_add_on_this_level)
        if best_accuracy_so_far >= final_accuracy:
            final_accuracy = best_accuracy_so_far
            final_set.append(feature_to_add_on_this_level)
    
    print("Best set: ", final_set)
    print("Final Accuracy: ", final_accuracy)




print("Testing Output")
data = np.loadtxt('CS170_Small_Data__6.txt')
#print(data[])
current_set = []
numOfFeatures = data[1].size - 1

feature_search_demo(data)

