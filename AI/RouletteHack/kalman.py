import matplotlib.pyplot as plt
import random 
x=0.0
p=0.9
r=0.001
def experiment(threshold):
	trail=10
	d={'1':0,'0':0}
	stringdata=""
	problist=[]
	for i in range(trail):
		n=random.random()
		if n >threshold:
			d['1']=d['1']+1
			stringdata=stringdata+"1"
		else:
			d['0']=d['0']+1
			stringdata=stringdata+"0"
		problist.append(d['1']/(1.0*(i+1)))
	plt.plot(problist,'r')
	plt.plot(kallist,'g')
	plt.ylabel('some numbers')
	

	return {'1':d['1']/(trail*1.0),'0':d['0']/(trail*1.0),'outcome':stringdata}
	#return problist
def update(z):
	global x,p,r
	k=p/(p+r)
	x=x+k*(z-x)
	p=(1-k)*p




kallist=[0]
problist=experiment(0.5)
print "1:" ,problist['1']," 0:",problist['0']
plt.show()
# for prob in problist:
# 	update(prob)
# 	kallist.append(x)

# plt.plot(problist,'r')
# plt.plot(kallist,'g')
# plt.ylabel('some numbers')
# plt.show()



