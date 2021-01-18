from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#create 2 die
die_1 = Die()
die_2 = Die()

results = [die_1.roll()*die_2.roll() for roll_num in range(50_000)]

#analysis of results
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1,max_result+1)]


#visualise results
x_values = list(range(1, max_result+1))#must be list or plotly wont accept
data =[Bar(x=x_values, y=frequencies)]#a list of each axis data set

x_axis_config = {'title': 'Result', 'dtick':1}#dtick contols tick spacing
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling and multiplying two D6 50,000 times',
                   xaxis = x_axis_config, yaxis = y_axis_config)#will return the object for layout plotly will use
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d6.html')#offline requires dictionary with data and layout objects and name for file outside dictionary
