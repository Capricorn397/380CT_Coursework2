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

	def exhaustive(self):
		s = self.S #Create pointer to list
		power_set=[[]] #Create 2D list for power set
		for elem in s: #Loop to fill power set
			for sub_set in power_set: #Loop through subsets
				power_set=power_set+[list(sub_set)+[elem]] #Add subset from current subset with elem added
				result = [sum(power_set[i]) for i in range(len(power_set))] #Create summed list
				for j in range(len(result)): #Loop through summed values
					if result[j] == self.t: #Test if summed value is equal to target
						return True #If equal return true
		return False #If no answer found return false


instance = SSP() #Makes an instance of the class SSP
aver = [] #List of time taken
for t in range(1,20): #Array length increasing
	for s in range(0,19): #Amount of repeats per array length
		instance.random_yes_instance(t) #Calls the function random_yes_instance inside the class instance with input of t
		start_time = time.time() #Record start time
		instance.exhaustive() #runs exhaustive search on current instance
		aver.append(time.time() - start_time) #Record time taken
		#print(aver[-1:]) #print time taken
	print('average of ',t,' numbers - ',(sum(aver)/20)) #Print average of time taken for a set array length
	del aver[:] #Empty average list
