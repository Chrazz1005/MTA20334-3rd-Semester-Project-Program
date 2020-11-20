import pyodbc
import time


class Database:
    database = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-RBC5RA1\SQLEXPRESS;'
                              'Database=hand_gesture_dataset;'
                              'Trusted_Connection=yes;')

    sqlTable = "hand_gesture_dataset.dbo.gesture_dataset"
    sqlTableClean = "gesture_dataset"

    # ----------- How to use -----------
    # addToTable: Will take 1-3 inputs which will be added to the database
    # deleteEntireDatabase: Deletes the entire database (this is non-revertible)
    # resetIdentityField: Resets the id to start from 1
    # showDatabase: Shows the database in the console

    def addToTable(self, x1=0, x2=0, x3=0):
        cursor = self.database.cursor()
        cursor.execute("INSERT INTO " + self.sqlTable + " VALUES (?, ?, ?)", (x1, x2, x3))
        self.database.commit()
        print("Inserted the following into the database")
        print("You inserted the following into the database:")
        print(x1, x2, x3)

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
