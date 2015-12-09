#!/usr/bin/python
#coding:utf-8
'''
name   : testTurn.py
author : ykita
date   : Thu Dec 10 02:03:03 JST 2015
memo   :  
'''
import sys
from optparse import OptionParser
import util

def turnMirror(dice):
    mirrored = dice
    mirrored[0], mirrored[5] = mirrored[5], mirrored[0]
    mirrored[1], mirrored[4] = mirrored[4], mirrored[1]
    mirrored[2], mirrored[3] = mirrored[3], mirrored[2]
    return mirrored
    

def turnOne(dice):
    for d in dice:
        if d:
            print d
    
def turnTwo(dice):
    pass

def turn(dice,index,n):
    if n==1 and dice[index-1]>=1:
        dice[index-1] -= n
        dice[5-index+1] += n
    elif n==2 and dice[index-1]>=2:
        dice[index-1] -= n
        dice[5-index+1] += n
    return dice


parser = OptionParser()
(options, args) = parser.parse_args()

shoot = map(lambda x:int(x), list(reduce(lambda a,b:a+b,[]+args)))
if len(shoot)!=5:
    print "okashii"
    sys.exit(1)
dice = util.toDice(shoot)
print shoot
print dice
dice = turn(dice,1,1)
print dice
print util.toShoot(dice)

