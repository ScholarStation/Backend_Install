
import json
import urllib2
data = {
       'username': 'qwe12x',
       'password': 'pass1234'
}
print "trying incorrect login"
req = urllib2.Request('http://localhost:3000/LoginApp')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print '******\n\n\n******'


data = {
       'username': 'qwex',
       'password': 'pass1234'
}
print "trying correct login"
req = urllib2.Request('http://localhost:3000/LoginApp')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
KEY = data['KEY']
print data
print '******\n\n\n******'


print "attempting profile retrevial"
req = urllib2.Request('http://localhost:3000/ProfileApp')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print '******\n\n\n******'


print "creating study sessions"
data = {
       'username': 'qwex',
	   'KEY':KEY,
	   'course':'CEN9999',
	   'owner':'qwex',
	   'topic':'stuff and thangs',
	   'date':'2/2/22',
	   'time':'5:00PM',
	   'members':['jasonea','scarecr0w','oldage']
}
req = urllib2.Request('http://localhost:3000/StudyUtility/Create')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
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


print "deleting a study group with ID:" + deleteID
data = {
    '_id':deleteID
}
req = urllib2.Request('http://localhost:3000/StudyUtility/DeleteByID')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data


print "ok done"
