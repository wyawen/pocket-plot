import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

plt.rcParams.update({'font.size': 24})
fig, ax = plt.subplots(figsize=(15, 8))

N = 4 
ind = np.arange(N)
width = 0.3

# microbenchmark results for throughput
write_gbps_s3 = 13.6
read_gbps_s3 = 11.1
write_gbps_redis = 10.93
read_gbps_redis = 23.43
write_gbps_pocket_dram = 7.75 #using only 1 core, adding more cores incerase throughput to ~8Gb/s
read_gbps_pocket_dram = 8.06 
write_gbps_pocket_flash = 7.97   
read_gbps_pocket_flash = 8.13 

write_gbps = (write_gbps_s3, write_gbps_redis, write_gbps_pocket_dram, write_gbps_pocket_flash)
read_gbps = (read_gbps_s3, read_gbps_redis, read_gbps_pocket_dram, read_gbps_pocket_flash)
write_throughput = [ x*1000/8 for x in write_gbps] #convert from Gbps to MBps
read_throughput = [ x*1000/8 for x in read_gbps] #convert from Gbps to MBps

put_c = 'b'
get_c = 'y'
put_h = '/'
get_h = '.'
rects1 = ax.bar(ind, write_throughput, width, color=put_c, hatch=put_h)
rects2 = ax.bar(ind + width, read_throughput, width, color=get_c, hatch=get_h)


ax.set_ylabel('Throughput (MB/s)')
ax.set_ylim(0,3300)
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('S3', 'Redis', 'Pocket-DRAM', 'Pocket-Flash'))
ax.legend((rects1[0], rects2[0]), ('PUT', 'GET'))

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

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.savefig("plots/throughput.pdf")

plt.show()


