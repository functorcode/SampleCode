#author:juned munshi
#contact: juned@ymail.com

#This is experimental project to create group of simillar words from given wordlist.




import numpy
from numpy.random import rand
import readwordlist
from nltk.corpus import wordnet as wn
import Pycluster

sysnet={}

def getDistance(n1,n2):
	global sysnet
	ns1=sysnet[n1]['sysnet']
	ns2=sysnet[n2]['sysnet']
	max_sim=0
	for _ns1 in ns1:
		for _ns2 in ns2:
			sim=_ns1.wup_similarity(_ns2)
			if sim>max_sim:
				max_sim=sim
	if max_sim>1:
		print max_sim
	return 1-max_sim


def vectorize(data):
	max_len=0
	for i in data:
		l=len(i)
		if l>max_len:
			max_len=l
	
	for i in data:
		if len(i)<max_len:
			for m in range(max_len-len(i)):
				i.append(0)
	return data

def findclusters(data,treedepth):
	#data=vectorize(data)
	Y=pdist(data,similarity)
	Z=linkage(Y,method="average",metric="centroid")
	dendrogram(Z)
	return fcluster(Z,t=0.7,depth=treedepth)

	
words=readwordlist.read("rt_words.csv")
vectWords=[]
for i in range(1000):
	sysnet.setdefault(i,{'word':words[i],'sysnet':wn.synsets(words[i])})
	vectWords.append(i)


totalElement=len(vectWords)
clusters={}
itteration=3
clusterCount=0;
distMatrix=numpy.ones((totalElement,totalElement),dtype=float)
for i in range(totalElement):
	for j in range(0,i):
		distMatrix[i,j]=getDistance(i,j)
		distMatrix[j,i]=distMatrix[i,j]
		
for i in range(itteration):
	print "itteration:",i
	for v in vectWords:
		matched=0
		#print clusters
		for key,value in clusters.items():
			if not v in value:
				l_value=[]
				for wor in value:
					dist=distMatrix[v,wor]
					if(dist<0.3):
						l_value.append(v)
						matched=1
						continue
					if matched==1:
						continue
				for l in l_value:
					if l not in value:
						clusters.setdefault(key,[]).append(l)
			else:
				matched=1
		if matched==0:
			clusters.setdefault(clusterCount,[]).append(v)
			clusterCount=clusterCount+1

	


#print clusters

print "****GroupWords****"
for key,value in clusters.items():
	if len(value)>1:
		for v in value:
			print sysnet[v]['word']
		print "\n***********************************\n"

print "\n\n"
print "*************Unclassified Words ************ "
for key,value in clusters.items():
	if len(value)==1:
		for v in value:
			print sysnet[v]['word']

		
#print findclusters(vectWords,100)
#plt.show()




#X = rand(10,100)
# X=[[1,2,3],[1,2],[2,3,5]]
#X[0:5,:] *= 2
# Y = pdist(X,similarity)
# print Y
# print squareform(Y)
# Z = linkage(Y,method='weighted')
# print Z
# print fcluster(Z,0.5)
# dendrogram(Z)
# plt.show()


#links=[[1,2,3],[1,2],[5,2,3],[2,4,5]]
#print findclusters(links,2)
#plt.show()
