from cvxopt.solvers import qp
from cvxopt.base import matrix

import numpy, pylab, random, math

classA = []
classB = []
xs = []

def createData():
	global classA, classB, xs
	classA = [(random.normalvariate(-1.5, 1), random.normalvariate(.5, 1), 1.0) for i in range(10)] + [(random.normalvariate(1.5, 1), random.normalvariate(.5, 1), 1.0) for i in range(10)]
	classB = [(random.normalvariate(0, 0.5), random.normalvariate(-.5, .5),
		   -1.0)
		  for i in range(20)]
	xs = classA + classB
	random.shuffle(xs)


def linearK(x, y):
	s = 1;
	for i in range(2):
		s+= (x[i] * y[i])
	return s

def polyK(x,y,p):
	return pow(linearK(x,y),p)

def radialK(x,y,sigma):
	diff = range(2)
	for i in range(2):
		diff[i] = x[i] - y[i]
	val = 0
	for i in range(2):
		val += diff[i] * diff[i]
	return math.exp(-(val) / (2 * sigma * sigma))

def sigmoidK(x,y,k,delta):
	val = 0;
	for i in range(2):
		val += x[i]*y[i]
	val *= k
	val - delta
	return val

def run(ker):
	pass
#	P = buildP(xs, ker)
#	q = buildq(xs)
#	h = buildh(xs)
#	G = buildG(xs)

if __name__ == "__main__":
	createData()
	run(linearK)
