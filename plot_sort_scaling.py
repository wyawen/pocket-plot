import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 24})
fig, ax = plt.subplots(figsize=(20, 7))

N = 3 # number of groups on x-axis

ind = np.arange(N)  # the x locations for the groups
#ind = np.array([0.8,1])
print ind
width = 0.25      # the width of the bars
w = 0.05

#		250	500	1000 workers
reflex_1 = [10.67+9.49, 5.18+4.76, 2.93+2.54] #s3 read + s3 write
reflex_2 = [2.61+14.21, 1.34+6.65, 0.68+3.00] # map compute + reduce compute 
reflex_3 = [9.74+11, 4.24+4.84, 2.42+2.56] #shuffle data write + read

reflex_data=[reflex_1, reflex_2, reflex_3]
reflex=[] #12x10Gbps (i3.2xlarge) + 2 m5.2xlarge namenodes
for i in xrange(len(reflex_data)):
    reflex.append(reflex_data[i])
reflex_bottom = []
tmp = [0,0,0]
for i in reflex:
    tmp = np.array(i)+np.array(tmp)
    reflex_bottom.append(tmp)



#		250	500	1000 workers
redis_1 = [9.97+11.75, 4.5+5.5, 2.7+3.4] #s3 read + s3 write 
redis_2 = [2.62+14.42, 1.36+6.46, 0.69+2.97]  # map compute + reduce compute 
redis_3 = [10.86+6.11, 5.79+2.21, 2.48+1.13] #shuffle data write + read 

redis_data=[redis_1, redis_2, redis_3]
redis=[] #12x10Gbps 
for i in xrange(len(redis_data)):
    redis.append(redis_data[i])
redis_bottom = []
tmp = [0,0,0]
for i in redis:
    tmp = np.array(i)+np.array(tmp)
    redis_bottom.append(tmp)


s3_1=[21.40, 0, 0] #s3 read + s3 write
s3_2=[2.48+13.63, 0, 0] #map compute + reduce compute
s3_3=[33.27+27.03,0,0] #shuffle data write + read
s3=[]
s3.append(s3_1)
s3.append(s3_2)
s3.append(s3_3)
s3_bottom = []
tmp = [0,0,0]
for i in s3:
    tmp = np.array(i)+np.array(tmp)
    s3_bottom.append(tmp)

#plt.rcParams.update({'font.size': 24})
#plt.rcParams.update({'font.size': 28})
#fig, ax = plt.subplots()
#fig, ax = plt.subplots(figsize=(18, 10))
#fig, ax = plt.subplots(figsize=(16, 8))
##fig.tight_layout()

c_b = '#1f77b4'
c_r = '#d62728'
c_y = '#bcbd22'
c_o = '#ff7f0e'
c_g = '#2ca02c'
c_p = '#9467bd'
c_pink = '#e377c2'
c = [c_b, c_o, c_y, c_p, c_r, c_g]
p = []
h = ['/','.','x','//','-','o']

ind_0 = ind-(width)/2-w
ind_1 = ind+(width)/2
ind_2 = ind+(width)*3/2+w

p0 = ax.bar(ind_0, s3_1, width, color=c_p, hatch='x')
p0_1 = ax.bar(ind_0, s3_2, width, color=c_g, hatch='.', bottom=s3_bottom[0])
p0_2 = ax.bar(ind_0, s3_3, width, color=c_b, hatch='/', bottom=s3_bottom[1])
#p0_3 = ax.bar(ind_0, s3_4, width, color=c_g, hatch='o', bottom=s3_bottom[2])

p1 = ax.bar(ind_1, redis_1, width, color=c_p,hatch='x')
p1_1 = ax.bar(ind_1, redis_2, width, color=c_g, hatch='.', bottom=redis_bottom[0])
p1_2 = ax.bar(ind_1, redis_3, width, color=c_b, hatch='/', bottom=redis_bottom[1])
#p1_3 = ax.bar(ind_1, redis_4, width, color=c_g, hatch='o', bottom=redis_bottom[2])

p2 = ax.bar(ind_2, reflex_1, width, color=c_p, hatch='x')
p2_1 = ax.bar(ind_2, reflex_2, width, color=c_g, hatch='.', bottom=reflex_bottom[0])
p2_2 = ax.bar(ind_2, reflex_3, width, color=c_b, hatch='/', bottom=reflex_bottom[1])
#p2_3 = ax.bar(ind_2, reflex_4, width, color=c_g, hatch='o', bottom=reflex_bottom[2])

#ax.set_title('100GB Sort')
ax.set_ylabel('Average Time per Lambda (s)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('           S3      Redis  Pocket-NVMe \n250 lambdas', 
					'                      Redis   Pocket-NVMe \n500 lambdas',
					'                   Redis  Pocket-NVMe \n1000 lambdas'), fontsize=20)
#ax.set_xticklabels(('           S3      Redis  Crail-ReFlex \n250 lambdas', '                      Redis   Crail-ReFlex \n500 lambdas', '                      Redis   Crail-ReFlex \n1000 lambdas'), fontsize=20)
#ax.set_xlabel('# of Lambdas Workers')
ax.legend((p1[0], p1_1[0], p1_2[0]), ('S3 I/O','Compute','Ephemeral Data I/O'),fontsize=24)
#ax.legend((p1[0], p1_1[0], p0_2[0], p1_2[0], p2_2[0], p3_2[0]), ('Input/Ouput','Compute','S3 R/W','Redis R/W 8x25Gbps', 'Redis R/W 4x10Gbps', 'Redis R/W 4x25Gbps'))
plt.show()

#for tick in ax.get_xticklabels():
#    tick.set_rotation(45)
fig.savefig("plots/sort-barplot-execution-time.pdf")
