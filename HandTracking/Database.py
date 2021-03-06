import pymongo
import pyodbc
import time


class Database:
    # ----------- How to use -----------
    # addToTable: Will take 1-3 inputs which will be added to the database
    # deleteEntireDatabase: Deletes the entire database (this is non-revertible)
    # resetIdentityField: Resets the id to start from 1
    # showDatabase: Shows the database in the console

    databaseName = "gesture_database"

    def __init__(self):
        userName = input("DB Username: ")
        userPassword = input("DB Password: ")
        try:
            print("-------- Connection --------")
            print("Name:", userName)
            print("Password:", userPassword)
            print("----------------------------")
            print("Attempting to connect database..")
            self.client = pymongo.MongoClient(
                "mongodb+srv://" + userName + ":" + userPassword + "@cluster0.4cszv.mongodb.net/" + self.databaseName +
                                                                   "?retryWrites=true&w=majority")
            print("Connection established.")
        except:
            print("Connection failed.")

        self.database = self.client["gesture_database"]
        self.databaseCollection = self.database["3rd_semester_project"]

    # def addToTable(self, x1=0, x2=0, x3=0):
    #     cursor = self.database.cursor()
    #     cursor.execute("INSERT INTO " + self.sqlTable + " VALUES (?, ?, ?)", (x1, x2, x3))
    #     self.database.commit()
    #     print("Inserted the following into the database")
    #     print("You inserted the following into the database:")
    #     print(x1, x2, x3)

    def mdbAdd(self, dbId=1, x1=0, x2=0, x3=0, x4=0, x5=0, x6=0):
        dataToInsert = {
            "_id": dbId,
            "A_COMPACTNESS": x1,
            "A_ASPECTRATIO": x2,
            "B_COMPACTNESS": x3,
            "B_ASPECTRATIO": x4,
            "C_COMPACTNESS": x5,
            "C_ASPECTRATIO": x6
        }
        self.databaseCollection.insert_one(dataToInsert)

    def mbDelete(self):
        deletedDocuments = self.databaseCollection.delete_many({})
        print(deletedDocuments.deleted_count, "Documents were deleted.")

    def deleteEntireDatabase(self):
        cursor = self.database.cursor()
        userInput = input("Database: Are you fucking sure? (y/n)")
        if userInput == "y":
            cursor.execute("DELETE FROM " + self.sqlTable)
            self.database.commit()
            print("Deleted the database successfully.")
        else:
            print("Aight ending....")

    def resetIdentityField(self):
        cursor = self.database.cursor()
        cursor.execute("DBCC CHECKIDENT(" + self.sqlTableClean + ", RESEED, 0)")
        self.database.commit()

    def showDatabase(self):
        cursor = self.database.cursor()
        cursor.execute("SELECT * FROM " + self.sqlTable)
        sqlResult = cursor.fetchall()
        for results in sqlResult:
            print(results)