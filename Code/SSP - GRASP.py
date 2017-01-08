from random import randint, sample
from itertools import chain, combinations
import time
import random
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

	def GRASP(self, iterations):
		lis = sorted(self.S,reverse=True) #Sort list largest to smallest
		currentBest = [] #List for current best solution
		for i in range(0,iterations): #Loop for amount of iterations
			solution = [] #Solution list
			lis2 = list(lis) #Copy set
			while len(lis2) != 0: #While set is not empty
				choose = random.choice(lis2) #Select element at random
				lis2.remove(choose) #Remove chosen element
				if (sum(solution) + choose) <= self.t: #If solution add chosen is less than or equal to the target
					solution.append(choose) #Add element to solution
			nghbrhd = [x for x in lis if x not in solution] #Fill neighbourhood with elements not in solution
			for j in range(0,len(solution)): #For length of solution
				for k in range(0,len(nghbrhd)): #For length of neighbourhood
					if len(nghbrhd) == 0: #If neighbourhood is empty
						return currentBest #Return best solution
					test = list(solution) #Create a test solution list from current solution
					test[j] = nghbrhd[k] #Replace value in test solution with value from neighbourhood
					if abs(self.t - sum(test)) < abs(self.t - sum(solution)): #If new test solution is better than solution
						solution[j] = nghbrhd[k] #Make solution the same as test solution
			if abs(self.t - sum(solution)) < abs(self.t - sum(currentBest)): #If solution is better than the current best solution
				currentBest = list(solution) #Make current best equal to new solution
			del solution[:] #Empty solution list
		return currentBest #Return best solution

instance = SSP() #Makes an instance of the class SSP

aver = [] #List to store values to be averaged
inp = input("Enter 1 for timed, 2 for pretty output and anything else for accuracy: ")
if inp == "1":
	for t in range(1,101): #Array length timed testing
		for s in range(0,19):
			instance.random_yes_instance(t) #Calls the function random_yes_instance inside the class instance with input of 4
			start_time = time.clock()
			instance.GRASP(10)
			aver.append(time.clock() - start_time)
			#print(aver[-1:])
		print((sum(aver)/20))
		del aver[:]

if inp == "2":
	instance.random_yes_instance(10) #Single instance prettified output
	answer = instance.GRASP(5)
	print("Target: ",instance.t)
	print("Answer: ",sum(answer))
	print("Using: ", answer)
	print("From: ", instance.S)

else:
	for u in range(1,201): #Average accuracy test
		for v in range(0,19):
			instance.random_yes_instance(u)
			if instance.t != 0:
				needed = instance.t
				found = sum(instance.GRASP(5))
				aver.append((found/needed)*100)
			else:
				aver.append(100)
		print(sum(aver)/20)
		del aver[:]
