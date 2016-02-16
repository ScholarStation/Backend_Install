//runs in the Mongo Terminal and creates the necessary collections
conn = new Mongo();
db = conn.getDB("SS");


db.createCollection( "login",
   {
      validator: { $or:
		[
            { username: { $type: "string" } },
            { password: { $type: "string" } }
		
            
         ]
      },
	  validationLevel: "strict",
	  validationAction: "error"
   }
)

db.createCollection( "uniquekey",
   {
      validator: { $or:
		[
            { username: { $type: "string" } },
            { KEY: { $type: "string" } }
		
            
         ]
      },
	  validationLevel: "strict",
	  validationAction: "error"
   }
)


db.createCollection( "profile",
   {
      validator: { $or:
		[
            { fname:{$type: "string"}},
			{ lname:{$type: "string"}},
			{ age:{$type: "string"}},
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
		validator: { $or:
		[
			{ owner:{$type: "string"}},
			{ members:{$type: "string"}},
			{ time:{$type: "string"}},
			{ topic:{$type: "string"}},
			{ class:{$type: "string"}}
		]
	  },
	  validationLevel: "strict",
	  validationAction: "error"
	}
)