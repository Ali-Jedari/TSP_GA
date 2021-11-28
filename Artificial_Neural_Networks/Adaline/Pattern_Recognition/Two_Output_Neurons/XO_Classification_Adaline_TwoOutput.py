#!/usr/bin/env python
# coding: utf-8

#Implementing XO Classifier using Adaline network with two Output Neurons

def activation(net_input):
    '''bipolar activation function using the pre-declared threshold variable'''
    return 1 if net_input >= 0 else -1

def adaline(x_train, y_train):
    '''This function gets a train list,
        calculates the efficient weights and the bias
        then returns them both'''
    
    weights = [[0 for _ in range(25)], [0 for _ in range(25)]]
    bias = [0, 0]
    
    n = len(x_train)
    learning_rate = 0.01
    minimum = 0.0001

    for k in range(2):
        index = 0
        max_delta_w = float('inf')
        while max_delta_w > minimum:
            delta_w = [0 for _ in range(25)]
            s = x_train[index]
            t = y_train[index][k]
            y_NI = 0

            #Finding the net_input of the output neuron
            for i in range(len(s)):
                y_NI += weights[k][i] * s[i]
            y_NI += bias[k]

            for i in range(len(s)):
                delta_w[i] = learning_rate * (t - y_NI) * s[i]    #calculating delta_weight for each weight
            delta_b = learning_rate * (t - y_NI)    #calculating delta_bias

            max_delta_w = max(delta_w)    #finding the maximum delta_weight occurred in itteration

            for i in range(len(delta_w)):
                weights[k][i] += delta_w[i]   #updating weights
            bias[k] += delta_b    #updating bias
            index = (index + 1) % n    #moving index onto the train data in x_train
    
    return weights, bias

def test(x_test):
    '''Test function gets test data,
        trains the network (finds the weights and the bias)
        the returns the test's reusult'''
    
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

    x_train, y_train = generator(X,[1, -1],O,[-1, 1])

    weights, bias = adaline(x_train, y_train)

    #calculating net input
    net_input = [0, 0]
    for k in range(2):
        for i in range(len(x_test)):
            net_input[k] += x_test[i] * weights[k][i]
        net_input[k] += bias[k]

    return [activation(net_input[0]), activation(net_input[1])]

def generator(input1, label1, input2, label2):
    '''Random train data generator
    gets two inputs and labels corresponding to each
    changes a random element at every itteration
    to generate different shapes out of the precise shaped inputs'''
     
    from random import choice, random, randrange
    
    x_train = [input1, input2]
    y_train = [label1, label2]
    x_ones = [0, 6, 12, 18, 24, 4, 8, 16, 20]
    o_ones = [1, 2, 3, 5, 10, 15, 21, 22, 23, 9, 14, 19]
    
    for _ in range(50):
        rnd = random()
        if rnd <= 0.5:
            data = input1.copy()
            label = label1
            ones = x_ones
        else:
            data = input2.copy()
            label = label2
            ones = o_ones
        
        prob = randrange(3)
        if prob == 0:
            random_index = choice(ones)
            data[random_index] *= -1  #changes a random element
        elif prob == 1:
            random_index1 = choice(ones)
            random_index2 = choice(ones)
            data[random_index1] *= -1  #changes a random element
            data[random_index2] *= -1  #changes a random element
        else:
            r1 = randrange(25)
            r2 = randrange(25)
            data[r1] *= -1
            data[r2] *= -1

        x_train.append(data)
        y_train.append(label)
        
    return x_train, y_train

def converter(matrix):
    '''This function gets a 2D list, a matrix so to speak
        and converts it into a 1D (linear) list'''
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result.append(matrix[i][j])
    return result
