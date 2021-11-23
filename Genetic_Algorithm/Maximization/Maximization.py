#!/usr/bin/env python
# coding: utf-8

'''
Maximization problem using genetic algorithm
The aim is to find an 8-bit value (x) that maximizes x^2
Binary encoding is employed in this exercise
'''

from random import random, randrange

def f(x):
    return x ** 2

def int_to_binary(n):
    b = bin(n)[2:]
    return '0' * (8 - len(b)) + b

def crossover(parent1, parent2):
    offspring = []
    crossover_point = randrange(len(parent1))
    offspring.append(parent1[:crossover_point] + parent2[crossover_point:])
    offspring.append(parent2[:crossover_point] + parent1[crossover_point:])
    return offspring

def mutate(chromosome):
    r = randrange(len(chromosome))
    l = list(chromosome)
    l[r] = str(int(l[r] != '1'))
    return ''.join(l)

def maximize():
    population = []
    while len(population) < 50:
        b = int_to_binary(randrange(256))
        if b not in population:
            population.append(b)

    for _ in range(40):
        fitness = [f(int(x,2)) for x in population]
        s = sum(fitness)
        F = [fitness[0]/s]
        for i in range(1, len(fitness)):
            F.append(F[i-1] + (fitness[i] / s))
        
        new_population = []
        while len(new_population) < 50:    
            if random() < 0.90:
                r1 = random()
                r2 = random()
                i = 0
                for i in range(len(F)):
                    if F[i-1] <= r1 <= F[i]:
                        break
                j = 0
                for j in range(len(F)):
                    if F[j-1] <= r2 <= F[j]:
                        break
                offspring = crossover(population[i], population[j])
                new_population.append(offspring[0])
                new_population.append(offspring[1])
        
        if random() < 0.01:
            r = randrange(len(new_population))
            new_population[r] = mutate(new_population[r])
            
        population = new_population.copy()

    return max(population)

print(maximize())
