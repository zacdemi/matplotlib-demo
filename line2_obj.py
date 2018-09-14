import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [111,100,81,62,80,84,73,103,77]
y2 = [140,115,None,127,151,62,148,179,156]

fig, ax = plt.subplots()

ax.plot(x,y,'bo-',linewidth=2,label='an evening of python')
ax.plot(x,y2,'ro--',linewidth=2,label='monthly python')

ax.set_ylabel('Members')
ax.set_xlabel('Months')
ax.set_title('Python Meetup Attendence')
ax.legend()

plt.show()

#---------------------------------------
fmt = '[color][marker][line]'

'b'    # blue markers with default shape
'ro'   # red circles
'g-'   # green solid line
'--'   # dashed line with default color
'k^:'  # black triangle_up markers connected by a dotted line
