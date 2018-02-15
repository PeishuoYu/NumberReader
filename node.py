import math
import os
from PIL import Image


# eg. {'1':['1','0']} which means there is one attribute called '1', and it has two possible values, '0' and '1'.
# in this program, because there are 1600 attributes, I will use a function to modify this dict, and leave it empty now.
attribute_key = {}


# the target attribute name and possible values, actually it is not used in the rest of program.
target_key = {'number': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}


# a node class, attribute will record how the entire data have been sorted
# dataSet is the dataSet after the entire dataSet have been sorted in the way that is recorded in attribute
# entropy is calculated based on the dataSet, when it reaches 0.0, it means that the dataset is pure
# uptree is the connection to the uptree, it could be a node class or None
# subtree is the connection to the subtree, it could be a list of node class or []
class node():
    def __init__(self, attribute, dataSet, uptree = None):
        self.dataSet = dataSet
        self.attribute = attribute
        self.entropy = getEntropy(dataSet)
        self.uptree = uptree
        self.subtree = []


    def __str__(self):
        result = 'Attributes: ' + str(self.attribute) + '\nentropy: ' + str(self.entropy)
        result += '\ndataset: ' + str(self.dataSet) + '\nuptree: '
        if self.uptree is None:
            result += str(self.uptree) + '\nsubtree: \n' + self.print_subtree()
        else:
            result += str(self.uptree.attribute) + ' ' + str(self.uptree.entropy) + '\nsubtree: \n' + self.print_subtree() + '\n'
        return result

    def print_subtree(self):
        if self.subtree == []:
            return 'None'
        else:
            result = ''
            for i in range(len(self.subtree)):
                result += (str(i) + '. ' + str(self.subtree[i].attribute) + ' ' + str(self.subtree[i].entropy)+ '\n')
            return result


# get the entropy of a dataSet
def getEntropy(dataSet):
    number = {}
    for i in dataSet:
        if i[-1] in number:
            number[i[-1]] += 1
        else:
            number[i[-1]] = 1
    total = len(dataSet)
    entropy = 0
    for i in number:
        entropy -=(number[i]/total*math.log((number[i]/total),2))
    return entropy


# get the entropy of a divided dataSet, this can be used to calculate the information gain
def getDivideSetEntropy(dividedSet):
    entropy = 0
    total = 0
    for i in dividedSet:
        entropy += len(i) * getEntropy(i)
        for j in i:
            total += 1
    entropy /= total
    return entropy


# if the second parameter is left blank
# this function will choose the attribute that can most efficiently divide the dataSet of an old_node
# and attach the new_node that are generated to the old_node
# if the second parameter is not blank
# this function will use the attribute provided to sort the data and do the same thing as before
def choose_attribute(old_node, final_attribute = ''):
    nodes = []
    if final_attribute != '':
        dividedSet = divideDataSet(old_node.dataSet, final_attribute)
        for singleSet in range(len(dividedSet)):
            entropy = getDivideSetEntropy(dividedSet)
            new_node_attribute = old_node.attribute.copy()
            new_node_attribute[final_attribute] = attribute_key[final_attribute][singleSet]
            new_node = node(new_node_attribute, dividedSet[singleSet], old_node)
            nodes.append(new_node)
    else:
        unusedAttributes = set(attribute_key.keys()) - set(old_node.attribute.keys())
        entropy = 100
        final_attribute = ''
        if unusedAttributes == set() or getEntropy(old_node.dataSet) == 0:
            return None
        for attribute in unusedAttributes:
            dividedSet = divideDataSet(old_node.dataSet, attribute)
            if entropy > getDivideSetEntropy(dividedSet):
                nodes = []
                entropy = getDivideSetEntropy(dividedSet)
                final_attribute = attribute
                for singleSet in range(len(dividedSet)):
                    new_node_attribute = old_node.attribute.copy()
                    new_node_attribute[attribute] = attribute_key[attribute][singleSet]
                    new_node = node(new_node_attribute, dividedSet[singleSet], old_node)
                    nodes.append(new_node)
    old_node.subtree = nodes
    print('\nSorting ' + str(old_node.attribute) + ' based on: ' + final_attribute + '\nentropy: ' + str(entropy) + '\ninformation gain: ' +str(old_node.entropy - entropy) + '\n')
    return nodes


