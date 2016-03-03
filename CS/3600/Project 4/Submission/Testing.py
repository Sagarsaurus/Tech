from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt

def average(list):
    return sum(list)/float(len(list))

def stDeviation(list):
    mean = average(list)
    diffSq = [pow((val-mean),2) for val in list]
    return sqrt(sum(diffSq)/len(list))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)


pen = []
car = []
for iteration in range(5):
    result = testPenData([40])[1]
    pen.append(result)
    
for iteration in range(5):
    result = testCarData([40])[1]
    car.append(result)
print "Pen max is:", max(penlist), "Pen average is:", average(penlist), "Pen SD is:", stDeviation(penlist)
print "Car max is:", max(carlist), "Car average is:", average(carlist), "Car SD is:", stDeviation(carlist)

