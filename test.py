
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


print "creating a study session"
data = {
       'username': 'qwex',
	   'KEY':KEY,
	   'course':'CEN9999',
	   'owner':'qwex',
	   'topic':'stuff and thangs',
	   'date':'2/2/22',
	   'time':'5:00PM',
	   'members':['asdasdasd','asdqwd','qwrqwrrwqqwrterertyy']
}
req = urllib2.Request('http://localhost:3000/StudyUtility/Create')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
data = json.load(response)
print data
print "ok done"
