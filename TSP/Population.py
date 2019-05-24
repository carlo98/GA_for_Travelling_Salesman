'''
Created on May 24, 2019

@author: carlo
'''
from TSP.Solution import Solution
from random import randint
MAX_DISTANCE = 1000.0

class Population(object):
    '''
    classdocs
    '''
    inhabitants = []
    numName = []
    
    def __init__(self, map, pc, pm, inhabitantsNumber):
        '''
        @map: dictionary of dictionaries: <cityName, dict<city, distance>>
        '''
        self.map = map
        for cityName in map:
            self.numName.append(cityName)
        self.pc = pc
        self.pm = pm
        for i in range(inhabitantsNumber):
            self.inhabitants.append(Solution(len(map)))
            
    def computeFit(self):
        for solution in self.inhabitants:
            solution.fit = 0.0
            previous_city = solution.route[0]
            for city in solution.route:                
                if city != previous_city:
                    if self.numName[city] in self.map[self.numName[previous_city]]:
                        solution.fit += self.map[self.numName[previous_city]][self.numName[city]]
                    else:
                        solution.fit += MAX_DISTANCE
                previous_city = city
        self.inhabitants.sort(key=lambda x: x.fit, reverse=False)
        
    def reproduction(self):
        half_size= int(len(self.inhabitants)/4)
        i= int(len(self.inhabitants)/2)
        while i < len(self.inhabitants):
            first = randint(0, len(self.map)-1)
            second = randint(0, len(self.map)-1)
            tmp = self.inhabitants[i].route[first]
            self.inhabitants[i].route[first] = self.inhabitants[i].route[second]
            self.inhabitants[i].route[second] = tmp
            i += 1  
        
        
                    