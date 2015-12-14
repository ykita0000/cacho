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

import util
import check
import shootMovie

### possible

parser = OptionParser()
parser.add_option('-o','--opposit-side',dest='opp',action='store_true',help='Show opposit dice.')
parser.add_option('-s','--sleep',dest='sleep',action='store_true',help='take 1 sec with shooting dice')
parser.add_option('-e','--end',dest='end',action='store_true',help='End after first shoot.')
parser.add_option('-g','--graph',dest='graph',action='store_true',help='Show dice histgram.')
parser.add_option('-m','--movie',dest='movie',action='store_true',help='Show movie of shooting dice.')
(options, args) = parser.parse_args()

dice   = ( 1, 2, 3, 4, 5, 6 )
shoot1 = [ random.choice(dice) for _ in range(5) ]
if options.sleep:
    time.sleep(1)

if options.movie:
    shootMovie.shootMovie()
    
print ""
print ""
print " shoot 1       | ", shoot1
if options.opp:
    print " opposite side | ", map(lambda x:7-x,shoot1)
print ""
if options.graph:
    util.showDice(shoot1)
check.DeMano(shoot1)
# util.check.PossibilitiesGrande(shoot1)
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


