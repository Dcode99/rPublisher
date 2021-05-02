import pymongo #mongodb library - may need to be installed

client = pymongo.MongoClient("<hostname>:<port>",
                            username = "",
                            password = "",
                            authSource = "<databasename>",
                            authMechanism = "SCRAM-SHA-256") #default mechanism for current version of mongodb

distances = client["<databasename>"] #Why does database name need to be referenced twice? Cause for concern.

