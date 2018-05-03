import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

plt.rcParams.update({'font.size': 24})

fig, ax = plt.subplots(figsize=(15, 8))

N = 4 
ind = np.arange(N)
width = 0.3

# microbenchmark results for IOPS
write_iops_s3 = 0 #TODO: update with fewer lambdas  
read_iops_s3 = 0  #TODO
write_iops_redis = 172425
read_iops_redis = 177772
write_iops_pocket_dram = 44065 #using only 1 core, adding more cores incerase throughput to ~8Gb/s
read_iops_pocket_dram = 133399
write_iops_pocket_flash = 45174
read_iops_pocket_flash = 77950

read_iops = (read_iops_s3, read_iops_redis, read_iops_pocket_dram, read_iops_pocket_flash)

rects2 = ax.bar(ind + width/2, read_iops, width, color = 'g')

ax.set_ylabel('IOPS')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('S3', 'Redis', 'Pocket-DRAM', 'Pocket-Flash'))
ax.legend('GET')

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
autolabel(rects2)

plt.tight_layout()
plt.savefig("plots/iops.pdf")

plt.show()