# this is a driver that uses the functions to generate model and print how the dataSet is sorted
def computing(node_list):
    for i in node_list:
        print(str(i)[:-15])
    print('------------------------------------------')
    for i in node_list:
        result = choose_attribute(i)
        if result != None:
            computing(result)


# this will divide the dataSet according to the attribute provided, and return a list of dataSet that has been divided
def divideDataSet(dataset, attribute):
    index = list(attribute_key.keys()).index(attribute)
    possible = len(attribute_key[attribute])
    dividedSet = []
    for i in range(possible):
        dividedSet.append([])
    for i in dataset:
        dividedSet[attribute_key[attribute].index(i[index])].append(i)
    return dividedSet


# this function will take the root node of a model and return the information about the nodes that do not have subtree
def getLeaf(beginningNode, leaves):
    if beginningNode.subtree != []:
        for i in beginningNode.subtree:
            leaves += getLeaf(i, leaves)
        if beginningNode.uptree != None:
            return []
        else:
            return leaves
    else:
        attribute = beginningNode.attribute
        result = {}
        for i in beginningNode.dataSet:
            if i[-1] in result:
                result[i[-1]] += 1
            else:
                result[i[-1]] = 1
        judge = ''
        number = 0
        for i in result:
            if result[i] > number:
                judge = i
                number = result[i]
        return [[attribute, judge, len(beginningNode.dataSet), beginningNode.entropy]]


# this function export a model to a txt file, there will be all the attribute and possible value, the target attribute
# and possible value, and the model that has been established (included attribute, predict result, number of occurrence,
# and entropy
def exportModel(beginningNode):
    file = open('numbers/model.txt', 'w')
    file.write('attributes:\n')
    file.write(str(attribute_key) + '\n')
    file.write('target:\n')
    file.write(str(target_key) + '\n')
    leaves = getLeaf(beginningNode, [])
    file.write('result:\n')
    file.write(str(leaves))
    file.close()


# an interactive_mode, really did not write much about it, you can show the current node, show the subtree nodes,
# show the uptree nodes, move the current node, and sort the current node.
def interactive_mode():
    # open file
    file = open('sample.txt', 'r')
    content = file.read()
    content = content.split('\n')
    for i in range(len(content)):
        content[i] = content[i].split(',')
    tree = node({}, content)
    # input
    words = input()
    # 'stop' will close the program
    while words != 'stop':
        # show the current node
        if words == 'show':
            print(tree)
        # show the upper node
        elif words == 'show upper':
            print(tree.uptree)
        # show the subtree
        elif words == 'show sub':
            print(tree.print_subtree())
        # move the current node up or down, if down, a list of subtree will show and you can make the selection
        elif words == 'move':
            direction = input('up or down: ')
            if direction == 'up':
                if tree.uptree != None:
                    tree = tree.uptree
                    print('moved')
                else:
                    print('no uptree')
            elif direction == 'down':
                if tree.subtree == []:
                    print('no subtree')
                else:
                    print(tree.print_subtree())
                    number = int(input('which subtree: '))
                    try:
                        tree = tree.subtree[number]
                        print('moved')
                    except:
                        print('invalid input')
        # sort the data according to a specific attribute, a list of possible attributes will show and you can make
        # selection
        elif words == 'sort':
            print('available sorting options')
            for i in range(len(attribute_key.keys())):
                print(str(i) + '. ' + (list(attribute_key)[i]))
            number = int(input('which option: '))
            try:
                attribute = list(attribute_key)[number]
                choose_attribute(tree, attribute)
                print('sorted')
            except:
                print('invalid input')
        # delete the subtree
        elif words == 'delete sub':
            tree.subtree = []
            print('deleted')
        words = input()


