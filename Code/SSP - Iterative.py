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

	def iterative(self, lngth):
		lis = sorted(self.S,reverse=True) #Sort list large to small
		solution = [] #List for solution
		currentBest = [] #List for current best solution
		for i in range(0, len(lis)): #Loop though all set values
			choose = lis[i] #Select next value
			if (sum(solution) + choose) <= self.t: #If solution + value <= target
				solution.append(choose) #Add chosen value to the solution
		currentBest = list(solution) #make solution current best solution
		external = [x for x in lis if x not in solution] #Fill external list with all set values not in solution
		for j in range(0,len(solution)): #Loop through the solution
			for k in range(0,len(external)): #Loop through the external numbers
				if len(external) == 0: #If external numbers empty
					return currentBest #Return last best
				test = list(solution) #Copy solution to test list
				test[j] = external[k] #Swap value in test solution with external value
				if abs(self.t - sum(test)) < abs(self.t - sum(solution)): #If new test solution is better
					solution[j] = external[k] #Make test solution the new solution
		if abs(self.t - sum(solution)) < abs(self.t - sum(currentBest)): #if solution is better than the best solution
			currentBest = list(solution) #Make solution new better solution
		del solution[:] #Empty solution list
		return currentBest #Return best solution

instance = SSP() #Makes an instance of the class SSP
aver = [] #List for storing items to be averaged
inp = input("Enter 1 for timed, 2 for pretty and anything else for accuracy: ") #Input
if inp == "1":
	for t in range(1,101): #Array length loop
		for s in range(0,19): #Amount of repeats that will be averaged
			instance.random_yes_instance(t) #Calls the function random_yes_instance inside the class instance with input of 4
			start_time = time.clock() #Record starting time
			instance.iterative(t) #Run iterative search
			aver.append(time.clock() - start_time) #record time taken
		print(sum(aver)/20) #Print average of set array length
		del aver[:] #Empty average array
if inp == "2":
	instance.random_yes_instance(10) #Completes one set instance and outputs nicely
	print(instance.t)
	answer = instance.iterative(10)
	print(sum(answer))
	print(answer)
	print(instance.S)
else:
	for u in range(1,201): #Same as array length above but tests average accuracy
		for v in range(0,19):
			instance.random_yes_instance(u)
			if instance.t != 0:
				needed = instance.t
				found = sum(instance.iterative(u))
				aver.append((found/needed)*100)
			else:
				aver.append(100)
		print(sum(aver)/20)
		del aver[:]
