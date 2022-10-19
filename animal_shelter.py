from pymongo import MongoClient



class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self,username,password):   
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        # init connect to mongodb with authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:52840/?authMechanism=DEFAULT&authSource=AAC'%("aacuser", "luna123"))
        # init connect to mongodb without authentication                        
        # self.client = MongoClient('mongodb://localhost:52840')
        self.database = self.client['AAC']
        
        
        
        
# Method to implement the C in CRUD.
    def create(self,data):
        if data is not None:
            self.database.animals.insert(data) # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty.")
            return False      
            
            
# Method to implement the R in CRUD.
    def read(self,data):
        return self.database.animals.find_one(data) ## return only one document as a python dictionary
        raise Exception("Data not found. Please check parameters.")
                  
            
    def read_all(self,data):
        if data:
            cursor = self.database.animals.find(data, {'_id':False} ) 
        else:
            cursor = self.database.animals.find({}, {'_id':False} ) 
            
        return cursor #Return a curser which a pointer to a list of results(Documents)
    
    
# Method to implement the U in CRUD.  
    def update(self,old,new):
        if old is not None:
            if self.database.animals.count_documents(old) != 0:
                if self.database.animals.count_documents(old) == 1:
                    updateOne = self.database.animals.update_one(old, {"$set": new})
                    resultUO = updateOne.raw_result
                    return print(resultUO)
                if self.database.animals.count_documents(old) >= 2:
                    updateMany = self.database.animals.update_many(old, {"$set": new})
                    resultUM = updateMany.raw_result
                    return print(resultUM)
            elif self.database.animals.count_documents(old) == 0:
                print("No results. Please try different parameters.")
        else:
            raise Exception("Could not update. Please check parameters and try again.")
        
    
    
# Method to implement the D in CRUD.    
    def delete(self,search):
        if search is not None:
            if self.database.animals.count_documents(search) != 0:
                if self.database.animals.count_documents(search) == 1:
                    deleteOne = self.database.animals.delete_one(search)
                    resultDO = deleteOne.raw_result
                    return print(resultDO)
                if self.database.animals.count_documents(search) >= 2:
                    deleteMany = self.database.animals.delete_many(search)
                    resultDM = deleteMany.raw_result
                    return print(resultDM)
            elif self.database.animals.count_documents(search) == 0:
                print("No results. Please try different parameters.")   
        else:
            raise Exception("Could not update. Please check parameters and try again.")
            
    
    

            
            
            
            
            
          