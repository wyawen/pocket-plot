import pandas as pd
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.text import OffsetFrom

#time net_usedMbps avg_cpu dram_usedGB net_allocMbps dram_allocGB
plt.rcParams.update({'font.size': 30})
plt.rcParams.update({'pdf.fonttype': 42})
plt.rcParams.update({'ps.fonttype': 42})

def plot_throughput_scaling():
 
  x = range(1,7)
  s3 = [1.5]*6
  redis = [0.92, 1.75, 2.7, 3.3, 4.2, 4.67]
  pocket_dram = [0.99, 1.92, 2.8, 3.64, 4.4, 4.75]
  pocket_nvme = [0.99, 1.97, 2.96, 3.83, 4.57, 4.8]
  pocket_ssd = [0.12, 0.24, 0.37, 0.47, 0.6, 0.72]
  pocket_ssd_8xl = [0.49, 0.94, 1.52, 2.1, 2.6, 3.1]
  pocket_hdd = [0.028, 0.064, 0.091, 0.122, 0.151, 0.181]

#  fig = plt.figure(figsize=(15,8))
  fig, ax = plt.subplots(figsize=(15, 8))
#ax  = plt.axes([0.06, 0.2, 0.9, 0.75]) # left bottom width height (fraction of total figsize)
#ax.plot(x, net_alloc, label='Total GB/s allocated', linestyle=':', color="#1f77b4", linewidth=3)
#  ax.plot(x, net_usage, label='Total GB/s used', color="#ff7f0e", linewidth=3)
  ax.plot(x, s3, label='S3', linestyle='--', linewidth=5, color="#d62728")
  ax.plot(x, redis, label='Redis', linewidth=3, color="#ff7f0e", marker='o', markersize=10)
#ax.plot(x, pocket_dram, label='Pocket-DRAM', linewidth=3) #TODO
  ax.plot(x, pocket_dram, label='Pocket-DRAM', linewidth=3, color="#2ca02c", marker='s',
		  markersize=10)
  ax.plot(x, pocket_nvme, label='Pocket-NVMe', linewidth=3, color="#1f77b4", marker='D',
		  markersize=10)
  ax.plot(x, pocket_ssd, label='Pocket-SSD-i2.2xl', linewidth=3, color="#7f7f7f", marker='*',
		  markersize=15)
  ax.plot(x, pocket_ssd_8xl, label='Pocket-SSD-i2-8xl', linewidth=3, color="#7f7f7f", marker='*',
		  linestyle=':', markersize=15)
  ax.plot(x, pocket_hdd, label='Pocket-HDD', linewidth=3, color="#9467bd", marker='.',
		  markersize=15)
  ax.set_xlabel("Number of nodes")
  ax.set_ylabel("Cumulative Throughput (GB/s)")
  ax.legend(loc='upper left', fontsize=20)


#plt.show()
  plt.savefig("throughput-scaling.pdf")


if __name__ == '__main__':
  plot_throughput_scaling()
  
