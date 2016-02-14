# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 16:31:55 2016

@author: Conor
"""
import seaborn as sns
import matplotlib.pyplot as plt

abs1 = [1170,1310,1432]
abserror = [20,90,20]

cf85 = [1599.017366,2013.174279,2863.784965]
cf85err = [45,95,39]

cf110 = [1754.768052,1921.135175,2498.476821]
cf110err = [109,103,62]

hs = [1537.406208,1853.576255,2650.79776]
hserr = [40,60,60]
hf = [1630.328595,1984.993175,2485.599]
hferr = [40,50,50]
cs = [2259.604645,2875.051749,3038.013]
cserr = [20,70,70]
cf = [2202.481953,2700.000194,2906.150333]
cferr = [10,60,70]

x = [33,66,100]

#sns.tsplot(x,cs)
plt.errorbar(x,abs1,yerr=abserror, label='ABS')
#plt.errorbar(x,cf85,yerr=cf85err, label='CF-ABS - Base @85C')

#plt.errorbar(x,cf110,yerr=cf110err, label='CF-ABS - Base @110C')
plt.errorbar(x,hs,yerr=hserr, label='CF-ABS - Hot & Slow')
plt.errorbar(x,hf,yerr=hferr, label='CF-ABS - Hot & Fast')
plt.errorbar(x,cs,yerr=cserr, label='CF-ABS - Cold & Slow')
plt.errorbar(x,cf,yerr=cferr, label='CF-ABS - Cold & Fast')
plt.xlim(30,105)
plt.title("Comparing the Elastic Moduli Whilst Changing Printing Parameters")
plt.legend(loc=2)
plt.xlabel("Percentage of Layers Alligned with Pulling Direction")
plt.ylabel("Young's Modulus (MPa)")
