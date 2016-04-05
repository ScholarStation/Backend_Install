//runs in the Mongo Terminal and creates the necessary collections
conn = new Mongo();
db = conn.getDB("SS");


db.createCollection( "login",
   {
      validator: { $and:
		[
            { username: { $type: "string" } },
            { password: { $type: "string" } },
			{permissionLevel: {$type: "string"}}
		
            
         ]
      },
	  validationLevel: "strict",
	  validationAction: "error"
   }
)

db.createCollection( "uniquekey",
   {
      validator: { $and:
		[
            { username: { $type: "string" } },
            { KEY: { $type: "string" } },
			{permissionLevel: {$type: "string"}},
			{expiration: {$type: "string"}}
				
			
            
         ]
      },
	  validationLevel: "strict",
	  validationAction: "error"
   }
)


db.createCollection( "profile",
   {
      validator: { $and:
		[
            { fname:{$type: "string"}},
			{ lname:{$type: "string"}},
			{ age:{$type: "int"}},
			{ gender:{$type: "string"}},
			{ email:{$type: "string"}},
			{ year:{$type: "string"}},
			{ major:{$type: "string"}},
			{ username:{$type: "string"}}
		
            
         ]
      },
	  validationLevel: "strict",
	  validationAction: "error"
   }
)
db.createCollection("study",
	{
		validator: { $and:
		[
			{ course:{$type: "string"}},
			{ owner:{$type: "string"}},
			{ members:{$type: "string"}},
			{ time:{$type: "string"}},
			{ date:{$type: "string"}},
			{ time:{$type: "string"}},
			{ topic:{$type: "string"}},
			{ course:{$type: "string"}},
			{ publicView:{$type: "boolean"}}
				
		]
	  },
	  validationLevel: "strict",
	  validationAction: "error"
	}
)

db.createCollection("courseList",
	{
		validator: { $and:
		[
			{ courseName:{$type: "string"}}
		]
	  },
	  validationLevel: "strict",
	  validationAction: "error"
	}
)