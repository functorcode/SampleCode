#author:Juned Munshi
#contact: juned@ymail.com


#Colorfill is simple constrain satisfaction problem. Algorithm should feel color in the box such that two adjacent box should not have
#same color.  
#this program is just to check that backtracking algorithm is working.


from backtrack import *
import copy
class fillColor:
	variable=[(1,1),(1,2),(2,1),(2,2)]
	values=['r','g']
	domain={}
	def  __init__(self):
		for var in self.variable:
			self.domain.setdefault(var,copy.copy(self.values))
		
	def isGoal(self,asignment):
		for var in self.variable:
			if not asignment.has_key(var):
				return False
			
		return True;
	def getVariables(self):
		return self.variable
	def getValues(self,var):
		return self.domain[var]

	def isConsistant(self,var,value,asignment):
		result=self.adjustancyConstrain(var,value,asignment)
		return result;
	def getAllNeighbors(self,var):
		return self.getAdjNeighbors(var)
	def getAdjNeighbors(self,var):
		neigh=[]
		for v in self.variable:
			dist_x= abs(v[0]-var[0])
			dist_y=abs(v[1]-var[1])
			if dist_x+dist_y ==1 :
				neigh.append(v)
		return neigh

	def adjustancyConstrain(self,var,value,asignment):
		neighbors=self.getAdjNeighbors(var)
		#print neighbors
		for neigh in neighbors:
			if(asignment.has_key(neigh)):
				if asignment[neigh]==value:
					return False;
		return True


fc=fillColor()
print bts({},fc,[])
#asignment={(1, 2): 'g', (1, 1): 'r'}
#print fc.adjustancyConstrain((2,1),'g',asignment)
