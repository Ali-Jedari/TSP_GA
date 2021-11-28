#Implementing AND logical function using Perceptron

#!/usr/bin/env python
# coding: utf-8

from matplotlib import pyplot as plt

threshold = 0.05

def activation(net_input):
    '''bipolar activation function using the pre-declared threshold variable'''
       
    if net_input > threshold: return 1
    elif -1 * threshold <= net_input <= threshold: return 0
    else: return -1

def perceptron(X_train, y_train):
    '''Perceptorn function 
        gets X_train and their respective labels called y_train,
        then returns weights and bias of the network'''
    
    #weights = [w1, w2]
    weights = [0, 0]
    bias = 0
    
    n = len(X_train)
    learning_rate = 0.2
    index = 0
    fault = True
    plot_number = 221
    
    while fault:
        fault = False
        s = X_train[index]
        t = y_train[index]
        net_input = (s[0] * weights[0]) + (s[1] * weights[1]) + (1 * bias)
        activation_result = activation(net_input)
        
        if activation_result != t:
            weights[0] += learning_rate * s[0] * t
            weights[1] += learning_rate * s[1] * t
            bias += learning_rate * t
            fault = True
        
        index = (index + 1) % n
        
        #Plotting input data and the separator line
        plt.subplot(plot_number)
        plt.title('Input No. %d' %(plot_number%10))
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        w1 = weights[0]
        w2 = weights[1]
        b = bias
        x = [-2, 2]
        y = [(threshold - b - (w1 * i)) / w2 for i in x]
        plt.plot(x, y)
        y = [((-1 * threshold) - b - (w1 * i)) / w2 for i in x]
        plt.plot(x, y)
        plt.plot([1, 1, -1, -1], [1, -1, 1, -1],'o')
        plot_number += 1
        plt.tight_layout()
    plt.show()
    return weights, bias

def test(X_train, y_train, X_test):
    '''Test function 
        gets X_train, y_train, and X_test 
        trains the network (finds the weights and bias)
        the returns the activation function's reusult on the test data'''
    
    weights, bias = perceptron(X_train, y_train)
    net_input = (X_test[0] * weights[0]) + (X_test[1] * weights[1]) + (1 * bias)
    return activation(net_input)

def main():
    AND_X_train = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    AND_y_train = [1, -1, -1, -1]
    print('Please do enter bipolar values (1 and -1)')
    x1 = int(input('x1 = '))
    x2 = int(input('x2 = '))
    output = test(AND_X_train, AND_y_train, [x1, x2])
    print('%d AND %d = %d' %(x1, x2, output))

if __name__ == '__main__':
    main()
