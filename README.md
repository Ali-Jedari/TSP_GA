# Simulation of Travelling Salesman Problem using Genetic Algorithm
## Introduction
In this project, the aim is to implement a simulation of the TSP using GA from scratch and find the route with the shortest length.

It should be noted that in this problem, the salesman must enter a city only once, except for the first city that he began his journey from.

In this simulation, it is assumed that the salesman always starts from the City #1 and therefore, he returns to this city at the end.
## Installation
First, you need to clone this repository to your local machine via the following command:
```shell
$ git clone https://github.com/Ali-Jedari/TSP_GA.git
```
In case you don't have `git` installed on your computer, you can download the zip file of this repository and then, extract it.
## Requirements
This project is written in Python3 and since it is implemented from scratch, no additional libraries are required.

The TSP51.txt file needs to be in the same directory as the TSP.py file. Otherwise, the path to TSP51.txt file should be specified as a command-line argument, as follows:
```shell
$ python TSP.py path/to/TSP51.txt
```

## Usage
Run:
```shell
$ cd TSP_GA
$ python TSP.py
```