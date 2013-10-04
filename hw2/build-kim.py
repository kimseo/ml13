# N x N
def buildP(xs,ker):
	P = range(len(xs))
	for i in range(len(xs)):
		P[i] = range(len(xs))
		for j in range(len(xs)):
			P[i][j] = xs[i][2]*xs[j][2]*ker(xs[i], xs[j])
	return P

# N x 1
def buildq(xs):
	q = range(len(xs))
	for i in range(len(xs)):
		q[i] = -1.0
	return q

# N x 1
def buildh(xs):
	h = range(len(xs))
	for i in range(len(xs)):
		h[i] = 0.0
	return h

# N x N
def buildG(xs):
	G = range(len(xs))
	for i in range(len(xs)):
		G[i] = range(len(xs))
		for j in range(len(xs)):
			if i == j:
				G[i][j] = -1.0
			else:
				G[i][j] = 0.0
	return G

# N x N with SlackV
def buildhWS(xs,C=100):
	print "SlackV " + str(C)
	h = range(2*len(xs))
	for i in range(len(xs)):
		h[i] = 0.0
	for i in range(len(xs)):
		h[len(xs)+i] = C
	return h

# N x N with SlackV
def buildGWS(xs):
	G = range(2*len(xs))
	for i in range(len(xs)):
		G[i] = range(len(xs))
		for j in range(len(xs)):
			if i == j:
				G[i][j] = -1.0
			else:
				G[i][j] = 0.0
	for i in range(len(xs)):
		G[len(xs)+i] = range(len(xs))
		for j in range(len(xs)):
			if i == j:
				G[len(xs)+i][j] = 1.0
			else:
				G[len(xs)+i][j] = 0.0
	return G

