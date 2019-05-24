'''
Created on May 24, 2019

@author: Carlo Cena
'''
from TSP.Population import Population

class TSP(object):
    '''
    Travelling Salesman problem with genetic algorithms
    '''


    def __init__(self, map, pc=0.8, pm=0.2, inhabitantsNumber=100, termination=1000):
        '''
        Constructor
        '''
        myPop = Population(map, pc, pm, inhabitantsNumber)
        myPop.computeFit()
        
        previous_fit = myPop.inhabitants[0].fit
        cont=0
        while cont<termination:
            myPop.reproduction()
            myPop.computeFit()
            #print(previous_fit, " ", myPop.inhabitants[0].fit, " ", myPop.inhabitants[0].route)
            if myPop.inhabitants[0].fit == previous_fit:
                cont += 1
            else:
                cont = 0
                previous_fit = myPop.inhabitants[0].fit
        print("Best track found has length: ", previous_fit, " track: ", myPop.inhabitants[0].route)
                
        
        