#author:juned munshi
#contact:juned@ymail.com

def read(file):
	wordlist=[]
	with open(file) as f:
		word=f.readline().lower().strip()
		
		while(word):
			if word not in wordlist:
				wordlist.append(word)
			word=f.readline().lower().strip()
			
	return wordlist
