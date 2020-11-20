import pyodbc
import time

database = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-RBC5RA1\SQLEXPRESS;'
                          'Database=hand_gesture_dataset;'
                          'Trusted_Connection=yes;')

cursor = database.cursor()

sqlTable = 'hand_gesture_dataset.dbo.gesture_dataset'

test = time.time()
for i in range(0, 1000):
    aVariable = "ATEST"
    bVariable = "BTEST"
    cVariable = "CTEST"
    cursor.execute("INSERT INTO hand_gesture_dataset.dbo.gesture_dataset VALUES (?, ?, ?)",
                   (aVariable, bVariable, cVariable))
    database.commit()
print("Execution time: %s" % round((time.time() - test), 2), "seconds")

