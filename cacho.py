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

def countDice(shoot):
    return [ shoot.count(i) for i in range(1,7) ]

def checkDeMano(shoot):
    dice = countDice(shoot)
    if checkGrande(dice):
        print "  It's Grande De Mano."
    if checkPoker(dice):
        print "  It's Poker De Mano."
    if checkFull(dice):
        print "  It's Full De Mano."
    if checkEscalera(dice):
        print "  It's Escalera De Mano."

# actually not only for de mano
def checkGrande(dice):
    if dice.count(5):
        return True
    return False

def checkPoker(dice):
    if dice.count(4):
        return True
    return False
    
def checkFull(dice):
    if dice.count(3) and dice.count(2):
        return True
    return False

def checkEscalera(dice):
    if dice.count(1)==5 and dice[2] and dice[3] and dice[4]:
        return True
    return False
    
def checkPossibilitiesGrande(shoot):
    dice = countDice(shoot)
    try:
        print  dice.index(2)+1
    except ValueError:
        pass
    # ひとつ投げて こんなことない
    # if dice.count(4):
    #     print "  chance to grande"
    # ふたつ投げて
    if not checkFull(dice) and dice.count(3):
        print "  chance to grande"
    # みっつ投げて
    # よっつ投げて
    # いつつ投げて

def showDice(shoot):
    dice = countDice(shoot)
    for i in range(6):
        sys.stdout.write(" %d |"%(i+1))
        for _ in range(dice[i]):
            sys.stdout.write("*")
        sys.stdout.write("\n")
    sys.stdout.write("\n")

### possible

parser = OptionParser()
parser.add_option('-o','--opposit-side',dest='opp',action='store_true',help='Show opposit dice.')
parser.add_option('-s','--sleep',dest='sleep',action='store_true',help='take 1 sec with shooting dice')
parser.add_option('-e','--end',dest='end',action='store_true',help='End after first shoot.')
parser.add_option('-g','--graph',dest='graph',action='store_true',help='Show dice histgram.')
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
if options.graph:
    showDice(shoot1)
checkDeMano(shoot1)
checkPossibilitiesGrande(shoot1)
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


