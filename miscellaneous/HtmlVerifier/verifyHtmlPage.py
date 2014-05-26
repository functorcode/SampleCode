import re
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
	tableDetected=False
	currentTag=''
	parsedData={}
	isFound=False
	currentParsedData={}
	currentDataToCheck={}
	def __init__(self,_dataToCheck):
		self.dataToCheck=_dataToCheck
		HTMLParser.__init__(self)  #need to call supper class  init

	def handle_starttag(self, tag, attrs):
		#print "Encountered the beginning of tag ",tag," with attr ",attrs

		#try to create same data structure as in self.dataTocheck for self.parsedData
		#go up to two level in hierarchy
		self.parseData(self.dataToCheck,self.parsedData,tag,attrs)
		# for key,value in self.dataToCheck.items():
		# 	if key == tag:
		# 		if not self.parsedData.has_key(key):
		# 			self.parsedData[key]=self.getNewElement(value)

		# 		#tmp assigment for easy referece of current tag structure in other functions
		# 		self.currentParsedData=self.parsedData[key]
		# 		self.currentDataToCheck=self.dataToCheck[key]
		# 		self.isFound=True   #process data handle only when we tag we want to check

		# 	else:
		# 		#go second level to find tag ,for eg. th
		# 		for c_key,c_val in value.items():

		# 			if c_key == tag:
		# 				if not self.parsedData[key].has_key(c_key):
		# 					self.parsedData[key][c_key]=self.getNewElement(c_val)

		# 				#tmp assignement for easy reference
		# 				self.currentParsedData=self.parsedData[key][c_key]
		# 				self.currentDataToCheck=self.dataToCheck[key][c_key]
		# 				self.isFound=True


		# #add all common attributes
		# if isinstance(self.currentDataToCheck,dict):
		# 	if self.currentDataToCheck.has_key('attr'):

		# 		for key,value in self.currentDataToCheck['attr'].items():
		# 			if (key,value) in attrs:
		# 				self.currentParsedData.setdefault('attr',{})[key]=value

	def parseData(self,_dataToCheck,_parsedData,tag,attrs):
		for key,value in _dataToCheck.items():
			if key == tag:
				if not _parsedData.has_key(key):
					_parsedData[key]=self.getNewElement(value)

				#tmp assigment for easy referece of current tag structure in other functions
				self.currentParsedData=_parsedData[key]
				self.currentDataToCheck=_dataToCheck[key]
				self.isFound=True   #process data handle only when we tag we want to check

			else:
				if isinstance(value,dict):
					if _parsedData.has_key(key):
						self.parseData(value,_parsedData[key],tag,attrs)


		#add all common attributes
		if isinstance(self.currentDataToCheck,dict):
			if self.currentDataToCheck.has_key('attr'):

				for key,value in self.currentDataToCheck['attr'].items():
					if (key,value) in attrs:
						self.currentParsedData.setdefault('attr',{})[key]=value
	def handle_data(self,data):
		
		if self.isFound==True:
			if isinstance(self.currentParsedData,dict):
				if self.currentDataToCheck.has_key('data'):
					self.currentParsedData['data']=data.strip()
			elif isinstance(self.currentParsedData,list):
				
				if data.strip() in self.currentDataToCheck:
					self.currentParsedData.append(data.strip())

	def handle_endtag(self, tag):
		self.currentTag=''
		self.isFound=False
	#	print "Encountered the end of a %s tag" % tag

	def getNewElement(self,value):
		result=[]
		if isinstance(value,dict):
			result={}
		if isinstance(value,list):
			result=[]
		return result

	def is_valid(self,debug):
		if debug==True:
			print "Data to check:", self.dataToCheck
			print "Parsed data:" ,self.parsedData
		return self.dataToCheck==self.parsedData


f=open('test11.html')
data=f.read()
f.close()
#dataToCheck={'title':{'data':'This is test Page'},'table':{'attr':{'id':'jobs'},'th':['Job ID','Maps Completed','Reduce Progress']}}
#dataToCheck={'title':{'data':'This is test Page'},'table':{'attr':{'id':'jobs'},'th':['Job ID','Maps Completed','Reduce Progress']}}
dataToCheck={'table':{ 'td' : {'attr':{'style':"vertical-align: top;background-color:LightGrey;"},'b': ['Type','Size'] } } } 
parser=MyHTMLParser(dataToCheck)
parser.feed(data)
#pass debug=Ture to check what went wrong
isSame= parser.is_valid(debug=True)
print "Output:",isSame
#warning change in order of list element will return False. for eg. ['Reduce Progress','Maps Completed']

