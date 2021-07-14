#Put this file and GUI.py in the same directory and
#Run GUI.py, if you want to test
#Do NOT run this file!

#!/usr/bin/env python
# coding: utf-8

def activation(n, threshold=0.05):
    '''bipolar activation function using the pre-declared threshold variable'''
    
    if n >= threshold: return 1
    elif -1 * threshold <= n <= threshold: return 0
    else: return -1

def perceptron(X_train, y_train):
    '''Perceptorn function 
        gets X_train and their respective labels called y_train,
        then returns weights and bias of the network'''
    
    weights = [0 for _ in range(25)]
    bias = 0
    
    n = len(y_train)
    learning_rate, index = 0.2, 0
    flag = True
    
    while flag:
        flag = False
        net_input = 0
    
        for i in range(len(X_train[index])):
            net_input += (X_train[index][i] * weights[i])
    
        net_input += bias

        if activation(net_input) != y_train[index]:
            for i in range(len(weights)):
                weights[i] += learning_rate * X_train[index][i] * y_train[index]
            flag = True
            bias += learning_rate * y_train[index]
            
        index = (index + 1) % n

    return weights, bias

def generator(input1, label1, input2, label2):
    '''Random train data generator
        gets two inputs (X-shape and O-shape) 
        changes at least one random element and at most two random elements every time
        and generates different shapes
        returns generated shapes and their respective labels'''
     
    from random import choice, randrange
    #Generating X-like shapes
    X_train = [input1]
    y_train = [label1]
    n = len(input1)
    ones = [0, 6, 12, 18, 24, 4, 8, 16, 20]
    for _ in range(n):
        temp_input = input1.copy()
        r = randrange(3)
        if r == 0:
            #change one random element that is 1
            index = randrange(len(ones))
            temp_input[ones[index]] *= -1
        elif r == 1:
            #change two random element that are 1
            index1 = randrange(len(ones))
            index2 = randrange(len(ones))
            temp_input[ones[index1]] *= -1
            temp_input[ones[index2]] *= -1
        else:
            #change a completely random element anywhere
            r1 = randrange(25)
            r2 = randrange(25)
            temp_input[r1] *= -1
            temp_input[r2] *= -1

        X_train.append(temp_input)
        y_train.append(label1)
    
    #Generating O-like shapes
    X_train.append(input2)
    y_train.append(label2)
    ones = [1, 2, 3, 5, 10, 15, 21, 22, 23, 9, 14, 19]
    for _ in range(n):
        temp_input = input2.copy()
        r = randrange(3)
        if r == 0:
            #change one random element that is 1
            index = randrange(len(ones))
            temp_input[ones[index]] *= -1
        elif r == 1:
            #change one random element that are 1
            index1 = randrange(len(ones))
            index2 = randrange(len(ones))
            temp_input[ones[index1]] *= -1
            temp_input[ones[index2]] *= -1
        else:
            #change a completely random element anywhere
            r1 = randrange(25)
            r2 = randrange(25)
            temp_input[r1] *= -1
            temp_input[r2] *= -1

        X_train.append(temp_input)
        y_train.append(label2)
        
    return X_train, y_train
    
def test(X_test):
    '''test function
        gets X_test and returns the predicted label for it'''
    
    X = [1, -1, -1, -1, 1,
         -1, 1, -1, 1, -1,
         -1, -1, 1, -1, -1,
         -1, 1, -1, 1, -1,
         1, -1, -1, -1, 1]
    
    O = [-1, 1, 1, 1, -1,
         1, -1, -1, -1, 1,
         1, -1, -1, -1, 1,
         1, -1, -1, -1, 1,
         -1, 1, 1, 1, -1]

    X_train, y_train = generator(X,1,O,-1)

    weights, bias = perceptron(X_train, y_train)

    #calculating net input
    net_input = 0
    for i in range(len(X_test)):
        net_input += X_test[i] * weights[i]
    
    net_input += bias

    return activation(net_input)

def converter(matrix):
    '''This function gets a 2D list, a matrix so to speak
        and converts it into a 1D (linear) list'''
    
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result.append(matrix[i][j])

    return result
