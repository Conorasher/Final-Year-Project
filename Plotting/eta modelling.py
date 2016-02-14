# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 17:01:13 2016

@author: Conor
"""

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def n(G_m, E_f, V_f):
    a = 2 * G_m
    b = E_f * np.log(1/V_f)
    c = (a / b)**(0.5)
    return c
    
def eta(n,s):
    a = n*s
    b = np.tanh(a)
    c = (1 - (b/a))
    return c
    
def Gm(E_m, v):
    return (E_m / (2 * (1 + v)))

def vf(w_w, w_m, rho_f, rho_m):
    return (w_w / (w_w + (w_m * rho_f / rho_m)))

# w_w is the whieght ratio, w_m is the weight fraction of the matrix, 
#rho_f = , rho_m = 1.07 http://www.matbase.com/material-categories/natural-and-synthetic-polymers/commodity-polymers/material-properties-of-acrylonitrile-butadiene-styrene-general-purpose-gp-abs.html#properties
w_w = 0.12
w_m = 0.88
rho_f = 1.8
rho_m = 1.07
    
v = 0.35

E_m = 1430 * 10**6
E_f = 240 * 10**9

V_f = vf(w_w, w_m, rho_f, rho_m)
V_m = 1 - V_f
G_m = Gm(E_m, v)


x = np.linspace(0,400)

#Ayyy = 0.72 for printed, 0.86 for unprinted

diameter = 6.4453125
length = 89
s = length / diameter

def E_comp(E_f, V_f, eta_l, eta_o, E_m, V_m):
    return ((E_f * V_f * eta_l * eta_o) + (E_m * V_m))
    
eta_o = 0.72
n = n(G_m, E_f, V_f)
y = eta(n,x)
eta_l = eta(n,s)
x_1 = np.linspace(0,1)
e_cmp = E_comp(E_f, V_f, eta_l, x_1, E_m, V_m)
e_cmp = E_comp(E_f, V_f, eta_l, eta_o, E_m, V_m)


print e_cmp

#plt.plot(x_1,e_cmp)

#plt.plot(x,y)    
#v is poisson's ratio for ABS it is 0.35 according to http://www.engineersedge.com/plastic/materials_common_plastic.htm
# and http://xahax.com/subory/Spec_ABS.pdf

#sns.tsplot(x,cs)
#plt.errorbar(x,abs1,yerr=abserror, label='ABS')
#plt.errorbar(x,cf85,yerr=cf85err, label='CF-ABS - Base @85C')

#plt.errorbar(x,cf110,yerr=cf110err, label='CF-ABS - Base @110C')
#plt.errorbar(x,hs,yerr=hserr, label='CF-ABS - Hot & Slow')
#plt.errorbar(x,hf,yerr=hferr, label='CF-ABS - Hot & Fast')
#plt.errorbar(x,cs,yerr=cserr, label='CF-ABS - Cold & Slow')
#plt.errorbar(x,cf,yerr=cferr, label='CF-ABS - Cold & Fast')
#plt.xlim(30,105)
#plt.title("Comparing the Elastic Moduli Whilst Changing Printing Parameters")
#plt.legend(loc=2)
#plt.xlabel("n_o")
#plt.ylabel("E_Composite (Pa)")
