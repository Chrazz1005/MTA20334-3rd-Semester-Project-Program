import cv2
import numpy as np
import xlsxwriter
from MTA20334_Version_2_Slow.EuclideanDistance import *


class DataCollection:
    workbook = xlsxwriter.Workbook('DataCollection.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'ID:')
    worksheet.write('B1', 'Gesture Sequence:')
    worksheet.write('C1', 'Gestures Output:')
    worksheet.write('D1', 'Aspect Ratio:')
    worksheet.write('E1', 'Compactness:')
    worksheet.write('F1', 'MaxHeightRelation:')
    worksheet.write('G1', 'MaxRelation:')
    worksheet.write('H1', 'VerticalSizeRatio:')
    worksheet.write('I1', 'HorizontalSizeRatio:')
    worksheet.write('J1', 'Hit & Miss:')
    worksheet.write('K1', 'Hits:')
    worksheet.write('L1', 'Misses:')
    worksheet.write('M1', 'Accuracy:')
    content = []
    aspList = []
    cmpList = []
    mhrList = []
    mrList = []
    vsrList = []
    hsrList = []

    bbColumn = 3
    bbRow = 1

    def __init__(self):
        pass

    def gestureSequence(self):
        gestureColumn = 1
        gestureRow = 1
        content = ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B",
                   "C", "A", "B", "C", "A", "B", "C", "A", "B", "C", ]

        for value in content:
            self.worksheet.write(gestureRow, gestureColumn, value)
            gestureRow += 1

    def idColumn(self):
        uId = 1
        uIdColumn = 0
        uIdRow = 1

        for value in range(0, 30, 1):
            self.worksheet.write(uIdRow, uIdColumn, uId)
            uIdRow += 1
            uId += 1

    def aspColumnFnc(self):
        aspRow = 1
        aspColumn = 3

        for value in self.aspList:
            self.worksheet.write(aspRow, aspColumn, value)
            aspRow += 1

    def cmpColumnFnc(self):
        cmpRow = 1
        cmpColumn = 4

        for value in self.cmpList:
            self.worksheet.write(cmpRow, cmpColumn, value)
            cmpRow += 1

    def mhrColumnFnc(self):
        mhrRow = 1
        mhrColumn = 5

        for value in self.mhrList:
            self.worksheet.write(mhrRow, mhrColumn, value)
            mhrRow += 1

    def mrColumnFnc(self):
        mrRow = 1
        mrColumn = 6

        for value in self.mrList:
            self.worksheet.write(mrRow, mrColumn, value)
            mrRow += 1

    def vsrColumnFnc(self):
        vsrRow = 1
        vsrColumn = 7

        for value in self.vsrList:
            self.worksheet.write(vsrRow, vsrColumn, value)
            vsrRow += 1

    def hsrColumnFnc(self):
        hsrRow = 1
        hsrColumn = 8

        for value in self.hsrList:
            self.worksheet.write(hsrRow, hsrColumn, value)
            hsrRow += 1

    def hitMissColumn(self):
        hmRow = 1
        hmColumn = 9

        for value in range(2, len(self.content)+2, 1):
            self.worksheet.write(hmRow, hmColumn, "=EXACT(B" + str(value) + ",C" + str(value) + ")")
            hmRow += 1

    def hitsColumn(self):
        hitRow = 1
        hitColumn = 10

        self.worksheet.write(hitRow, hitColumn, "=COUNTIF(J2:J31,TRUE)")

    def missColumn(self):
        missRow = 1
        missColumn = 11

        self.worksheet.write(missRow, missColumn, "=COUNTIF(J2:J31,FALSE)")

    def accuracyColumn(self):
        acRow = 1
        acColumn = 12

        self.worksheet.write(acRow, acColumn, "=K2/A31")

    def dataCollector(self):
        row = 1
        column = 2

        for value in self.content:
            self.worksheet.write(row, column, value)
            row += 1

    def closeDocument(self):
        self.workbook.close()

    def startDataCollection(self):
        self.gestureSequence()
        self.idColumn()
