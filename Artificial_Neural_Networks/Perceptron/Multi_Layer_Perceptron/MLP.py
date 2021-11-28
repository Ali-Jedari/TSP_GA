#Multi-layer Perceptron using ‌‌Backpropagation

#!/usr/bin/env python
# coding: utf-8

f = open('ann-train.data').readlines()
x, y = [], []
for i in range(len(f)):
    f[i] = f[i].split(' ')
    f[i].remove('')
    f[i].remove('\n')
    x.append([])
    for j in range(len(f[i]) - 1):
        x[-1].append(float(f[i][j]))
    y.append(float(f[i][-1]))

X_train, y_train = x[:len(x)*3//4], y[:len(y)*3//4]  #Declaring X_train and y_train
X_validation, y_validation = x[len(x)*3//4:], y[len(y)*3//4:]  #Declaring validation sets

def sigmoid(x):
    '''sigmoid activation function'''
    from math import tanh
    return tanh(x)

def f_prime(x):
    '''derivative of the activation (sigmoid) function'''
    #df(x)/dt
    return 1 - (sigmoid(x) ** 2)

def mlp(X_train, y_train, X_valid, y_valid):
    '''main train function
        gets train and validation sets
        calculates and returns the weights and bias of the network
        the architecture of the network is 21 * 4 * 3'''
    
    from random import random
    
    #weights are initialized with values between -.25 and .25
    weights = [[[(random() / 2 - 0.25) for _ in range(4)] for __ in range(21)],
                [[random() / 2 - 0.25 for _ in range(3)] for __ in range(4)]]

    #biases are initialized with the same values
    bias = [[random() / 2 - 0.25 for _ in range(4)], 
            [random() / 2 - 0.25 for _ in range(3)]]
    
    learning_rate = 0.01
    previous_loss, loss_count = 0, 0
    
    while loss_count < 7:
        for i in range(len(X_train)):
            t = [0, 0, 0]
            t[int(y_train[i]) - 1] = 1
            
            z_ni = [0, 0, 0, 0]  #net_input of the hidden layer
            z = [0, 0, 0, 0]     #activation result of the hidden layer
            for k in range(4):
                net_input = 0
                for j in range(21):
                    net_input += weights[0][j][k] * X_train[i][j]
                net_input += bias[0][k]
                z_ni[k] = net_input
                z[k] = sigmoid(net_input)
            
            y_ni = [0, 0, 0]  #net_input of the output layer
            y = [0, 0, 0]     #activation result of the output layer
            for j in range(3):
                net_input = 0
                for k in range(4):
                    net_input += weights[1][k][j] * z[k]
                net_input += bias[1][j]
                y_ni[j] = net_input
                y[j] = sigmoid(net_input)

            delta = [0, 0, 0]
            delta_w = [[0 for _ in range(3)] for __ in range(4)]
            delta_b1 = [0, 0, 0]
            D = [0, 0, 0, 0]
            for k in range(3):
                delta[k] = (t[k] - y[k]) * f_prime(y_ni[k])
                for j in range(4):
                    delta_w[j][k] = learning_rate * delta[k] * z[j]
                    delta_b1[k] = learning_rate * delta[k]
                    D[j] += delta[k] * weights[1][j][k]
            delta = [0 for _ in range(4)]
            delta_v = [[0 for _ in range(4)] for __ in range(21)]
            delta_b2 = [0, 0, 0, 0]
            for j in range(4):
                delta[j] = D[j] * f_prime(z_ni[j])
                for k in range(21):
                    delta_v[k][j] = learning_rate * delta[j] * X_train[i][k]
                    delta_b2[j] = learning_rate * delta[j]

            for j in range(4):
                for k in range(21):
                    weights[0][k][j] += delta_v[k][j]
                bias[0][j] += delta_b2[j]

            for j in range(3):
                for k in range(4):
                    weights[1][k][j] += delta_w[k][j]
                bias[1][j] += delta_b1[j]
        
        loss = 0
        for i in range(len(X_valid)):
            if test(X_valid[i], weights, bias) != y_valid[i]:
                loss += 1
        
        if loss >= previous_loss:
            loss_count += 1
        else:
            loss_count = 0
        
        previous_loss = loss
        
    return weights, bias

def test(x_test, weights, bias):
    '''test function
        gets x_test, calculated weights, and biases
        predicts and returns the output of x_test'''
    
    z = [0, 0, 0, 0]
    for j in range(4):
        net_input = 0
        for i in range(21):
            net_input += weights[0][i][j] * x_test[i]
        net_input += bias[0][j]
        z[j] = sigmoid(net_input)

    y = [0, 0, 0]
    for j in range(3):
        net_input = 0
        for i in range(4):
            net_input += weights[1][i][j] * z[i]
        net_input += bias[1][j]
        y[j] = sigmoid(net_input)

    return float(y.index(max(y)) + 1)

weights, bias = mlp(X_train, y_train, X_validation, y_validation)

def main():
    test_data = open('ann-test.data').readlines()
    for i in range(len(test_data)):
        test_data[i] = test_data[i].split(' ')
        test_data[i].remove('')
        test_data[i].remove('\n')
        for j in range(len(test_data[i])):
            test_data[i][j] = float(test_data[i][j])

    n, correct = len(test_data), 0
    for r in range(n):
        x, y = test_data[r][:-1], test_data[r][-1]
        if test(x, weights, bias) == y:
            correct += 1

    print("Accuracy = %.2f%s" %(100 * correct/n, '%'))

if __name__ == '__main__':
    main()
