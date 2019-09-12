# -*- coding: utf-8 -*-
"""
--Orr Natural Selection Simulation--
A simple model of natural selection based on Orr, 2009. Fitness and its role in
evolutionary genetics.  Nature Reviews (Genetics) vol. 10, p. 531-539.
author: Ricardo A. S. Cerboncini
website: rcerboncini.freesite.vip
github repository:
  
--
MIT License

Copyright (c) 2019 Ricardo A. S. Cerboncini

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os, tkinter, tkinter.filedialog
import numpy, pandas
from scipy.integrate import odeint

print("\n Orr Natural Selection Simulation \n") 

#Define the value for relative fitness --w--:
while True:
    try:        
        w = float(input("What is the relative fitness (w = W2/W1)?"))
        if(0 < w < 1):
            s = 1 - w;
            print("w =",w,"and s =",s)
            break
        elif(w <= 0 or w >= 1):
            raise
    except:
        print("Error: number must be greater than 0 and lower than 1!")

#Define the initial frequency of the less fit allele/genotype in the population.
while True:
    try:        
        q0 = float(input("What is the initial frequency of the less fit allele (q0)?"))
        if(0 < q0 < 1):
            p0 = 1-q0
            print("p0 =",p0,"and q0 =",q0)
            break
        elif(q0 <= 0 or q0 >= 1):
            raise
    except:
        print("Error: number must be greater than 0 and lower than 1!")
        
#Now, let natural selection do it`s job!
print("\n Natural Selection is in progress!...")

def deltap (p,t):
    q = 1 - p
    dpdt = p*q*s / (1 - q * s)
    return dpdt

while True:
    try:
        t0 = 0
        while True:
            try:
                t1 = int(input("How many generations?"))
                if(t1 > 0):
                    print(t1,"generations")
                    break
                else:
                    raise
            except:
                print("Error: wrong input!")
        t = numpy.linspace(t0,t1,t1+1)
        p = odeint(deltap,p0,t)
        q = numpy.array([1-x for x in p])
        pdf = pandas.DataFrame(p, columns=['p'])
        qdf = pandas.DataFrame(q, columns=['q'])
        result = pandas.concat([pdf,qdf],axis=1)
        result.index.name = 'generation'
        print("\nInitial parameters:\n Initial p =",p0,"and Initial q =",q0,"\n\
              Relative fitness (w) =",w," Selection coefficient (s) =",s)
        print(result)
        root = tkinter.Tk()
        root.withdraw()
        root.wm_attributes("-topmost",True)
        savedir = tkinter.filedialog.askdirectory(parent=root,initialdir=os.getcwd(),title='Please select the output folder')
        root.destroy()
        os.chdir(savedir)
        result.to_csv("result.csv")
        break
    except:
        print("Error: wrong input!")