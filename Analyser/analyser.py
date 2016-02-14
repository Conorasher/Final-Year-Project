# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 12:22:14 2015

@author: Conor
"""

import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#print sheet

#def sheets(wb):
#    a=1
#    
def baseline(sheet):
    #nicked from http://stackoverflow.com/questions/13691775/python-pinpointing-the-linear-part-of-a-slope
    # create convolution kernel for calculating
    # the smoothed second order derivative
    x = sheet['strain']
    y = sheet['Force']
    smooth_width = 80
    x1 = np.linspace(-3,3,smooth_width)
    #norm = np.sum(np.exp(-x1**2)) * (x1[1]-x1[0]) # ad hoc normalization
    y1 = (4*x1**2 - 2) * np.exp(-x1**2) / smooth_width *8#norm*(x1[1]-x1[0])



    # calculate second order deriv.
    y_conv = np.convolve(y, y1, mode="same")
    sheet['use'] = y_conv
    

    # plot data
    #plt.plot(x,y_conv, label = "second deriv")
    #plt.plot(x, y, label="theory")
    #plt.plot(x, x, "0.3", label = "linear data")
    
    #plt.legend(loc=0)
    
    
    sheet2 = sheet[sheet['use'] > (-1)]
    sheet2 = sheet2[sheet2['use'] < (1)]
    #print sheet['poo']
    x = sheet2['strain']
    y = sheet2['Force']
    #plt.plot(x,y,'ro')
    #plt.show()
    b = sheet2.index
    a=[]
    for i in range(1, len(b)):
        c = b[i] - b[(i - 1)]
        a.append(c)
    baseln = []
    slp = []
    n = 0
    print a 
    for i in range(4, len(a)):
        if n == 1:
            if a[i + 1] < 3 and len(slp) < 8:
                slp.append(b[i + 1])
            else:
                n = 2
        if n == 0:
            if a[i] < 3:
                baseln.append(b[i + 1])
            else:
                n = 1
        
        
    t = (max(baseln) + 1)
    t = range(t, (t + 50))
    sheet3 = sheet.iloc[t]
    loc = max(sheet3['use'])
    loc = sheet[sheet['use'] == loc].index
    x_b = sheet['strain'][baseln]
    y_b = sheet['Force'][baseln]
    print slp
    z_coef = np.polyfit(x_b, y_b, 0)
    force_baseline = np.poly1d(z_coef)
    return force_baseline, loc, slp
    



def implementBaseline(sheet,force_baseline,time_baseline):
    fce = sheet.loc[0, 'Force']
    srs = sheet.loc[0, 'stress']
    factor = srs / fce
    for i in range(0, len(sheet)):
        sheet.loc[i, 'Alt. Force'] = sheet.loc[i, 'Force'] - force_baseline
        sheet.loc[i, 'Alt. Stress'] = sheet.loc[i, 'Alt. Force'] * factor
        sheet.loc[i, 'Alt. Time'] = sheet.loc[i, 'Time (ms)'] - time_baseline
        sheet.loc[i, 'Alt. Disp'] = (sheet.loc[i, 'Alt. Time'] / 1000) * (4.28 / 60)
        sheet.loc[i, 'Alt. Strain'] = sheet.loc[i, 'Alt. Disp'] / 40
    
    return sheet
    
    
    


def resultGet(sheet,slope,sheetName):
    x_b = sheet['Alt. Strain'][slope]
    y_b = sheet['Alt. Stress'][slope]
    ym_coeff = np.polyfit(x_b, y_b, 1)
    ym = np.poly1d(ym_coeff)
    t0sheet = sheet[sheet['Alt. Time'] > 0]
    x = t0sheet['Alt. Strain']
    y = t0sheet['Alt. Stress']
    plt.figure()
    plt.plot(x,y, label='"Data"')
    plt.plot(x,ym(x), label='Fit of Y.M.')
    plt.legend(loc=0)
    plt.xlabel('Strain')
    plt.ylabel('Stress (MPa)')
    title = 'Graph of Stress against Strain for Tab ' + str(sheetName)
    plt.title(title)
    plt.grid(True)
    fileName = str(sheetName) + '.png'
    plt.savefig(fileName, bbox_inches='tight')
    failStress = max(y)
    loc = sheet[sheet['Alt. Stress'] == failStress].index
    failStrain = sheet.loc[loc[0], 'Alt. Strain']
    return ym[1], failStress, failStrain
    
    
    


def doThings():
    wb = openpyxl.load_workbook('results.xlsx')
    #sheetName = 'C12'
    #sheet = pd.read_excel('results.xlsx', sheetname=sheetName,parse_cols='A,B,D,E,G,H')
    #force_baseline, time, slope = baseline(sheet)
    #time_baseline = sheet.loc[time[0], 'Time (ms)']
    #sheet = implementBaseline(sheet,force_baseline,time_baseline)  
    #ym, failStress, failStrain = resultGet(sheet,slope,sheetName)
    #dataTable.loc[sheetName, 'Failure Stress'] = failStress
    #dataTable.loc[sheetName, 'Failure Strain'] = failStrain
    #dataTable.loc[sheetName, "Young's Modulus"] = ym
    
    
    datalist = {"Young's Modulus":0,
            'Failure Stress':0,
            'Failure Strain':0}
            
    
#    wb = openpyxl.load_workbook('Carbon Fibre optomization printing.xlsx')
    c = wb.get_sheet_names()
    dataTable = pd.DataFrame(datalist, index=c[1:])
    #print dataTable
    for i in range(1, len(c)):
        sheetName = c[i]
        sheet = pd.read_excel('results.xlsx', sheetname=sheetName,parse_cols='A,B,D,E,G,H')
        force_baseline, time, slope = baseline(sheet)
        time_baseline = sheet.loc[time[0], 'Time (ms)']
        sheet = implementBaseline(sheet,force_baseline,time_baseline)  
        ym, failStress, failStrain = resultGet(sheet,slope,sheetName)
        dataTable.loc[sheetName, 'Failure Stress'] = failStress
        dataTable.loc[sheetName, 'Failure Strain'] = failStrain
        dataTable.loc[sheetName, "Young's Modulus"] = ym
        dataTable.to_csv('Data.csv')

        
doThings()

    