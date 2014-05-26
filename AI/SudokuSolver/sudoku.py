#author:Juned Munshi
#contact: juned@ymail.com

from backtrack import *
from board import *
import time
import copy
import pygame

class sudoku:
	variable=[]
	values=[x for x in range(1,10)]
	domain={}
	initState={}
	def  __init__(self,fileName):
		initState=self.readFromFile(fileName)
		self.initState=initState
		for i in range(9):
			for j in range(9):
				self.variable.append((i,j))
		
		for var in self.variable:
			self.domain.setdefault(var,copy.copy(self.values))
		for key,value in initState.items():
			self.domain[key]=[copy.copy(value)]
	def readFromFile(self,fileName):
		puzzle=open(fileName,'r')
		initState={}
		for i_X in range(9):
			line=puzzle.readline().split(" ")
			for j_Y in line:
				if int(j_Y) in range(1,9):
					initState[(line.index(j_Y),i_X)]=int(j_Y)
		
		return initState		
	def isGoal(self,asignment):
		for var in self.variable:
			if not asignment.has_key(var):
				return False
			
		return True;

	def getVariables(self):
		return self.variable


	def getValues(self,var):
		return self.domain[var]

	def getAllNeighbors(self,var):
		neighbors=[]
		neighbors=self.getrowNeighbors(var)
		neighbors+=self.getcolNeighbors(var)
		neighbors+=self.getblockNeighbors(var)
		return neighbors

	def isConsistant(self,var,value,asignment):
		if (self.checkConstrain(self.getrowNeighbors(var),var,value,asignment)==False):
			return False
		if (self.checkConstrain(self.getcolNeighbors(var),var,value,asignment)==False):
			return False
		if (self.checkConstrain(self.getblockNeighbors(var),var,value,asignment)==False):
			return False
		
		return True;

	def getrowNeighbors(self,var):
		neigh=[]
		for i in range(9):
			if(i!=var[1]):
				v=(var[0],i)
				neigh.append(v)
		return neigh
	def getcolNeighbors(self,var):
		neigh=[]
		for i in range(9):
			if(i!=var[0]):
				v=(i,var[1])
				neigh.append(v)
		return neigh

	def getblockNeighbors(self,var):
		neigh=[]
		sec_x=var[0]/3
		sec_y=var[1]/3
		
		for i in range(sec_x*3,sec_x*3+3):
			for j in range(sec_y*3,sec_y*3+3):
				
				if (i,j)!=var:
					neigh.append((i,j))
		return neigh		
	
	def checkConstrain(self,neighbors,var,value,asignment):
		for neigh in neighbors:
			if(asignment.has_key(neigh)):
				if asignment[neigh]==value:
					return False;
		return True


