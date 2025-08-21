from pymongo import MongoClient


class DAL_atlas_mongo:

    def __init__(self, user, password, database, collection):
        self.URI = f"mongodb+srv://{user}:{password}@{database}.gurutam.mongodb.net/"
        self.database = database
        self.collection = collection
        self.client = None


    def open_connection(self):
        try:
            self.client = MongoClient(self.URI)
            self.client.admin.command("ping")
            return True
        except Exception as e:
            self.client = None
            print("Error: ", e)
            return False


    def get_all(self):
        if self.client:
            db = self.client[self.database]
            collection = db[self.collection]
            data = collection.find({}, {"_id": 0})
            return list(data)


    def close_connection(self):
        if self.client:
            self.client.close()

# dal = DAL_atlas_mongo("IRGC", "iraniraniran", "IranMalDB", "tweets")
# dal.open_connection()
# data = dal.get_all()
# print(data)
# dal.close_connection()