from Lab7 import Graph

def f(x):
	return x**2
f3 = lambda x: 1/(x+.000000001)
g1 = Graph()
g1.plot("Literally Linear")

g2 = Graph(f)
g2.plot("quadRADICAL")

g3 = Graph(f3)
g3.plot("Inversely Awesome")