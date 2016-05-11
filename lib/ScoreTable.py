#!/usr/bin/python
#coding:utf-8
'''
name   : ScoreTable.py
author : ykita
date   : Wed May 11 12:52:59 JST 2016
memo   :  
'''
import os, os.path
import sys


class ScoreTable(object):
    def __init__(self):

        ### point 
        self._totalPoint = 0

        ### status as 0 or 1 
        self._grande     = [ 0, 0 ]
        self._poker      = 0
        self._full       = 0
        self._escalera   = 0

        ### numbers take status as 0 to 6
        self._numbers = [ 0, 0, 0, 0, 0, 0 ]

    # def setGrande(self,x):
    #     if self._grande[0]==0:
    #         self._grande[0] = x:
    #     elif not self._grande[0]==0:
    #         self._grange[1] = x

    # def sum(self):
    #     self._totalPoint += 1 * self._numbers[0]
    #     self._totalPoint += 2 * self._numbers[1]
    #     self._totalPoint += 3 * self._numbers[2]
    #     self._totalPoint += 4 * self._numbers[3]
    #     self._totalPoint += 5 * self._numbers[4]
    #     self._totalPoint += 6 * self._numbers[5]

    #     ###  on the way 

    # def getPoints(self):
    #     return self._totalPoint

    # def showScoreTable(self):
    #     pass

    # def getScore(self):
    #     totalPoint = 0


