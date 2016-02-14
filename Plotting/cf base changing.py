# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 14:15:21 2016

@author: Conor
"""
import matplotlib.pyplot as plt

abs1 = [1170,1310,1432]
abserror = [20,90,20]

cf85 = [1599.017366,2013.174279,2863.784965]
cf85err = [45,95,39]

cf110 = [1754.768052,1921.135175,2498.476821]
cf110err = [109,103,62]

x = [33,66,100]


plt.errorbar(x,abs1,yerr=abserror, label='ABS')
plt.errorbar(x,cf85,yerr=cf85err, label='Carbon Fibre ABS - Base @85C')
plt.errorbar(x,cf110,yerr=cf110err, label='Carbon Fibre ABS - Base @110C')
plt.xlim(30,105)
plt.title("Comparing the Elastic Moduli with Percentage of Fibres Aligned in the Direction of Pulling")
plt.legend(loc=2)
plt.xlabel("Percentage of Layers Alligned with Pulling Direction")
plt.ylabel("Young's Modulus (MPa)")
