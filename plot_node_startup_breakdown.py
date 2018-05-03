import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

plt.rcParams.update({'font.size': 24})

fig, ax = plt.subplots(figsize=(15, 8))

N = 3 
ind = np.arange(N)
width = 0.5

# node startup breakdowns 
vm_start        = [82,    105,   177.99]
container_start = [19.97, 15.96, 31.67]
container_img   = [2.37,  2.1,   2.31]
node_setup      = [0,     1.056, 0.739]
node_connect    = [0,     0.3,   0.3]
node_register   = [0,     0.5,   47]

breakdown = [vm_start, container_start, container_img, node_setup, node_connect, node_register]
breakdown_bottom = [[0]*len(vm_start)]
tmp = [0]*len(vm_start)
for i in breakdown:
    tmp = np.array(i)+np.array(tmp)
    breakdown_bottom.append(tmp)

c = ['b', 'r', 'y', 'g', 'purple', 'c']
p = []
for i in xrange(len(breakdown)):
    print breakdown[i]
    print breakdown_bottom[i]
    p.append(plt.bar(ind, breakdown[i], width, color=c[i], bottom = breakdown_bottom[i]))
    

ax.set_ylabel('Time (s)')
ax.set_xticks(ind)
ax.set_xticklabels(('Namenode', 'DRAM Datanode', 'Flash Datanode'))
#ax.legend((p1[0], p1_1[0], p0_2[0], p1_2[0], p2_2[0]), ('Input/Ouput','Compute','S3 R/W','Redis R/W','Pocket-Flash R/W'))
l = ('VM Startup', 'Container Image Pull', 'Container Startup', 'Datanode Setup', 'Connection to Namenode', 'Datanode Registration')
ax.legend((p[0][0], p[1][0], p[2][0], p[3][0], p[4][0], p[5][0]), (l), loc='upper left', ncol=1, fontsize=20)

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
#for i in p:
#    autolabel(i)

plt.tight_layout()
plt.savefig("plots/node-startup-time.pdf")

plt.show()


