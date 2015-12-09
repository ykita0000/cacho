#!/usr/bin/python
#coding:utf-8
'''
name   : check.py
author : ykita
date   : Thu Dec 10 03:25:50 JST 2015
memo   :  
'''
import os, os.path
import sys
import util

def DeMano(shoot):
    dice = util.toDice(shoot)
    if Grande(dice):
        print "  It's Grande De Mano."
    if Poker(dice):
        print "  It's Poker De Mano."
    if Full(dice):
        print "  It's Full De Mano."
    if Escalera(dice):
        print "  It's Escalera De Mano."

# actually not only for de mano
def Grande(dice):
    if dice.count(5):
        return True
    return False

def Poker(dice):
    if dice.count(4):
        return True
    return False
    
def Full(dice):
    if dice.count(3) and dice.count(2):
        return True
    return False

def Escalera(dice):
    if dice.count(1)==5 and dice[2] and dice[3] and dice[4]:
        return True
    return False

