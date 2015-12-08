#!/usr/bin/python
#coding:utf-8
'''
name   : cacho.py
author : ykita
date   : Mon Dec  7 22:43:10 JST 2015
memo   :  
'''
import random
import time
from optparse import OptionParser

def checkGrande(shoot):
    if shoot[0]==shoot[1]==shoot[2]==shoot[3]==shoot[4]:
        print "It's Grande"
    

parser = OptionParser()
parser.add_option('-o','--opposit-side',dest='opp',default=False,help='Show opposit dice.')
(options, args) = parser.parse_args()

dice   = ( 1, 2, 3, 4, 5, 6 )
shoot1 = [ random.choice(dice) for _ in range(5) ]
time.sleep(1)
print ""
print " shoot 1       | ", shoot1
if options.opp:
    print " opposite side | ", map(lambda x:7-x,shoot1)
print ""

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
time.sleep(1)
print ""
print " shoot 2       | ", keep+shoot2
if options.opp:
    print " opposite side | ", map(lambda x:7-x,keep+shoot2)
print ""
