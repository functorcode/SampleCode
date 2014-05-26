import urllib,urllib2,json
import glob,os
import mapq
import csv
import time
import datetime
class FileUtil:
	def loadJsonFile(name):
		f=open(name,'r')
		json_data=json.loads(f.read())
		f.close()
		return json_data

class Angellist:
	locationUtil=None
	verbose=0
	jobFolder=''
	jobDb=[]
	def __init__(self,angelJobFolder,locationObject,verbose=0):
		self.verbose=verbose
		self.locationUtil=locationObject
		self.jobFolder=angelJobFolder
	def loadJobDb(self,fileName):
		f=open(fileName,'r')
		self.jobDb=json.loads(f.read())
		f.close()
	def saveJobDb(self,fileName):
		f=open(fileName,'w')
		f.write(json.dumps(self.jobDb),indent=4)
		f.close()

	def parseJobs(self,jobs):
		jobslist=[]
		for job in jobs['jobs']:
			jobdict={}
			jobdict['title']=str(job['title'].encode('utf-8'))
			jobdict['skills']=[]
			jobdict['location']={'name':'','lang':'','lat':''}
			for tag in job['tags']:
				if tag['tag_type']=='SkillTag':
					jobdict['skills'].append(str(tag['name'].encode('utf-8')))
				if tag['tag_type']=='LocationTag':
					orignalName=str(tag['name'].encode('utf-8'))
					jobdict['location']['orignalName']=orignalName
			jobslist.append(jobdict)
		return jobslist
	def buildDbFromRaw(self):
		for infile in glob.glob( os.path.join(self.jobFolder+"/", '*.json') ):
		 
			if self.verbose==1:
				print "Reading :",infile
			f=open(infile,"r")    
			json_data=json.loads(f.read())
			jlist=self.parseJobs(json_data)
			self.jobDb=self.jobDb+jlist
			f.close()
			loclist=[]
			for job in self.jobDb:
				if job['location'].has_key('orignalName'):
					loclist.append(job['location']['orignalName'])


		result=self.locationUtil.scrapLocationData(loclist)
		for job in self.jobDb:
			if job['location'].has_key('orignalName'):
				oname=job['location']['orignalName']
				locInfo=result[oname]
				job['location']=locInfo
				job['location']['orignalName']=oname

	def scrapJobs(self,maxScrapCount):
		startPage=1
		lastPage=10
		cpage=startPage
		while cpage<=lastPage or cpage<=maxScrapCount:
			url="https://api.angel.co/1/jobs/?page="+str(cpage)
			try:
				print "Fetching job page "+str(cpage)
				response = urllib2.urlopen(url)

				json_data = json.loads(response.read())
				f=open(self.jobFolder+"/"+str(cpage)+".json",'w')
				f.write(json.dumps(json_data,indent=4))
				f.close()
				if cpage==1:
					lastPage=json_data['last_page']
				
			#print json.dumps(json_data)
				#return json_data
			except:
				print "Failed to get jobs"
				#return None
			cpage=cpage+1