# make the prediction based on the existing model file (model.txt) and the input from test.png
# if the prediction is wrong, enter the right value, and this prediction question will be moved to training set
def makePrediction():
    # turn image into 0s and 1s, and save it to test.txt
    content = ''
    image = Image.open('numbers/test.png').resize((40, 40))
    image = list(image.getdata())
    for i in range(len(image)):
        content += str(sum(image[i]) // 765)
        if (i + 1) % 40 == 0:
            content += '\n'
    data = list(content.replace('\n',''))
    file = open('numbers/test.txt', 'w')
    file.write(content)
    file.close()
    # read the model from mode.txt, and make it ready for making prediction
    file = open('numbers/model.txt', 'r')
    content = file.readlines()
    file.close()
    attribute = eval(content[1][:-1])
    target = eval(content[3][:-1])
    feature = eval(content[5])
    # fill the attribute_key dict
    preparation()
    # find the attribute in the model that fit the data provided, and print the prediction
    for result in feature:
        fit = True
        for attribute in result[0]:
            if data[list(attribute_key.keys()).index(attribute)] != result[0][attribute]:
                fit = False
        if fit:
            print('\n\n\n     Prediction: ' + result[1] + '\n\n\n')
    # prompt you to enter the right answer, if you enter, this prediction example will be saved in training set
    # if you prefer not to save the prediction example to training set, just press enter and the program will close
    rightAnswer = input('right answer? ')
    if rightAnswer != '':
        file = open('numbers/test.txt', 'r')
        content = file.read()
        content += rightAnswer
        file.close()
        num = 1
        while os.path.exists('numbers/' + str(num) + '.txt'):
            num += 1
        file = open('numbers/' + str(num) + '.txt', 'w')
        file.write(content)
        file.close()

# fill the attribute_key dict
def preparation():
    for i in range(1600):
        attribute_key[str(i)] = ['0', '1']

# read all the file in trainingset and make a single file that contains all sample
def updateTrainingSet():
    newcontent = ''
    num = 1
    while os.path.exists('numbers/' + str(num) + '.txt'):
        file = open('numbers/' + str(num) + '.txt', 'r')
        content = file.read().replace('\n', '')
        # making sure that each file has 1600 positions and one answer at the end
        if len(content)!= 1601:
            raise Exception('Number ' + str(num) + ' has problem.')
        for i in content:
            newcontent += i + ','
        newcontent = newcontent[:-1] + '\n'
        file.close()
        num += 1
    file = open('numbers/sample.txt', 'w')
    file.write(newcontent[:-1])
    file.close()

# this function is used to train the data and export model
def training(i = True):
    updateTrainingSet()
    file = open('numbers/sample.txt', 'r')
    content = file.read()
    content = content.split('\n')
    if i:
        preparation()
    for i in range(len(content)):
        content[i] = content[i].split(',')
    tree = node({},content)
    computing([tree])
    exportModel(tree)

# this function will tell you the number of samples of different Numbers ('0' - '9')
def sampleResult():
    file = open('numbers/sample.txt', 'r')
    content = file.read()
    file.close()
    content = content.split('\n')
    a = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for i in content:
        number = i.split(',')[-1]
        a[number] += 1
    print(a)

# instruction:
# open "Paint" application in windows and draw a number, save it as "test.png" under the number folder
# the PNG should be a square image
# run the makePrediction function, after the prediction is made, the program will prompt you to enter the right answer,
# if you enter the answer, this prediction example will be saved in training set
# if you prefer not to save the prediction example to the training set, just press 'enter' and the program will close
# when you think you have enough samples, you can train the model using the training() function
# sampleResult() will tell you the number of samples of different Numbers ('0' - '9')

#training()
makePrediction()
#sampleResult()