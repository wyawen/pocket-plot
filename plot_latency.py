import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

plt.rcParams.update({'font.size': 24})

fig, (ax,ax2) = plt.subplots(2, 1, sharex=True, figsize=(15, 8))

N = 4 
ind = np.arange(N)
width = 0.3

# 1KB latency microbenchmark results 
put_s3 = 25819
get_s3 = 12102
put_redis = 232
get_redis = 230
put_pocket_dram = 508
get_pocket_dram = 414 #TODO: update with getBuffer
put_pocket_flash = 572   
get_pocket_flash = 466 #TODO: update with getBuffer
puts = (put_s3, put_redis, put_pocket_dram, put_pocket_flash)
gets = (get_s3, get_redis, get_pocket_dram, get_pocket_flash)

put_c = 'b'
get_c = 'y'
rects1 = ax.bar(ind, puts, width, color = put_c, hatch='/')
rects2 = ax.bar(ind + width, gets, width, color = get_c, hatch='.')
rects1 = ax2.bar(ind, puts, width, color = put_c, hatch='/')
rects2 = ax2.bar(ind + width, gets, width, color = get_c, hatch='.')

# add some text for labels, title and axes ticks
ax2.set_ylim(0,600)
ax.set_ylim(10000,30000)

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax.set_ylabel('Latency (us)')
#ax.set_title('Unloaded latency for 1KB requests')
ax2.set_xticks(ind + width / 2)
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
        ax2.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)


plt.tight_layout()
plt.savefig("plots/unloaded-latency.pdf")

plt.show()


