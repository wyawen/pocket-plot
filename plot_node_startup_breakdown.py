import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

plt.rcParams.update({'font.size': 32})
plt.rcParams.update({'pdf.fonttype': 42})
plt.rcParams.update({'ps.fonttype': 42})

fig, ax = plt.subplots(figsize=(15, 8))

N = 3 
ind = np.arange(N)
#ind = np.array([0,0.2,0.4])
print ind
width = 0.4

# node startup breakdowns 
vm_start        = np.array([82,    105,   177.99])
container_start = np.array([19.97, 15.96, 31.67])
container_img   = np.array([2.37,  2.1,   2.31])
#node_setup      = np.array([0,     1.056, 0.739])
#node_connect    = np.array([0,     0.3,   0.3])
#node_register   = np.array([0,     0.5,   47])
node_register   = np.array([0,     0.3+0.5+1.056,   0.3+0.5+0.739])

#breakdown = [vm_start, container_start, container_img, node_setup, node_connect, node_register]
breakdown = [vm_start, container_start, container_img, node_register]
breakdown_bottom = [[0]*len(vm_start)]
a0 = vm_start
a1 = a0+container_start
a2 = a1+container_img
#a3 = a2+node_setup
#a4 = a3+node_connect
#a5 = a4+node_register
a5 = a2+node_register
#addup = [a0, a1, a2, a3, a4, a5]
addup = [a0, a1, a2, a5]
tmp = [0]*len(vm_start)
for i in breakdown:
    tmp = np.array(i)+np.array(tmp)
    breakdown_bottom.append(tmp)

c_b = '#1f77b4'
c_r = '#d62728'
c_y = '#bcbd22'
c_o = '#ff7f0e'
c_g = '#2ca02c'
c_p = '#9467bd'
#c = [c_b, c_o, c_y, c_p, c_r, c_g]
c = [c_b, c_o, c_p, c_g]
p = []
#h = ['/','.','x','//','-','o']
h = ['/','.','x','o']
for i in xrange(len(breakdown)):
    p.append(plt.bar(ind, breakdown[i], width, color=c[i], bottom = breakdown_bottom[i], hatch=h[i]))
    #print addup[-i-1]
    #p.append(plt.bar(ind, addup[-i-1], width, color=c[-i-1]))
    
ax.set_ylim(0,260)
ax.set_ylabel('Time (s)')
ax.set_xticks(ind)
ax.set_xticklabels(('Metadata Server', 'DRAM Server', 'NVMe Server'))
#l = ('VM Startup', 'Container Image Pull', 'Container Startup', 'Datanode Setup', 'Connection to Namenode', 'Datanode Registration')
l = ('VM Startup', 'Container Image Pull', 'Container Startup', 'Datanode Registration')
#ax.legend((p[0][0], p[1][0], p[2][0], p[3][0], p[4][0], p[5][0]), (l), loc='upper left', ncol=1, fontsize=24)
ax.legend((p[0][0], p[1][0], p[2][0], p[3][0]), (l), loc='upper left', ncol=1, fontsize=24)

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        print height
        ax.text(rect.get_x() + rect.get_width()/2., 0.9*height,
                '%d' % int(height),
                ha='center', va='bottom')


def autolabel_right(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        print height
        ax.text(rect.get_x() + rect.get_width()/2., 0.8*height,
                '%d' % int(height),
                ha='left', va='bottom')
'''
for rect in p[5]:
    h = rect.get_height()
    w = rect.get_width()
    ax.text(rect.get_x() + w, h-20,
                '%d' % int(h),
                ha='left', va='bottom', 
                color=c[-1-5])

for rect in p[4]:
    h = rect.get_height()
    w = rect.get_width()
    ax.text(rect.get_x() + w, h-10,
                '%d' % int(h),
                ha='left', va='bottom', 
                color=c[-1-4])

'''

#autolabel(rects1)

plt.tight_layout()
plt.savefig("plots/node-startup-time-simplified.pdf")
#plt.savefig("plots/node-startup-time.png")

plt.show()


