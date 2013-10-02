from cvxopt.solvers import qp
from cvxopt.base import matrix

import numpy, pylab, random, math

def linearK(x, y):
	s = 1;
	for i in range(2):
		s+= (x[i] * y[i])
	return s

def polyK(x,y,p=10):
	return pow(linearK(x,y),p)

def radialK(x,y,sigma=5):
	diff = range(2)
	for i in range(2):
		diff[i] = x[i] - y[i]
	val = 0
	for i in range(2):
		val += diff[i] * diff[i]
	return math.exp(-(val) / (2 * sigma * sigma))

def sigmoidK(x,y,k=2,delta=0.1):
	val = 0;
	for i in range(2):
		val += x[i]*y[i]
	val *= k
	val -= delta
#	return val
#	return math.tanh(val)

