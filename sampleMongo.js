//Will make sample profile, username and password
conn = new Mongo();
db = conn.getDB("SS");
var a  = {
	"fname":"Ben",
	"lname":"Churchill",
	"age":21,
	"gender":"whitehorse",
	"email":"bjc37@students.uwf.edu",
	"year":"senior",
	"major":"SE",
	"username":"qwex"
};
db.profile.save(a);
var a  = {
	"fname":"Branden",
	"lname":"Poe",
	"age":22,
	"gender":"foxspirit",
	"email":"bmp18@students.uwf.edu",
	"year":"senior",
	"major":"SE",
	"username":"scarecr0w"
};
db.profile.save(a);
var a  = {
	"fname":"Jonathan",
	"lname":"Rogers",
	"age":21,
	"gender":"whiteman",
	"email":"jmr76@students.uwf.edu",
	"year":"senior",
	"major":"SE",
	"username":"oldage"
};
db.profile.save(a);
var a = {
	"fname":"Jason",
	"lname":"Monforton",
	"age":24,
	"gender":"whiteman",
	"email":"jem75@students.uwf.edu",
	"year":"senior",
	"major":"CIS",
	"username":"jasonea"
};
db.profile.save(a);
var a = {
	"fname":"Michael",
	"lname":"Caine",
	"age":27,
	"gender":"bigbull",
	"email":"mjc15@students.uwf.edu",
	"year":"something",
	"major":"SE",
	"username":"hamhock"
};
db.profile.save(a);
var b = {
	"username":"qwex",
	"password":"pass1234"
};
db.login.save(b);
var b = {
	"username":"scaresc0w",
	"password":"password"
};
db.login.save(b);
var b = {
	"username":"jasonea",
	"password":"mongo"
};
db.login.save(b);
var b = {
	"username":"hancock",
	"password":"h4ckm3"
};
db.login.save(b);
var b = {
	"username":"oldage",
	"password":"password"
};
db.login.save(b);
