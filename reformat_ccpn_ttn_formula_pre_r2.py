#!/usr/bin/python
from __future__ import print_function

import sys,os, re
from math import sqrt
import numpy as np
from scipy.optimize import fsolve

import matplotlib.pyplot as plt



datafilename1=sys.argv[1]
datafilename2=sys.argv[2]


if len(sys.argv)==5:
  relconc=sys.argv[4]

datafile1=open(datafilename1,'r')
datafile2=open(datafilename2,'r')

top_line1=datafile1.readline()
top_line2=datafile2.readline()

r_list=datafile1.readlines()
r2_list=datafile2.readlines()

l1=len(r_list)
l2=len(r2_list)

rate={}

if l1 != l2:
  print ("error -> different number of residues")
  exit()
  
i=0
r2=0
w=0
rp_values=[]
for peak in r_list:
  peak1=peak.split()
  peak2=r2_list[i].split()
  
  npts=len(peak1)
  rate[i]=[]
  for j in range(npts):
   try:
     r=float(peak1[j])
     w=float(peak2[j])
     r2=w*3.14
     func = lambda rp : r - r2*np.exp(-10.6/1000*rp)/(r2+rp)

     rp_initial_guess=40
     rp_solution=fsolve(func, rp_initial_guess)
     print (float(rp_solution), end=" ")
     rate[i].append(float(rp_solution))
  
   except: print ("0.0", end=' ')

  i=i+1
  print("")

  

  
