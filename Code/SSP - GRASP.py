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
		lis = sorted(self.S,reverse=True)
		currentBest = []
		for i in range(0,iterations):
			solution = []
			lis2 = list(lis)
			while len(lis2) != 0:
				choose = random.choice(lis2)
				lis2.remove(choose)
				if (sum(solution) + choose) <= self.t:
					solution.append(choose)
			nghbrhd = [x for x in lis if x not in solution]
			for j in range(0,len(solution)):
				for k in range(0,len(nghbrhd)):
					if len(nghbrhd) == 0:
						return currentBest
					test = list(solution)
					test[j] = nghbrhd[k]
					if abs(self.t - sum(test)) < abs(self.t - sum(solution)):
						solution[j] = nghbrhd[k]
			if abs(self.t - sum(solution)) < abs(self.t - sum(currentBest)):
				currentBest = list(solution)
			del solution[:]
		return currentBest

instance = SSP() #Makes an instance of the class SSP

aver = []
inp = input("Enter 1 for timed, 2 for pretty output and anything else for accuracy: ")
if inp == "1":
	for t in range(1,101):
		for s in range(0,19):
			instance.random_yes_instance(t) #Calls the function random_yes_instance inside the class instance with input of 4
			start_time = time.clock()
			instance.GRASP(10)
			aver.append(time.clock() - start_time)
			#print(aver[-1:])
		print((sum(aver)/20))
		del aver[:]

if inp == "2":
	instance.random_yes_instance(10)
	answer = instance.GRASP(5)
	print("Target: ",instance.t)
	print("Answer: ",sum(answer))
	print("Using: ", answer)
	print("From: ", instance.S)

else:
	for u in range(1,201):
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
