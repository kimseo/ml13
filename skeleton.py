from cvxopt.solvers import qp
from cvxopt.base import matrix
from kernel import linearK
from kernel import polyK
from kernel import radialK
from kernel import sigmoidK
from kernel import sigmoidK
from build import buildP
from build import buildq
from build import buildh
from build import buildG

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

def buildP(xs,ker):
	P = range(len(xs))
	for i in range(len(xs)):
		P[i] = range(len(xs))
		for j in range(len(xs)):
			P[i][j] = xs[i][2]*xs[j][2]*ker(xs[i], xs[j])
	return P

def run(ker):
	pass
#	P = buildP(xs, ker)
#	q = buildq(xs)
#	h = buildh(xs)
#	G = buildG(xs)

if __name__ == "__main__":
	createData()
	run(linearK)
