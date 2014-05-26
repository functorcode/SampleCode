import os
import re
import readwordlist
import networkx as nx
import pygraphviz
from nltk.corpus import wordnet as wn
from networkx import graphviz_layout


#code ref: www2.imm.dtu.dk/pubdb/views/edoc_download.php/6120/pdf
#		   http://nltk.googlecode.com/svn/trunk/doc/book/ch04.html	
def traverse(graph,start,node=None,level=0):
	
	if not node:
		node=start
		
	graph.depth[nodename(node.name)]=node.shortest_path_distance(start)
	if(level>maxDepth):
		return
	level=level+1
	
	for child in node.hypernyms():
		graph.add_edge(nodename(child.name),nodename(node.name))
		traverse(graph,start,child,level)

def nodename(name):
	return re.sub("_"," ",re.sub("\..*","",name)).capitalize()



def drawGraph(G,words,layout):
	A = nx.to_agraph(G)

	for n in A.nodes():
		
		if str(n).lower() in words:
			
			n.attr['color']='green'
	A.layout(layout, args='-Nfontsize=10 -Nwidth=".2" -Nheight=".2" -Nmargin=0 -Gfontsize=8')
	A.draw('graph_'+str(layout)+'.png')
	

#max depth for traverser
maxDepth=1000
#max number of words to load
limit=10

layout=['neato','dot','twopi','circo','fdp'] 	
G=nx.DiGraph()

G.depth={}
#read words from file
words=readwordlist.read("rt_words.csv")
counter=0;

for word in words:
	if counter>limit:
		break
	counter=counter+1
	for syn in wn.synsets(word):
		traverse(G,syn)

#draw 
drawGraph(G,words,layout[1])


