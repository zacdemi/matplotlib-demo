import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [111,100,81,62,80,84,73,103,93]
y2 = [140,115,None,127,151,62,148,179,156]

fig, ax = plt.subplots()

line1, = ax.plot(x,y)
line2, = ax.plot(x,y2)

#format line 1
line1.set_color('b')
line1.set_marker('o')
line1.set_linewidth(2)
line1.set_linestyle('-')
line1.set_label('an evening of python')

#format line 2
line2.set_color('r')
line2.set_marker('o')
line2.set_linewidth(2)
line2.set_linestyle('--')
line2.set_label('monthly python')

#format axes
ax.set_ylabel('Attendees')
ax.set_xlabel('Months')
ax.set_title('Python Meetup Attendence')
ax.legend()

plt.show()
