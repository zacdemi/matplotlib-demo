import numpy as np
import matplotlib.pyplot as plt

x = np.arange(9)
#an evening of coding
y_2017 = [91,72,72,70,82,79,81,66,70]
y_2018 = [111,100,81,62,80,84,73,103,77]

#monthly python
y2_2017 = [117,108,115,102,94,139,108,139,125]
y2_2018 = [140,115,0,127,151,62,148,179,156]


fig, (ax1,ax2)  = plt.subplots(nrows=2,ncols=1,sharex=True)

width = 0.35
 
ax1.bar(x,y_2017,width,color='blue',alpha=.5,label="2017")
ax1.bar(x + width,y_2018,width,color='blue',label="2018")
ax1.set_title('An Evening of Python Coding')
ax1.legend()

ax2.bar(x,y2_2017,width,color='red',alpha=.5,label="2017")
ax2.bar(x + width,y2_2018,width,color='red',label="2018")
ax2.set_title('Monthly Python')
ax2.legend()

ax1.set_xticks(x + width / 2)
ax1.set_xticklabels(('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep'))

fig.suptitle('Attendence 2017 vs 2018')
fig.text(0.5, 0.04, 'Months', ha='center')
fig.text(0.04, 0.5, 'Attendence', va='center', rotation='vertical')


plt.show()
