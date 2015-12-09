#!/usr/bin/python
#coding:utf-8
'''
name   : PointsTable.py
author : ykita
date   : Wed Dec  9 16:44:22 JST 2015
memo   :  
'''
import os, os.path
import sys


class PointsTable(object):
    def __init__(self):

        ### point 
        self._totalPoint = 0

        ### code take status as 0 or 1 
        self._grande     = [ 0, 0 ]
        self._poker      = 0
        self._full       = 0
        self._escalera   = 0

        ### numbers take status as 0 to 5
        self._numbers = [ 0, 0, 0, 0, 0, 0 ]

    def setGrande(self,id):
        self._grange[id] = 1
        
        

    def sum(self):
        self._totalPoint += 1 * self._numbers[0]
        self._totalPoint += 2 * self._numbers[1]
        self._totalPoint += 3 * self._numbers[2]
        self._totalPoint += 4 * self._numbers[3]
        self._totalPoint += 5 * self._numbers[4]
        self._totalPoint += 6 * self._numbers[5]

        ###  on the way 

    def getPoints(self):
        return self._totalPoint
