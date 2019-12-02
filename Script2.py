#!/usr/bin/env python
# coding: utf-8

# In[67]:


get_ipython().run_line_magic('matplotlib', 'inline')
import arcpy
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


fc = r"C:\Users\w935558\Desktop\Final\FinalData\FinalData.gdb\Question2Features"

histo_field = "Elevation"


def createHisto(featureclass, field):
    valuelist = []
    meansum = 0
    meannum = 0
    for value in arcpy.da.SearchCursor(featureclass, field):
        valuelist.append(value[0])
    n, bins, patches = plt.hist(valuelist, 6, facecolor='blue', alpha=0.5, density=0, histtype='barstacked')
    plt.xlabel(histo_field)
    plt.ylabel('Frequency')
    plt.title(r'Histogram of : {0}'.format(histo_field))
    plt.subplots_adjust(left=0.15)
    
    for entry in valuelist:
        meansum = meansum + entry
        meannum = meannum + 1
        
        mean = meansum / meannum 
        meansum2 = 0


    for entry in valuelist:
        entry = (entry - mean)**2
        meansum2 = meansum2 + entry
   
    mean2 = meansum2 / meannum    
    stddev = mean2**(1/2)


    print("The mean of the field's values is: {0}".format(mean))
    print("The standard deviation of the field's values is: {0} ".format(stddev))

    return

createHisto(fc,histo_field)


# In[ ]:





# In[ ]:




