import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2for x in x_values]#used to plot single point scatter graph


plt.style.use('seaborn')
fig, ax = plt.subplots()#generates one or more plots on the same figure,variable ax represents single plot in the figure
ax.scatter(x_values,y_values,s=10,c=y_values, cmap =plt.cm.Blues,)#s to set size of point, each x and y value are passed on as corresponding coordinates, c for colour using a tuple for custom RGB, cmap using a colour map to change the colour as values get higher


#set chart title + axes labels
ax.set_title('Square numbers',fontsize = 24)
ax.set_xlabel('Value',fontsize = 14)
ax.set_ylabel('Square of value',fontsize = 14)

#set the range for each axis
ax.axis([0,1100,0,1100000])

#set size of tick labels (fontsize of values)
ax.tick_params(axis='both',labelsize=14)

plt.show()#opens viewer andd displays plot
