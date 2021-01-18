from random import choice

class RandomWalk:
    """a class to generate random walks"""

    def __init__(self,num_points = 5000):
        """init attributes of walk"""
        self.num_points = num_points

        #all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all points on the walk"""
        while len(self.x_values)< self.num_points:#keep taking steps until wak reaches desired length

            x_direction = choice([20, -20])#choice of left or right
            x_distance = choice([0,2,4])#how far does this travel
            x_step = x_direction * x_distance

            y_direction = choice([0.1, -0.1])#choice of up or down
            y_distance = choice ([0,1,3])
            y_step = y_direction * y_distance

            if x_step ==0 and y_step ==0:#continue if no movement to ignore move so it isnt plotted and mess up results
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
