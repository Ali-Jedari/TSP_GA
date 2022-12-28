#!/usr/bin/env python
# coding: utf-8

'''
Travelling Salesman Problem with 51 cities
using Genetic Algorithm
'''

from random import random, randrange, shuffle
from math import sqrt
from sys import argv
from time import time

def read_coord(path='TSP51.txt'):
    lines = open(path).readlines()
    coord = []
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].split(' ')
        coord.append([int(lines[i][0]), int(lines[i][1]), int(lines[i][2])])
    
    return coord

def distance(coord, city1, city2):
    return sqrt((coord[city1-1][1] - coord[city2-1][1]) ** 2 + 
                (coord[city1-1][2] - coord[city2-1][2]) ** 2)

def route_length(coord, chromosome):
    #it is assumed that a path always starts from city #1
    d = distance(coord, 1, chromosome[0])
    d += distance(coord, 1, chromosome[-1])
    for i in range(1, len(chromosome)):
        d += distance(coord, chromosome[i-1], chromosome[i])
    
    return d

def crossover(parent1, parent2):
    r = randrange(len(parent1))    
    offspring = parent1[:r]
    for i in range(len(parent2)):
        if parent2[i] not in offspring:
            offspring.append(parent2[i])
    
    return offspring

def mutate(chromosome):
    r1 = randrange(len(chromosome))
    r2 = randrange(len(chromosome))
    if r1 < r2:
        chromosome[r1:r2] = chromosome[r1:r2][::-1]
    else:
        chromosome[r2:r1] = chromosome[r2:r1][::-1]
    return chromosome

def tsp(coord):
    population_size = 40
    p = []
    cities = [i for i in range(2, 52)]
    for i in range(population_size):
        temp_cities = cities.copy()
        shuffle(temp_cities)
        p.append(temp_cities)
    
    generation = 5000
    for gen in range(generation):
        length = []
        for x in p:
            length.append(route_length(coord, x))
        
        fitness = [1 / length[0]]
        for i in range(1, len(length)):
            fitness.append(fitness[i-1] + (1 / length[i]))
                
        best = p[length.index(min(length))]
        
        new_p = []
        while len(new_p) < population_size - 1:
            if random() <= 0.90:
                r1 = random()
                r2 = random()
                i = 0
                for i in range(len(fitness)):
                    if i == 0:
                        if 0 <= r1 <= fitness[i]:
                            break
                    elif fitness[i-1] < r1 <= fitness[i]:
                        break

                j = 0
                for j in range(len(fitness)):
                    if j == 0:
                        if 0 <= r2 <= fitness[j]:
                            break
                    elif fitness[j-1] < r2 <= fitness[j]:
                        break

                    offspring = crossover(p[i], p[j])
                    new_p.append(offspring)

        for i in range(len(new_p)):
            if random() <= 0.1:
                new_p[i] = mutate(new_p[i])

        new_p.append(best)
        p = new_p.copy()
        print(f'generation: {gen+1} out of {generation}, shortest_path_length: {min(length)}', end = '\r')

    return p

def main():
    if len(argv) == 1:
        coord = read_coord()
    else:
        coord = read_coord(argv[1])

    t1 = time()
    p = tsp(coord)
    t2 = time()
    print("\nTime Elapsed: %.2fs" %(t2-t1))

if __name__ == '__main__':
    main()
