#Put this file and GUI.py in the same directory and
#Run GUI.py, if you want to test
#Do NOT run this file!

#!/usr/bin/env python
# coding: utf-8

def activation(n):
    '''bipolar step activation function'''
    return 1 if n >= 0 else -1

def network(X_train, y_train):
    '''main (train) function that uses Hebb's law
        gets X_train whose each element is either a X-like or O-like shape
        and respective labels (1 for X and -1 for O)
        returns network's weights'''
    
    height = len(X_train[0])
    width = len(X_train[0][0])    
    weights = [[0 for _ in range(height)] for _ in range(width)]
    
    for index in range(len(y_train)):
        for i in range(height):
            for j in range(width):
                weights[i][j] += X_train[index][i][j] * y_train[index]
    return weights

def test(X_test):
    '''test function
        gets X_test and returns the predicted label for it'''
    
    X = [[1, -1, -1, -1, 1],
         [-1, 1, -1, 1, -1],
         [-1, -1, 1, -1, -1],
         [-1, 1, -1, 1, -1],
         [1, -1, -1, -1, 1]]
    
    O = [[-1, 1, 1, 1, -1],
         [1, -1, -1, -1, 1],
         [1, -1, -1, -1, 1],
         [1, -1, -1, -1, 1],
         [-1, 1, 1, 1, -1]]

    X_train, y_train = generator(X,1,O,-1)

    weights = network(X_train, y_train)
    net_input = 0
    for i in range(len(X_test)):
        for j in range(len(X_test[i])):
            net_input += X_test[i][j] * weights[i][j]
    return activation(net_input)

def generator(input1, label1, input2, label2):
    '''Random train data generator
        gets two inputs (X-shape and O-shape) 
        changes at least one random element and at most two random elements every time
        and generates different shapes
        returns generated shapes and their respective labels'''
    
    from random import randrange
    
    #Generating X-like shapes
    X_train = [input1]
    y_train = [label1]
    height, width = len(input1), len(input1[0])
    ones = [[0,0], [1,1], [2,2], [3,3], [4,4], [0,4], [1,3], [2,2], [3,1], [4,0]]
    for _ in range(height):
        for _ in range(width):
            temp_input = input1.copy()
            r = randrange(3)
            if r == 0:
                #change one random element that is 1
                index = randrange(len(ones))
                temp_input[ones[index][0]][ones[index][1]] *= -1  #changes a random element
            elif r == 1:
                #change two random element that are 1
                index1 = randrange(len(ones))
                index2 = randrange(len(ones))
                temp_input[ones[index1][0]][ones[index1][1]] *= -1  #changes a random element
                temp_input[ones[index2][0]][ones[index2][1]] *= -1  #changes a random element
            else:
                #change a completely random element anywhere
                r1 = randrange(5)
                r2 = randrange(5)
                temp_input[r1][r2] *= -1

            X_train.append(temp_input)
            y_train.append(label1)
    
    #Generating O-like shapes
    X_train.append(input2)
    y_train.append(label2)
    ones = [[0,1], [0,2], [0,3], [1,0], [2,0], [3,0], [4,1], [4,2], [4,3], [1,4], [2,4], [3,4]]
    for _ in range(height):
        for _ in range(width):
            temp_input = input2.copy()
            r = randrange(3)
            if r == 0:
                #change one random element that is 1
                index = randrange(len(ones))
                temp_input[ones[index][0]][ones[index][1]] *= -1  #changes a random element
            elif r == 1:
                #change one random element that are 1
                index1 = randrange(len(ones))
                index2 = randrange(len(ones))
                temp_input[ones[index1][0]][ones[index1][1]] *= -1  #changes a random element
                temp_input[ones[index2][0]][ones[index2][1]] *= -1  #changes a random element
            else:
                #change a completely random element anywhere
                r1 = randrange(5)
                r2 = randrange(5)
                temp_input[r1][r2] *= -1

            X_train.append(temp_input)
            y_train.append(label2)
            
    return X_train, y_train
