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
	def random_yes_instance(self, n, bitlength):
		max_n_bit_number = 2**bitlength-1
		self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
		self.t = sum( sample(self.S, randint(0,n)) )
		self.n = len( self.S )


	"""Tests whether a random subset of numbers in S can be equal to t when summed"""
	def try_at_random(self):
		candidate = []
		total = 0
		while total != self.t:
			candidate = sample(self.S, randint(0,self.n))
			total     = sum(candidate)
			print( "Trying: ", candidate, ", sum:", total )

	"""Dynamic search to find if problem can be completed"""
	def dynamic(self):
		lis = list(self.S) #Create a copy of the list
		n = len(self.S) #Length of the main set
		su = self.t #The target number
		sub = [[0 for x in range(n+1)] for y in range(su+1)] #Fill 2D list with correct number of sapces for the problem
		for i in range(0,n+1): #For the amount of numbers in the main set
			sub[0][i] = True #Set first column to true
		for j in range(1, su+1): #For amount of columns
			sub[j][0] = False #Set all other values to false as placeholder
		for k in range(1, su+1): #For amount of columns
			for l in range(1,n+1): #For amount of rows
				sub[k][l] = sub[k][l-1] #Make value eqaul to one above it
				if k >= lis[l-1]: #If column is more than or equal to point in rows in the main set
					sub[k][l] = sub[k][l] | sub[k - lis[l-1]][l-1] #make equal to point or one up and back 
		return sub[su][n] #Return true or false for final point

instance = SSP() #Makes an instance of the class SSP
aver = [] #Array for storing times
inp = input("Enter 1 for bitlength, anything else for amount of numbers: ")
if inp == "1":
	for t in range(1,21): #Amount of numbers created
		for s in range(0,19): #Number of repeats of same amount of numbers
			instance.random_yes_instance(10, t) #Calls the function random_yes_instance inside the class instance with input of t
			start_time = time.time() #Record start time
			instance.dynamic() #Run dynamic search
			aver.append(time.time() - start_time) #Add time taken to list
			#print(aver[-1:]) #Print time taken
		print('average of ',t,' bitlength - ',(sum(aver)/20)) #Make average of times and print
		del aver[:] #Empty List

else:
	for u in range(1,100): #Amount of numbers created
		for s in range(0,19): #Number of repeats of same amount of numbers
			instance.random_yes_instance(u, 10) #Calls the function random_yes_instance inside the class instance with input of t
			start_time = time.time() #Record start time
			instance.dynamic() #Run dynamic search
			aver.append(time.time() - start_time) #Add time taken to list
			#print(aver[-1:]) #Print time taken
		print('average of ',u,' numbers - ',(sum(aver)/20)) #Make average of times and print
		del aver[:] #Empty list
