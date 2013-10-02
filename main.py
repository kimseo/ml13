import getopt, sys
from cvxopt.solvers import qp
from cvxopt.base import matrix
from kernel import linearK
from kernel import polyK
from kernel import radialK
from kernel import sigmoidK
from build import buildP
from build import buildq
from build import buildh
from build import buildG
from build import buildhWS
from build import buildGWS
import cPickle 
import numpy, pylab, random, math

Xclass = []
Yclass = []
Trainingsets = []

sz = 5 
def create():
	global Xclass, Yclass, Trainingsets
	Xclass = [(random.normalvariate(-1.5, 1), random.normalvariate(.5, 1), 1.0) for i in range(sz)] + [(random.normalvariate(1.5, 1), random.normalvariate(.5, 1), 1.0) for i in range(sz)]
	Yclass = [(random.normalvariate(0, 0.5), random.normalvariate(-.5, .5), -1.0) for i in range(sz*2)]
	Trainingsets = Xclass + Yclass
	random.shuffle(Trainingsets)

def run(ker):
	P = buildP(Trainingsets, ker)
	q = buildq(Trainingsets)
	h = buildh(Trainingsets)
	G = buildG(Trainingsets)
	alphas = callQP(P,q,G,h)
	SVectors = extractSupportVectors(Trainingsets, alphas)
	Plotresult(SVectors, ker)

def runWS(ker):
	P = buildP(Trainingsets, ker)
	q = buildq(Trainingsets)
	h = buildhWS(Trainingsets,slackV)
	G = buildGWS(Trainingsets)
	alphas = callQP(P,q,G,h)
	SVectors = extractSupportVectors(Trainingsets, alphas)
	Plotresult(SVectors, ker)

def callQP(P, q, G, h):
	r = qp(matrix(P), matrix(q,(len(q),1)), matrix(G).T, matrix(h,(len(h),1)))
	alphas = list(r['x'])
	return alphas

def callQPWS(P, q, G, h):
	r = qp(matrix(P), matrix(q,(len(q),1)), matrix(G).T, matrix(h,(len(h),1)))
	alphas = list(r['x'])
	return alphas

def trainingsetShow(A,B):
	pylab.hold(True)
	pylab.plot([p[0] for p in Xclass],[p[1] for p in A],'bo')
	pylab.plot([p[0] for p in Yclass],[p[1] for p in B],'ro')
	pylab.show()

def show(alphas,ker):
	SVectors = PickoutNonzeroAlpha(Trainingsets, alphas)
	Plotresult(SVectors, ker)

# val > 0 : 1.0 or val < 0 : -1.0
def indicate(x, SVectors,ker):
	val = 0
	for i in range(len(SVectors)):
		a,y = SVectors[i]
		val += a * y[2] * ker(x,y)
	return val

def PickoutNonzeroAlpha(Trainingsets, alphas):
	eps = 1e-5 #low threshhold would be fine
	result = []
	for i in range(len(Trainingsets)):
		if abs(alphas[i]) > eps:
			result.append((alphas[i], Trainingsets[i]))
	return result

def Plotresult(SVectors, ker):
	pylab.hold(True)
	pylab.plot([p[0] for p in Xclass],[p[1] for p in Xclass],'bo') #show Xclass
	pylab.plot([p[0] for p in Yclass],[p[1] for p in Yclass],'ro') #show Yclass
	pylab.plot([p[0] for (a,p) in SVectors],[p[1] for (a,p) in SVectors],'kx') #show supportvector

# plot boundary
	x_range = numpy.arange(-4, 4, 0.01)
	y_range = numpy.arange(-4, 4, 0.01)
	grid = matrix([[indicate((x,y), SVectors, ker) for y in y_range] for x in x_range])
	pylab.contour(x_range, y_range, grid,(-1.0, 0.0, 1.0),colors = ('red', 'black', 'green'),linewidths=(1, 3, 1))

	pylab.show()

if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:], "s:vk:vc:vf:vl:v", ["help", "output="])
	except getopt.GetoptError as err:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(2)

	slack = False
	saving = False
	loading = False

	filename = ""
	global slackV
	ker = linearK
	for o, a in opts:
		if o == "-s":
			slack = True
			slackV = int(a)
		elif o == "-k":
			if "linear" == a:
				ker = linearK
			elif "poly" == a:
				ker = polyK
			elif "radial" == a:
				ker = radialK
			elif "sigmoid" == a:
				ker = sigmoidK
		elif o == "-c":
			sz = int(a)
		elif o == "-f":
			saving = True
			filename = str(a)
		elif o == "-l":
			loading = True
			filename = str(a)

	print "size:"+str(sz)+" x 4 = " +str(sz*4)

	if False == loading:
		create()
	else:
		Trainingsets = cPickle.load(open(filename, 'rb'))
		Xclass = cPickle.load(open(filename+"-A", 'rb'))
		Yclass = cPickle.load(open(filename+"-B", 'rb'))

	if False == saving:
		if False == slack:
			run(ker)
		else:
			runWS(linearK)
	else:
		cPickle.dump(Trainingsets, open(filename, 'wb'))
		cPickle.dump(Xclass, open(filename+"-A", 'wb'))
		cPickle.dump(Yclass, open(filename+"-B", 'wb'))
		trainingsetShow(Xclass, Yclass)