class LocationUtil:
	database=[]
	verbose=0
	locationFolder=""
	mapQuestKey='Fmjtd%7Cluub206rn1%2Cb5%3Do5-9ubau6'
	
	def __init__(self,locationFolder,verbose=0):
		self.locationFolder=locationFolder;
		self.verbose=verbose
		mapq.key(self.mapQuestKey)
	def loadLocationDb(self,fileName):
		f=open(fileName,'r')
		self.database=json.loads(f.read())
		f.close()
	def saveLocationDb(self,fileName):
		f=open(fileName,'w')
		f.write(json.dumps(self.database,indent=4))
		f.close()

	def dumpCSV(self,saveFile):
		
		fs=open(saveFile,'w')
		fs.write('Lat\tLang\tCity\tState\tCounty\tCountry\tStreet\n')
		for locInfo in self.database:
			formatedString='%(lat)s\t%(lang)s\t%(city)s\t%(state)s\t%(county)s\t%(country)s\t%(street)s\n'%locInfo
			fs.write(formatedString)
		fs.close()
	def buildDbFromRaw(self):
		for infile in glob.glob( os.path.join(self.locationFolder+"/", '*.json') ):
		 
			if self.verbose==1:
				print "Reading :",infile
			f=open(infile,"r")    
			data=json.loads(f.read())
			loc=self.parseLocation(data)
			self.database.append(loc)
			f.close()
			

	def searchInDb(self,location,delimiter=','):
		locPart=location.split(delimiter)
		for l in self.database:
			for part in locPart:
				p=part.replace(' ','').lower()
				if len(locPart)==1:
					for key,value in l.items():
						if p==value.replace(' ','').lower():
							return l

				elif p==l['street'].replace(' ','').lower():
					return l
				elif p==l['city'].replace(' ','').lower():
					return l
		if self.verbose==1:
			print "No match found:",location
		return False
	
	def parseLocation(self,locationData):
		adminArea={'adminArea1Type':'adminArea1','adminArea2Type':'adminArea2','adminArea3Type':'adminArea3',
					'adminArea4Type':'adminArea4','adminArea5Type':'adminArea5','adminArea6Type':'adminArea6'}
		locInfo={'street':'None','city':'None','state':'None',
				'county':'None','country':'None','lat':'None','lang':'None'}
		data=locationData
		#parse location detail, at= areatype , an=areaname
		for at,an in adminArea.items():
			if data.has_key(at):
				val=data[an].encode('utf-8')
				if data[at]=='City':
					locInfo['city']=str(val)
				if data[at]=='State':
					locInfo['state']=str(val)
				if data[at]=='County' :
					locInfo['county']=str(val)
				if data[at]=='Country':
					locInfo['country']=str(val)
				if data[at]=='Street':
					locInfo['street']=str(val)
		locInfo['lat']=str(data['latLng']['lat'])
		locInfo['lang']=str(data['latLng']['lng'])
		return locInfo

		
	def scrapLocationData(self,locationList):
		loclist=[]
		result={}
		#f=open(fileName,'w');
		counter=0;
		todayStamp=str(datetime.date.today())
		failed=[]
		for l in locationList:

			if not result.has_key(l)  and not l in failed:
				search=self.searchInDb(l)
				if search== False:
					try:
						print "fetching data.."+l
						locinfo=mapq.geocode(l)
						result[l]=locinfo
						#f.write(l+"\t"+str(locdict[l]['latLng']['lat'])+"\t"+str(locdict[l]['latLng']['lng'])+"\n")
						filename=l.replace(' ','').lower()+"_"+"_"+todayStamp+".json"
						x=open(self.locationFolder+"/"+filename,"w")
						x.write(json.dumps(locinfo))
						x.close()
						locdata=self.parseLocation(locinfo)
						loclist.append(locdata)
						counter=counter+1
					except Exception,e:
						print "failed:"+l
						print str(e)
						failed.append(l)
				else:
					result[l]=search
		#f.close()
		self.database=self.database+loclist
		return result

	




def query(jobList, skill):
	results={}
	for job in jobList :
		if skill in job['skills'] :
			if job['location']['name'] != '':
				if results.has_key(job['location']['name']):
					results[job['location']['name']]['count']=results[job['location']['name']]['count']+1
				else:
					results[job['location']['name']]={}
					results[job['location']['name']]['count']=1
					results[job['location']['name']]['lat']=job['location']['lat']
					results[job['location']['name']]['lang']=job['location']['lang']
	return results

def formatgJson(jobdata):
	result='eqfeed_callback({"type":"FeatureCollection","features":['
	for key, value in jobdata.items():
		data='{"type":"Feature","properties":{"count":'+str(value['count'])+',"name":"'+key+'"}'
		data=data+',"geometry":{"type":"Point","coordinates":['+str(value['lat'])+','+str(value['lang'])+']}'
		data=data+'},\n'
		result=result+data 
	result=result+']})'

	return result


locUtil=LocationUtil('/home/juned/Code/talentdemand/location/',verbose=1)
locUtil.buildDbFromRaw()
locUtil.saveLocationDb('locationDb.json')
#locUtil.loadLocationDb('locationDb.json')
angelJob=Angellist('/home/juned/Code/talentdemand/angelListJobs/',locUtil,verbose=1)
angelJob.buildDbFromRaw()
angelJob.saveJobDb("angleJobsDb.json")
#locUtil.buildDbFromRaw()
#print locUtil.database
#locUtil.saveLocationDb('locationDb.json')
#locUtil.dumpCSV('locationDb.csv')
		
#locToCSV('/home/juned/Code/talentdemand/location/','location.csv')
# joblist=jobsFromFiles('/home/juned/Code/talentdemand/angelListJobs/')
# locationInfo=locationCSV('location.csv')
# for job in joblist:
	
# 	if locationInfo.has_key(job['location']['name']):
# 		cord=locationInfo[job['location']['name']]
# 		job['location']['lat']=cord['lat']
# 		job['location']['lang']=cord['lang']

# print formatgJson(query(joblist, 'nlp'))
#getJobs('/home/juned/Code/talentdemand/angelListJobs/')
# joblist=[]
# jobs=loadFile('angellist.data')
# joblist=parseData(jobs)
#locationlist=[]
#for job in joblist:
# 	locationlist.append(job['location']['name'])

#buildLocationData(locationlist,'location.csv','location')