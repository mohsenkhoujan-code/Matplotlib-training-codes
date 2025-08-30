# pro1
from matplotlib import pyplot as plt
from SCo import Scource
import numpy as np
x = np.array([1,2,3,4])

src = Scource()
src.impment()
src.netm()

jk = []
for _ in range(10):
    jk.append(_)
    src.proxy()
    
src.part()
y = [12312,1234223,123123,21412]

fig = plt.figure()
ax = fig.subplots(ncols=1,nrows=1)
sors = src.index
labs = src.columns
print(sors)
ax.set_xticks(ticks=[1,2,3,4])
ax.set_xticklabels(labels=labs)
ax.bar(x,sors)

fig1 = plt.figure()
ax1 = fig1.subplots(ncols=1,nrows=1)
#ax1.set_xticks(ticks=[0,20,40,60,80,100])
#ax1.fill_between(jk,src.toli)
ax1.plot(jk,src.toli,marker='o')
fig2 = plt.figure()
ax2 = fig2.subplots(ncols=1,nrows=1)
ax2.pie(sors,labels=labs)

fig3 = plt.figure()
ax3 = fig3.subplots(ncols=1,nrows=1)
ax3.boxplot([src.mdam,src.hemo,src.tahg,src.toli],labels=labs)

fig4 = plt.figure()
ax4 = fig4.subplots(ncols=1,nrows=1)
ax4.stem(src.mdam)
;
