import re
import sys
src=sys.argv[1]#command line arguments
dest=sys.argv[2]
class matcher:
       
	def __init__(self,sr,dr):
		#opeaning file
		self.sr=open(src)
		self.dr=open(dest)
		
		#temp variables
		self.st0=''
		self.st1=''
		self.dt0=''
		self.dt1=''
		
		#dict variables
		self.dict1={}
		self.dict2={}
		
		#list variables
		self.list1= []
		self.list2 = []
				
		
	def ext(self):
		#source file extraction
		try:
		   for line in self.sr: 
			sq = re.search(r'(tempest.*)',line,re.IGNORECASE)
			if sq:
			  result = str(sq.group())
			  result_split = result.split(' ... ')
			  self.st0=result_split[0]#temp
			  self.st1=result_split[1]#temp
			  
			  result_strip = self.st1.strip('\r')
			  self.dict1[self.st0]=result_strip #dict
			  
			  self.list1.append(str(self.st0)+' ... '+str(result_strip))#list
			  
		except IndexError:
			pass
			#destination file extraction
		try:
		   for line in self.dr: 
			sq = re.search(r'(tempest.[a-zA-Z](.*))',line,re.MULTILINE|re.IGNORECASE)
			if sq:
			  result = str(sq.group())
			  result_split = result.split(' ... ')
			  self.dt0=result_split[0]#temp
			  self.dt1=result_split[1]#temp
			  
			  result_strip = self.dt1.strip('\r')
			  self.dict2[self.dt0]=result_strip #dict
			  
			  self.list2.append(str(self.dt0)+' ... '+str(result_strip))#list
			 
		except IndexError:
			print 'no error'
	
	def line_count(self):		
		print "No of lines starting with 'tempest' in Source : ",len(self.dict1)#lines starting with 'tempest' in Source
		print "No of lines starting with 'tempest' in Destination : ",len(self.dict2)#lines starting with 'tempest' in Destination
	
	def line_same(self):# same status
		count=0
		f=open("same.txt",'w+')
		for i in self.list1:
			for j in self.list2:
				if i==j:
					f.writelines(i+'\n')#writing to file
					count+=1
		print "No of lines having status same:", count
		f=0
    
	def line_differ(self): #diff status
		count=0
		f=open("difference.txt",'w+')
		for key in self.dict1:
			for key1 in self.dict2:
				if (key==key1):
					if(self.dict1[key]!=self.dict2[key1]):
						f.writelines(key+'\n')#writing to file
						count=count+1
		print "No of lines having status difference",count
		f=0
	def line_any(self):# ANY STATUS
		  #source dif count
		  f=open("any.txt",'w+')
		  count=0  
		  for key in self.dict1:
			 if (self.dict1[key]!='ok')&(self.dict1[key]!='FAIL'):
			   f.writelines(key+'\n')#writing to file
			   count=count+1		   
		#destination dif count	
		  count1=0
		  for key in self.dict2:    
			if(self.dict2[key]!='ok')&(self.dict2[key]!='FAIL'):
			  f.writelines(key+'\n')#writing to file
			  count1=count1+1
		#add both difference count
		  print "No of lines having status anything",count+count1
		  f=0
	def line_source(self):#first to second
		count=0
		f=open("fns.txt",'w+')
		for key in self.dict1:
			if self.dict2.has_key(key):
				continue
			else:
				f.writelines(key+'\n')#writing to file
				count=count+1
		print "No of lines available in source not in destination",count
		f=0
	def line_destination(self):#second to first
		count=0
		f=open("snf.txt",'w+')
		for key in self.dict2:
			if self.dict1.has_key(key):
				continue
			else:
				f.writelines(key+'\n')#writing to file
				count=count+1
		print "No of lines available in destination not in source",count
		f=0
a=matcher(src,dest)#calling class
#calling def
a.ext()
a.line_count()
a.line_same()
a.line_differ()
a.line_any()
a.line_source()
a.line_destination()