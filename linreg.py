import sys
import numpy as np
from pyspark import SparkContext
from numpy.linalg import inv

if __name__ == "__main__":
	if len(sys.argv) !=2:
		print >> sys.stderr, "Usage: linreg <datafile>"
		exit(-1)

	sc = SparkContext(appName="LinearRegression")

	# Input yx file has y_i as the first element of each line
	# and the remaining elements constitute x_i
	yxinputFile = sc.textFile(sys.argv[1])

	yxlines = yxinputFile.map(lambda line: line.split(','))
	# calculation of X. X transpose
	def first_term(values):
		values[0] = 1.0
		X = np.asmatrix(np.array(values).astype('float')).T
		#Product of X and X transpose
		return np.multiply(X, X.T)

	# calculation of X.Y matrices
	def second_term(values):
		Y = float(values[0])
		values[0] = 1.0
		X = np.asmatrix(np.array(values).astype('float')).T
		return np.multiply(X, Y)


	# calculating x.x Transpose
	x_xTranspose = yxlines.map(lambda values:("first_term",first_term(values)))

	# running the reducer to sum up app the values of each key and calculating the value
	value_x_xTranspose = x_xTranspose.reduceByKey(lambda x1,x2: np.add(x1,x2)).map(lambda v:v[1]).collect()[0]

	# calculating inverse
	A_inverse= inv(value_x_xTranspose)

	# calculating x.y Transpose
	x_y = yxlines.map(lambda values:("second_term",second_term(values)))

	# running the reducer to sum up app the values of each key and calculating the value
	value_x_y = x_y.reduceByKey(lambda x1,x2: np.add(x1,x2)).map(lambda v:v[1]).collect()[0]
	B = value_x_y

	# calculation of the beta coefficient for the multiple linear regression
	beta_coeff = np.dot(A_inverse, B)
	# print the linear regression coefficients in desired output format
	print "beta: "
	for coeff in beta_coeff:
		print coeff

	sc.stop()

	
	
	

