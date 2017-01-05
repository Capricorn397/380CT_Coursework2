from random import randint, sample
from itertools import chain, combinations
import time
"""The Class Itself"""
class SSP():
	"""Creating the objects needed for the class (Constructors)"""
	def __init__(self, S=[], t=0):
		self.S = S
		self.t = t
		self.n = len(S)
		self.decision = False
		self.total    = 0
		self.selected = []

	"""Casting any outputs of the class"""
	def __repr__(self):
		return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)

	"""Creates a defined amount of random numbers in array S and generates a random goal t"""
	def random_instance(self, n, bitlength=10):
		max_n_bit_number = 2**bitlength-1
		self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
		self.t = randint(0,n*max_n_bit_number)
		self.n = len( self.S )

	"""Creates a defined amount of numbers in array S and creates a total (t) from the sum of a random subset of the numbers in S"""
	def random_yes_instance(self, n, bitlength=10):
		max_n_bit_number = 2**bitlength-1
		self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
		self.t = sum( sample(self.S, randint(0,n)) )
		self.n = len( self.S )
		###

	"""Tests whether a random subset of numbers in S can be equal to t when summed"""
	def try_at_random(self):
		candidate = []
		total = 0
		while total != self.t:
			candidate = sample(self.S, randint(0,self.n))
			total     = sum(candidate)
			print( "Trying: ", candidate, ", sum:", total )

	def dynamic(self):
		lis = list(self.S)
		n = len(self.S)
		su = self.t
		print(su)
		sub = [[0 for x in range(n+1)] for y in range(su+1)]
		for i in range(0,n+1):
			sub[0][i] = True
		for j in range(1, su+1):
			sub[j][0] = False
		for k in range(1, su+1):
			for l in range(1,n+1):
				sub[k][l] = sub[k][l-1]
				if k >= lis[l-1]:
					sub[k][l] = sub[k][l] | sub[k - lis[l-1]][l-1]
		return sub[su][n]
instance = SSP() #Makes an instance of the class SSP
#instance.random_yes_instance(4)
#print(instance.dynamic())
aver = []
for t in range(1,20):
	for s in range(0,19):
		instance.random_yes_instance(t) #Calls the function random_yes_instance inside the class instance with input of 4
		#print( instance ) #Outputs the cast of the instance of the class SSP
		#print(instance.dynamic([], 0, 0, True))
		start_time = time.time()
		instance.dynamic()
		aver.append(time.time() - start_time)
		print(aver[-1:])
	print('average of ',t,' numbers - ',(sum(aver)/20))
	del aver[:]
