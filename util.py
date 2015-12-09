#!/usr/bin/python
#coding:utf-8
'''
name   : util.py
author : ykita
date   : Thu Dec 10 02:15:25 JST 2015
memo   :  
'''
import os, os.path
import sys

    
def checkPossibilitiesGrande(shoot):
    dice = toDice(shoot)
    try:
        print  dice.index(2)+1
    except ValueError:
        pass
    # ひとつ投げて こんなことない
    # if dice.count(4):
    #     print "  chance to grande"
    # ふたつ投げて
    if not check.Full(dice) and dice.count(3):
        print "  chance to grande"
    # みっつ投げて
    # よっつ投げて
    # いつつ投げて

def showDice(shoot):
    dice = toDice(shoot)
    for i in range(6):
        sys.stdout.write(" %d |"%(i+1))
        sys.stdout.write(reduce(lambda a,b:a+b,[]+[ "*" for _ in range(dice[i]) ]+["\n"]))


def toDice(shoot):
    return [ shoot.count(i) for i in range(1,7) ]
    
def toShoot(dice):
    shoot = []
    # shoot = [ 0, 0, 0, 0, 0 ] 
    for j in range(dice[0]):
        shoot.append(1)
    for j in range(dice[1]):
        shoot.append(2)
    for j in range(dice[2]):
        shoot.append(3)
    for j in range(dice[3]):
        shoot.append(4)
    for j in range(dice[4]):
        shoot.append(5)
    for j in range(dice[5]):
        shoot.append(6)
        
    return shoot
    
