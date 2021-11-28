#!/usr/bin/env python
# coding: utf-8

#Implementing AND logical function using Adaline

def activation(net_input):
    '''bipolar step activation function'''
    return 1 if net_input >= 0 else -1

def adaline(train_data):
    '''This function gets a train list,
        calculates the efficient weights and the bias
        then returns them both'''
    
    weights = [0, 0]
    bias = 0
    
    n = len(train_data)
    learning_rate = 0.01
    minimum = 0.0001
    max_delta_w = float('inf')
    index = 0
    
    while max_delta_w > minimum:
        delta_w = [0, 0]
        s = train_data[index][:-1]
        t = train_data[index][-1]
        y_NI = 0
        for i in range(len(delta_w)):
            y_NI += weights[i] * s[i]
        y_NI += bias
        
        for i in range(len(delta_w)):
            delta_w[i] = learning_rate * (t - y_NI) * s[i]
        delta_b = learning_rate * (t - y_NI)
        
        max_delta_w = max(delta_w)
        
        for i in range(len(delta_w)):
            weights[i] += delta_w[i]
        bias += delta_b
        index = (index + 1) % n

    return weights, bias

def test(x_test):
    and_input = [[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, -1]]
    weights, bias = adaline(and_input)
    net_input = 0
    for i in range(len(x_test)):
        net_input += x_test[i] * weights[i]
    net_input += bias
    
    return activation(net_input)

def main():
    x1 = int(input('x1 = '))
    x2 = int(input('x2 = '))
    result = test([x1, x2])
    print('%d AND %d = %d' %(x1, x2, result))

if __name__=='__main__':
    main()
