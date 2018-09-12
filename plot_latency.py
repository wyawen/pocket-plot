import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker


#plt.rcParams.update({'font.size': 32})
plt.rcParams.update({'font.size': 30})

fig, (ax,ax2) = plt.subplots(2, 1, sharex=True, figsize=(15, 9))

N = 6
ind = np.arange(N)
width = 0.3

# 1KB latency microbenchmark results 
put_s3 = 25819
get_s3 = 12102
put_redis = 232
get_redis = 230
put_pocket_dram = 437
get_pocket_dram = 317 
put_pocket_nvme = 539 #525   
get_pocket_nvme = 422 #389 

get_pocket_ssd = 516 #912 
put_pocket_ssd = 604 #762 

get_pocket_hdd = 1975
put_pocket_hdd = 712 #629

put_pocket_metadata = 145 #186
get_pocket_metadata = 145 #183

puts = (put_s3, put_redis, put_pocket_dram, put_pocket_nvme, put_pocket_ssd, put_pocket_hdd)
gets = (get_s3, get_redis, get_pocket_dram, get_pocket_nvme, get_pocket_ssd, get_pocket_hdd)

put_c = '#1f77b4'
get_c = '#ff7f0e'
metadata_c = 'gray'
rects1 = ax.bar(ind, puts, width, color = put_c, hatch='/')
rects2 = ax.bar(ind + width, gets, width, color = get_c, hatch='.')
rects1 = ax2.bar(ind, puts, width, color = [put_c, put_c, metadata_c, metadata_c, metadata_c, metadata_c,
				 metadata_c, metadata_c], hatch='/')
rects2 = ax2.bar(ind + width, gets, width, color = [get_c, get_c, metadata_c, metadata_c, metadata_c,
				 metadata_c, metadata_c, metadata_c], hatch='.')
rects3 =  ax2.bar(ind[2:], [put_pocket_dram-put_pocket_metadata,
				  put_pocket_nvme-put_pocket_metadata, put_pocket_ssd-put_pocket_metadata,
				  put_pocket_hdd-put_pocket_metadata], width, color = put_c, hatch='/')
rects4 =  ax2.bar(ind[2:]+width, [get_pocket_dram-get_pocket_metadata,
				  get_pocket_nvme-get_pocket_metadata, get_pocket_ssd-get_pocket_metadata,
				  get_pocket_hdd-get_pocket_metadata], width, color = get_c, hatch='.')
'''
put_bottom = [put_pocket_dram-put_pocket_metadata, put_pocket_nvme-put_pocket_metadata]  
rects3 =  ax2.bar(ind[2:], [put_pocket_metadata, put_pocket_metadata], width, color = metadata_c, hatch='/', bottom=put_bottom)
get_bottom = [get_pocket_dram-get_pocket_metadata, get_pocket_nvme-get_pocket_metadata]
rects3 =  ax2.bar(ind[2:] + width, [get_pocket_metadata, get_pocket_metadata], width, color = metadata_c, hatch='.', bottom=get_bottom)
'''

# add some text for labels, title and axes ticks
#ax2.set_ylim(0,630)
ax2.set_ylim(0,2500)
ax.set_ylim(10000,30000)

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax.set_ylabel('Latency (us)')
#ax.set_title('Unloaded latency for 1KB requests')
ax2.set_xticks(ind + width / 2)
ax.set_xticklabels(('S3', 'Redis', 'Pocket\nDRAM', 'Pocket\nNVMe', 'Pocket\nSSD', 'Pocket\nHDD'))
ax.legend((rects1[0], rects2[0], rects2[2]), ('PUT', 'GET', 'Metadata RPC'))

def autolabel(rects, c):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%d' % int(height),
                ha='center', va='bottom', 
                fontsize='18', color=c)
        ax2.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%d' % int(height),
                ha='center', va='bottom', 
                fontsize='18', color=c)

autolabel(rects1,'black')
autolabel(rects2,'black')
#autolabel(rects3,'w')
#autolabel(rects4,'w')

plt.tight_layout()
plt.savefig("plots/unloaded-latency.pdf")
#plt.savefig("plots/unloaded-latency.png")

plt.show()


