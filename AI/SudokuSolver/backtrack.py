#author:Juned Munshi
#contact: juned@ymail.com


import copy
domainStack=[]
def bts(asignment,csp,actions):

	if csp.isGoal(asignment):
		return asignment
	
	var=getNextVariable(asignment,csp)
	
	
	#print "dstack",domainStack
	for value in csp.getValues(var):
		if csp.isConsistant(var,value,asignment):
			asignment[var]=value
			actions.append(["a",[var,value]])
		
			#domainStack.append(csp.domain)
			#if forwordChecking(var,value,asignment,csp) ==False:
				#csp.domain=domainStack.pop()
			#	actions.append(["r",[var,value]])
			#	del asignment[var]
			#	break

			result = bts(asignment,csp,actions)

			if result!=False :
				return result
			else:
			#	csp.domain=domainStack.pop()
				actions.append(["r",[var,value]])
				del asignment[var]
	#csp.domain=copy.deepcopy(domainStack.pop())
	return False

def forwordChecking(var,value,asignment,csp):
	neigh=csp.getAllNeighbors(var)
	csp.domain[var]=[value]

	for n in neigh:
		if asignment.has_key(n):
			continue
		if value in csp.getValues(n):
			csp.domain[n].remove(value)
		if len(csp.getValues(n))==0:
			print "\hell"
			return False
	
	return True

def getNextVariable(asignment,csp):
	for var in csp.getVariables():
		if not asignment.has_key(var):
			return var 
	
def getNextVariable1(asignment,csp):
		valueCount={}
		result=()
		for key,value in csp.domain.items():
			if not asignment.has_key(key):
				result=key
				valueCount.setdefault(key,len(value))
		min_value=len(csp.values)+1
		for key,value in valueCount.items():
			if value<min_value :
				result=key
				min_value=value
		
		return result
		
				
				
		

		


