#!/usr/bin/python
#coding:utf-8
'''
name   : ScoreMaster.py
author : ykita
date   : Wed May 11 13:08:37 JST 2016
memo   :  
'''
import os, os.path
import sys

class ScoreMaster(object):
    def getScore(scoreTable):
        score = 0
        score += getScoreGrande(scoreTable)
        score += getScorePoker(scoreTable)
        score += getScoreFull(scoreTable)
        score += getScoreEscalera(scoreTable)


    def setScoreNumbers(scoreTable):
        pass

    def getScoreNumbers(scoreTable):
        pass


    def setScoreGrande(scoreTable,x):
        if not scoreTable._grande[1]==0: 
            print "Grande Already Filled"
        elif not scoreTable._grande[0]==0: 
            scoreTable._grande[1] = x
        else:
            scoreTable._grande[0] = x
            
    
    def getScoreGrande(scoreTable):
        if scoreTable._grande[0]==1 and scoreTable._grande[1]==1: 
            return 100
        elif not scoreTable._grande[0]==1 and not scoreTable._grande[1]==1: 
            return 0
        elif not scoreTable._grande[1]==1 or not scoreTable._grande[0]==1: 
            return 50

    def setScoreEscalera(scoreTable,x):
        if scoreTable._escalera==0: 
            scoreTable._escalera = x
        else:
            print "Escalera Already Filled"
    
    def getScoreEscalera(scoreTable):
        elif scoreTable._escalera==1: 
            return 20
        elif scoreTable._escalera==2: 
            return 25
        return 0
        
    def setScoreFull(scoreTable,x):
        if scoreTable._full==0: 
            scoreTable._full = x
        else:
            print "Full Already Filled"

    def getScoreFull(scoreTable):
        elif scoreTable._full==1: 
            return 30
        elif scoreTable._full==2: 
            return 35
        return 0
        
    def setScorePoker(scoreTable,x):
        if scoreTable._poker==0: 
            scoreTable._poker = x
        else:
            print "poker Already Filled"
        
    def getScorePoker(scoreTable):
        elif scoreTable._poker==1: 
            return 40
        elif scoreTable._poker==2: 
            return 45
        return 0

