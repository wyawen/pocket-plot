#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

plt.rcParams.update({'font.size': 24})
fig, ax = plt.subplots(figsize=(15, 8))

N = 3 
ind = np.arange(N)
width = 0.2

# normalized app cost using different heuristics 
heuristics = ['No Knowledge', 'Num Lambdas', 'Num Lambdas + Capacity', 'Num Lambdas + Capacity + Peak Throughput']
apps = ["Sort", "Video Analytics", 'λ'.decode('utf-8')+"-cc"] 
h1 = [1,1,1]
h2 = [0.351369637,
        0.5409818585,
        0.8060832848]
h3 = [0.08466750943,
        0.1173961265,
        0.1942372275]
h4 = [0.04980441731,
        0.01494132519,
        0.01309144684]

rects1 = ax.bar(ind-width, h1, width, color = 'b', hatch='//')
rects2 = ax.bar(ind, h2, width, color = 'r', hatch='/')
rects3 = ax.bar(ind + width, h3, width, color = 'y', hatch='x')
rects4 = ax.bar(ind + width*2, h4, width, color = 'g', hatch='.')


ax.set_ylim(0,1.19)
ax.set_ylabel('Normalized Resource Cost ($/hr)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(apps)
space = 6
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), (heuristics), loc='upper center', ncol=2, columnspacing=space, fontsize=15)
#handlelength=5)
#labelspacing=2) 
#borderpad=2)

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
        #ax2.text(rect.get_x() + rect.get_width()/2., 1.05*height,
        #        '%d' % int(height),
        #        ha='center', va='bottom')

#autolabel(rects1)

plt.tight_layout()
plt.savefig("plots/app-sizing-heuristics.pdf")

plt.show()


