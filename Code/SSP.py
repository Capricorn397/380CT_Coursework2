from random import randint, sample
from itertools import chain, combinations
from time import time
import numpy as np
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

	def exhaustive(self):
		s = self.S
		power_set=[[]]
		for elem in s:
			# iterate over the sub sets so far
			for sub_set in power_set:
				# add a new subset consisting of the subset at hand added elem
				power_set=power_set+[list(sub_set)+[elem]]
				result = [sum(power_set[i]) for i in range(len(power_set))]
				if result[i] == self.t:
					return True
		return False


instance = SSP() #Makes an instance of the class SSP
instance.random_yes_instance(4) #Calls the function random_yes_instance inside the class instance with input of 4
print( instance ) #Outputs the cast of the instance of the class SSP
print(instance.exhaustive())
#instance.try_at_random() #Calls the try_at_random function with the instance of the class SSP
