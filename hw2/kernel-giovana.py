import math

def linearK(x, y):
	for i in range(2):
		r += x[i] * y[i]
	return r + 1

def polyK(x, y, p):
	r = 1;
	for i in range(2):
		r += x[i] * y[i]
	return pow(r, p)
	
def radialK(x, y, sigma):
	for i in range(2):
		d[i] = x[i] - y[i]
	for i in range(2):
		num += d[i] * d[i]
	den = 2 * sigma * sigma
	return math.exp(- num / den)
	
def sigmoidK(x, y, k, delta):
	for i in range(2):
		r += x[i] * y[i]
	r *= k
	r -= delta
	return math.tanh(r)
