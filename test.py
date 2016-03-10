#Unit test for ScholarStation Node
import json
import urllib2


#incorrect Login Data
data = {
       'username': 'qwe12x',
       'password': 'pass1234'
}
print "trying incorrect login"
#HTTP Request
req = urllib2.Request('http://localhost:3000/LoginApp')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print '******\n\n\n******'

#valid Login Data
data = {
       'username': 'qwex',
       'password': 'pass1234'
}
print "trying correct login"
#HTTP Request
req = urllib2.Request('http://localhost:3000/LoginApp')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
KEY = data['KEY']
#save KEY for later
print data
print '******\n\n\n******'

#using the response, retreive the profile
print "attempting profile retrevial"
#HTTP Request
req = urllib2.Request('http://localhost:3000/ProfileApp')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print '******\n\n\n******'


print "creating study sessions"
#study group that will be used to search members
data = {
       'username': 'qwex',
	   'KEY':KEY,
	   'course':'CEN1111',
	   'owner':'qwex',
	   'topic':'123123stuff and thangs',
	   'date':'12/2/22',
	   'time':'10:00AM',
	   'members':['jasonea','scarecr0w','oldage']
}
#HTTP Request
req = urllib2.Request('http://localhost:3000/StudyUtility/Create')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
#study group with garbage as the members used to search owners 
data = {
       'username': 'qwex',
	   'KEY':KEY,
	   'course':'CEN9999',
	   'owner':'qwex',
	   'topic':'stuff and thangs',
	   'date':'2/2/22',
	   'time':'5:00PM',
	   'members':['asdsdadsa','sGArBAGE DATA','oWEEEEEEe']
}
req = urllib2.Request('http://localhost:3000/StudyUtility/Create')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print '******\n\n\n******'


print "retreiving the study groups! with owner (qwex)"
data = {
       'username': 'qwex',
	   'KEY':KEY,
}
req = urllib2.Request('http://localhost:3000/StudyUtility/GetStudyGroupsByMember')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print '******\n\n\n******'


print "retreiving the study groups! group members (jasonea)"
data = {
       'username': 'jasonea',
	   'password' : 'mongo',
}
req = urllib2.Request('http://localhost:3000/LoginApp')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
jasonLoggedIn = data['validate']
if jasonLoggedIn:
	jasonKEY = data['KEY']
	data = {
       'username': 'jasonea',
	   'KEY':jasonKEY,
	}
	req = urllib2.Request('http://localhost:3000/StudyUtility/GetStudyGroupsByMember')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	data = json.load(response)
	print data
	deleteID = data['studyGroups'][0]['_id']
else:
	print "invalid login for jasonea"
print '******\n\n\n******'


print" attempting to create and find study groups with bad login data"
data = {
       'username': 'jasoneaw3333313rdf',
	   'KEY':"asdasdasdasdasdasd",
}
req = urllib2.Request('http://localhost:3000/StudyUtility/GetStudyGroupsByMember')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
data = {
       'username': 'jasoneaw3333313rdf',
	   'KEY':"asdasdasdasdasdasd",
}
req = urllib2.Request('http://localhost:3000/StudyUtility/Create')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print '******\n\n\n******'


print"editing a study group"
data = {
		'_id':deleteID,
       'username': 'qwex',
	   'KEY':KEY,
	   'course':'AAAA',
	   'owner':'qwex',
	   'topic':'AAAAA',
	   'date':'2aaa',
	   'time':'5aaaaaaa',
	   'members':['jasonea','sGArBAGE DATA','oWEEEEEEe']
}
req = urllib2.Request('http://localhost:3000/StudyUtility/EditByID')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print '******\n\n\n******'


print "deleting a study group with ID:" + deleteID
data = {
	'username': 'qwex',
	'KEY': KEY,
    '_id':deleteID
}
req = urllib2.Request('http://localhost:3000/StudyUtility/DeleteByID')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print "deleting a study group with  bad Key (Should be bad)"
data = {
	'username': 'qwex',
	'KEY': KEY,
    '_id':"aaaaaaaaaaaa111111111111"
}
req = urllib2.Request('http://localhost:3000/StudyUtility/DeleteByID')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print "deleting a study group with  bad Key (Should not get to DB)"
data = {
	'username': 'qwex',
	'KEY': KEY,
    '_id':'asdqwe'
}
req = urllib2.Request('http://localhost:3000/StudyUtility/DeleteByID')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print "deleting a study group with  bad Login (using same _id, should not delete)"
data = {
	'username': 'qwex',
	'KEY': KEY,
    '_id': deleteID
}
req = urllib2.Request('http://localhost:3000/StudyUtility/DeleteByID')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data


print '******\n\n\n******'

print "ok done"
