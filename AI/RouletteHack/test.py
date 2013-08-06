import random
from nltk.util import ngrams
import operator
import log
from blessings import Terminal
t=Terminal()
import matplotlib.pyplot as plt


#print t.bold+t.red+"Roulette Hacker.!!!"+t.normal
#print t.bold+t.blue+"Created By: Juned Munshi\n"+t.normal
ngram_start=2
ngram_end=5


def experiment(threshold):
	trail=1000
	d={'1':0,'0':0}
	stringdata=""
	problist=[]
	for i in range(trail):
		#n=random.random()
		n=random.randint(1,35)
		if n >18:
			d['1']=d['1']+1
			stringdata=stringdata+"1"
		else:
			d['0']=d['0']+1
			stringdata=stringdata+"0"
		problist.append(d['1']/(1.0*(i+1)))
	#plt.plot(problist)
	#plt.ylabel('some numbers')
	#plt.show()
	return {'1':d['1']/(trail*1.0),'0':d['0']/(trail*1.0),'outcome':stringdata}

def getStates(data):
	prob={}
	for j in range(ngram_start,ngram_end):
		generated_ngrams = ngrams(data, j, pad_left=True, pad_right=True, pad_symbol=' ')
		#print generated_ngrams
		#print ''.join(generated_ngrams[4])
		stats={}
		totalgrams=len(generated_ngrams)
		for g in generated_ngrams:
			w=''.join(g)
			if stats.has_key(w):
				stats[w]=stats[w]+1
			else:
				stats[w]=0
		for key,val in stats.items():
			stats[key]=val/(totalgrams*1.0)
		stats_sorted = sorted(stats.iteritems(),\
		                             key=operator.itemgetter(1),\
		                           reverse=True)[0:10]
		print stats_sorted 
		
		for s in stats_sorted:
			prob[s[0]]={'0':0,'1':0,'score':s[1]}
		
		for s in stats_sorted:
		 	for i in range(totalgrams):
		 		w=''.join(generated_ngrams[i])
		 		if w==s[0]:
		 			if i+j <totalgrams:
		 				if generated_ngrams[i+j][0]=='1' or generated_ngrams[i+j][0]=='0':
		 					prob[w][generated_ngrams[i+j][0]]=prob[w][generated_ngrams[i+j][0]]+1

		#prob_sorted = sorted(prob.iteritems(),\
		 #                            key=operator.itemgetter(1),\
		  #                         reverse=True)[0:10]
	return prob

def experiment2():
	outcome=[]
	for i in range(1,10):
		out=experiment(i/(10.0))
		outcome.append(out['1'])
	plt.plot(outcome)
	plt.ylabel('some numbers')
	plt.show()
#experiment2()
exp=experiment(0.5)
#print "1: ",exp['1']," 0: ", exp['0']


prob=getStates(exp['outcome'])

input_data=''
orignalData=[]
#print prob
lastPrediction=''
BetWon=0
Betlost=0
PrevTrueValue=0;
while 1:
	num = raw_input("Please enter last winning number :") 
	orignalData.append(num)
	input_num=num
	if int(input_num)>18 and int(input_num) <37:
		num='1'
	if int(input_num) >-1 and int(input_num) < 19:
		num='0'

	if num =='0' or num=='1':
	
		input_data=input_data+num
		dt=4
		if len(input_data)<4:
			dt=len(input_data)
			
		#" internal",input_data[-dt:]
		print "Last four winning number you have entered ",orignalData[-dt:]
		if dt>2:
			if lastPrediction!= num :
				Betlost=Betlost+1
			else:
				BetWon=BetWon+1
			log.infog("\n"+t.bold+"Bet you won: "+str(BetWon))
			log.err(t.bold+"Bet you lost: "+str(Betlost)+"\n" )
			currentTrueVal=BetWon/(1.0*(BetWon+Betlost))
			print "True Value of wining:",currentTrueVal
			print " Difference of true value:",currentTrueVal-PrevTrueValue
			PrevTrueValue=currentTrueVal
		log.info(t.bold+"\nPrediction:")
		score={'1':0,'0':0}
		pred={}
	

		#log.infog("finalScore",score_sorted)
		for i in range(ngram_start,ngram_end):
			if prob.has_key(input_data[-i:]):
			#	print input_data[-i:],prob[input_data[-i:]]
				score['1']=score['1']+prob[input_data[-i:]]['1']*prob[input_data[-i:]]['score']
				score['0']=score['0']+prob[input_data[-i:]]['0']*prob[input_data[-i:]]['score']
				
		
		total_prob=score['1']+score['0']
		if total_prob>0:
			score['1']=score['1']/(1.0*total_prob)
			score['0']=score['0']/(1.0*total_prob)
		
		log.info("Bet : 19-36 \t Probability of winning : ",score['1'])
		log.info("Bet : 1-18 \t Probability of winning : ",score['0'])
		if score['1']>score['0']:
			log.infog("\n"+t.bold+"Bet on 19-36\n")
			lastPrediction='1'
		elif score['1']<score['0']:
			log.infog("\n"+t.bold+"Bet on 1-18"+"\n")
			lastPrediction='0'
		else:
			lastPrediction='-1'
			log.warn("\nNot enough data to make prediction.At least sequence of last 3 winning number is required.\n")
		
		#score_sorted = sorted(score.iteritems(),\
		#                            key=operator.itemgetter(1),\
		#                       reverse=True)
		#log.infog("finalScore",score_sorted)
	else:
		log.err("Enter valid input")



	