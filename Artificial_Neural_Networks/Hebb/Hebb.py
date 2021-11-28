#!/usr/bin/env python
# coding: utf-8

from matplotlib import pyplot as plt

def activation(n):
    '''bipolar step activation function'''
    return 1 if n >= 0 else -1

def hebb(X_train, y_train):
    '''main (train) function
        gets X_train and respective labels called y_train
        returns weights of the network which are calculated using hebb's law'''
    
    #weights = [w1, w2, bias]
    weights = [0, 0]
    bias = 0
    plot_number = 221
    for i in range(len(X_train)):
        delta_w1 = X_train[i][0] * y_train[i] #delta_w1 = x1 * y
        delta_w2 = X_train[i][1] * y_train[i] #delta_w2 = x2 * y
        delta_b = 1 * y_train[i]  #delta_b = b * y
        
        #Updating weights and also the bias
        weights[0] += delta_w1
        weights[1] += delta_w2
        bias += delta_b
        
        #Plotting input data and the separator line
        plt.subplot(plot_number)
        plt.title('iteration #%d' %(plot_number%10))
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        x = [-2, 2]
        if weights[1] != 0:
            y = [-1 * (float(weights[0]) / float(weights[1])) * i - (float(bias) / float(weights[1])) for i in x]
        else:
            y = [-1*float('inf'), float('inf')]
        plt.plot(x, y)
        plt.plot([1, 1, -1, -1], [1, -1, 1, -1],'o')
        plot_number += 1
        plt.tight_layout()
    plt.show()

    return weights, bias

def test(X_train, y_train, X_test):
    '''test function
        gets X_train and respective labels called y_train and X_test
        returns the result of the activation function for the X_test'''
    
    weights, bias = hebb(X_train, y_train)
    net_input = (weights[0] * X_test[0]) + (weights[1] * X_test[1]) + bias
    return activation(net_input)

def main():
    while True:
        option = int(input("Choose your logical function:\n1 AND\n2 OR\n>>> "))
        if option == 1:
            print("Please enter bipolar values (1 or -1)")
            x1 = int(input("x1 = "))
            x2 = int(input("x2 = "))

            AND_X_train = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
            AND_y_train = [1, -1, -1, -1]
            output = test(AND_X_train, AND_y_train, [x1, x2])
            print("%d AND %d is %d" %(x1, x2, output))
            break
        elif option == 2:
            print("Please enter bipolar values (1 or -1)")
            x1 = int(input("x1 = "))
            x2 = int(input("x2 = "))

            OR_X_train = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
            OR_y_train = [1, 1, 1, -1]
            output = test(OR_X_train, OR_y_train, [x1, x2])
            print("%d OR %d is %d" %(x1, x2, output))
            break
        else:
            print("\nInvalid option!\n")

if __name__=='__main__':
    main()
