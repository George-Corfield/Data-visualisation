import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:#keep making new walks, as long as program is active
    rw = RandomWalk(5_000)#call fill walk from random walk module
    rw.fill_walk()

    #plotting points of walk
    plt.style.use('classic')
    fig, ax = plt.subplots()#tuple for figsize gives it the size in inches (1 inch == 100 pixels on most systems) but dpi lets you fix this if needed
    point_numbers = range(rw.num_points)#using point numbers so the cmap tracks the start to end 
    ax.plot(rw.x_values, rw.y_values, linewidth = 1)

    #empasising the start and end
    ax.scatter(0,0, c='green', edgecolors = 'none', s=100)#start of (0,0)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors = 'none', s= 100)#end point of last point in each list (x,y)

    #Remove the axes
    ax.get_xaxis().set_visible(False)#make axes labels invisble so it doesnt distract from walk
    ax.get_yaxis().set_visible(False)

    
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running =='n':
        break
           
