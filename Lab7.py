# 1st part lab for 03/29/17

import matplotlib.pyplot as plt
import numpy as np


# can use lambda to declare functions
class Graph():

	def __init__(self,funk=lambda x: x):
		# self stores variable to Graph class
		self.funk = funk


	def plot(self,name):
		# This plots the function given to the Graph class in its own unique .png file
	
		x = np.arange(0,5,0.1)
		y = []

		for i in x:
			y.append(self.funk(i))

		plt.title(name)
		plt.xlabel("x, independent variable")
		plt.ylabel("y, independent variable")
		xmin, xmax = 0,5
		ymin, ymax = 0,10
		plt.axis([xmin,xmax,ymin,ymax])

		plt.plot(x,y)
		fig = plt.gcf()
		plt.show()
		fig.savefig(name + ".png")

# g1 = Graph()
# g1.plot("title")
