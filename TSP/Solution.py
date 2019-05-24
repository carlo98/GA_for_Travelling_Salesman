'''
Created on May 24, 2019

@author: carlo
'''
from random import randint
MAX_DISTANCE = 1000.0

class Solution(object):
    '''
    classdocs
    '''
    route = []
    fit = MAX_DISTANCE

    def __init__(self, cityNumber):
        '''
        Constructor
        '''
        self.route = []
        start = randint(0, cityNumber-1)
        for i in range(cityNumber):
            self.route.append((start+i) % cityNumber)    