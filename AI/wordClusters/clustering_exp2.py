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
for i in range(50):
	sysnet.setdefault(i,{'word':words[i],'sysnet':wn.synsets(words[i])})
	vectWords.append(i)


totalElement=len(vectWords)
totalClusters=10
distMatrix=numpy.ones((totalElement,totalElement),dtype=float)
for i in range(totalElement):
	for j in range(totalElement):
		distMatrix[i,j]=getDistance(i,j)

clusters=Pycluster.kmedoids(distMatrix,nclusters=totalClusters,npass=100)
print distMatrix
print clusters
groups={}
for i in range(len(clusters[0])):
	if clusters[0][i]<totalClusters :
		groups.setdefault(clusters[0][i],[]).append(sysnet[i]['word'])

for key,value in groups.items():
	print "\n***********************************\n"
	for v in value:
		print v
		
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
