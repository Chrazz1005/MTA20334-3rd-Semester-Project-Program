import pymongo
import pyodbc
import time


class Database:
    # ----------- How to use -----------
    # addToTable: Will take 1-3 inputs which will be added to the database
    # deleteEntireDatabase: Deletes the entire database (this is non-revertible)
    # resetIdentityField: Resets the id to start from 1
    # showDatabase: Shows the database in the console

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
                "mongodb+srv://" + userName + ":" + userPassword + "@cluster0.jqbtc.mongodb.net/3rd_semester_project?retryWrites=true"
                                                                   "&w=majority")
            print("Connection established.")
        except:
            print("Connection failed.")

        self.database = self.client["hand_gesture_data"]
        self.databaseCollection = self.database["3rd_semester_project"]

    def addToTable(self, x1=0, x2=0, x3=0):
        cursor = self.database.cursor()
        cursor.execute("INSERT INTO " + self.sqlTable + " VALUES (?, ?, ?)", (x1, x2, x3))
        self.database.commit()
        print("Inserted the following into the database")
        print("You inserted the following into the database:")
        print(x1, x2, x3)

    def mdbAdd(self, x1=0, x2=0, x3=0):
        dataToInsert = {
            "A": x1,
            "B": x2,
            "C": x3
        }
        self.databaseCollection.insert_one(dataToInsert)

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
