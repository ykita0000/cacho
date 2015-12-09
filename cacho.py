#!/usr/bin/python
#coding:utf-8
'''
name   : cacho.py
author : ykita
date   : Mon Dec  7 22:43:10 JST 2015
memo   :  
'''
import sys
import random
import time
from optparse import OptionParser

def checkDeMano(shoot):
    dice = [ shoot.count(i) for i in range(1,7) ]
    checkGrandeDeMano(dice)
    checkPokerDeMano(dice)
    checkFullDeMano(dice)
    checkEscaleraDeMano(dice)

# actually not only for de mano
def checkGrandeDeMano(dice):
    if dice.count(5):
        print "  It's Grande De Mano."
    
def checkEscaleraDeMano(dice):
    if dice.count(1)==5 and dice[2] and dice[3] and dice[4]:
        print "  It's Escalera De Mano."
    
def checkFullDeMano(dice):
    if dice.count(3) and dice.count(2):
        print "  It's Full De Mano."

def checkPokerDeMano(dice):
    if dice.count(4):
        print "  It's Poker De Mano."

def toGetGrande(shoot):
    pass

def checkPossibles(shoot):
    dice = [ shoot.count(i) for i in range(1,7) ]
    toGetGrande(shoot)


### possible


parser = OptionParser()
parser.add_option('-o','--opposit-side',dest='opp',default=False,help='Show opposit dice.')
parser.add_option('-s','--sleep',dest='sleep',default=False,help='.')
parser.add_option('-e','--end',dest='end',default=False,help='End after first shoot.')
(options, args) = parser.parse_args()

dice   = ( 1, 2, 3, 4, 5, 6 )
shoot1 = [ random.choice(dice) for _ in range(5) ]
if options.sleep:
    time.sleep(1)
print ""
print " shoot 1       | ", shoot1
if options.opp:
    print " opposite side | ", map(lambda x:7-x,shoot1)
print ""
checkDeMano(shoot1)
if options.end:
    sys.exit(0)

keep = []
while True:
    s = raw_input(" Which dice shoot again ? > ").replace(' ','')
    if not s.isdigit():
        print "Please input number(s) 1-5."
        continue
    p = map(lambda x:int(x), s)
    if not p:
        print "Please input number(s) 1-5."
        continue
    if not 1 in p:
        keep.append(shoot1[0])
    if not 2 in p:
        keep.append(shoot1[1])
    if not 3 in p:
        keep.append(shoot1[2])
    if not 4 in p:
        keep.append(shoot1[3])
    if not 5 in p:
        keep.append(shoot1[4])
    break
shoot2 = [ random.choice(dice) for _ in range(5-len(keep)) ]
if options.sleep:
    time.sleep(1)
print ""
print " shoot 2       | ", keep+shoot2
if options.opp:
    print " opposite side | ", map(lambda x:7-x,keep+shoot2)
print ""

checkPossibles(shoot2)

