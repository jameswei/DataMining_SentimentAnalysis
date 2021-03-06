"""
    Created by: Karen C. Aragon
    Senior Research Project

    Description: script coverts emotion sentences_tags
        into binary values and puts 24bit binary encodin
        into the postsData database

    TO DO:
        put dictionary into mysql database


    are we losing features we wanted to cluster?

"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import csv

con = None

try:

    con = mdb.connect('localhost','root', 
       'rachoes123','postsData');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    data = cur.fetchone()
    print "Database version : %s " % data

    cur.execute("SELECT sentenceID, tagID, annotatorID FROM sentences_tags ORDER BY sentenceID, annotatorID ASC")
    rows = cur.fetchall()

    #get number of rows
    numrows = int(cur.rowcount)
    printNumber of rows: + str(numrows) +\n'

    sentenceAnnotDict = {}
    percentValueDict = {}
    binaryAnnotDict = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}

    binaryValue = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    percentValue = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #tag id -1
    tagNamesDict = {1:"INTR",2:"VALI",3:"AFFE",4:"GRAT",5:"PEAC" ,
                6:"EXJD" ,7:"PRID" ,8:"HUMR" ,9:"THMR" ,10:"TENS" ,
                11:"FEAR" ,12:"SADN" ,13:"FRST" ,14:"ANG" ,15:"CONT" ,
                16:"DOMI" ,17:"BELL", 18:"DEFN", 19:"DISG" ,20:"STON" ,
                21:"WHIN" ,22:"SHME" ,23:"GILT" ,24:"EMBR"}

    """
        for each sentence replace annotatorID's tags with binary value
    """
    for annotator in binaryAnnotDict:
        binaryAnnotDict[annotator] = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    """
        for each sentence count the number of 1's at each index
        and divide by 24 (the number of emotions)
    """
    def percentageOfEmotion(percentValueDict):
        count = 0
        index = 0

        for k,values in percentValueDict.iteritems():
            count = count + values[index]
            print count
            percent[index] = count
            index = index + 1
        return percent


    sentenceID = rows0]0]
    annotatorID = rows0][2]
    # cycle through rows
    for row in rows:
        # if new sentences
        if row0] != sentenceID:
            # new sentence
            sentenceID = row0]
            # new annotator
            annotatorID = row[2]
            binaryValue = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # if new annotator
        elif row[2] != annotatorID:
            annotatorID = row[2]
            binaryValue = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        # cycle through emotions
        for key in tagNamesDict:
            # if tagID from db is in emotion tags
            if row[1] in tagNamesDict:
                # convert to binary encoding (id -1)
                binaryValue[row[1]-1] = 1
                binaryAnnotDict[row[2]] = binaryValue
                # add binaryDict to sentenceDict
                sentenceAnnotDict[row0]] = binaryAnnotDict.items()
                # if new annotator same as previous annotator for same sentence
       
    #print sorted(sentenceAnnotDict.items())


    count = 0
    index = 0
    
    writer = csv.writer(open('percent.csv',wb)
    # print sentenceAnnotDict[166506][2][1][7]

    for k in sorted(sentenceAnnotDict.iterkeys()):
        print k
        for index in xrange(24):
            for x in xrange(12):
                #print sentenceAnnotDict[k][x][1][index] 
                if sentenceAnnotDict[k][x][1][index] == 1:
                    count = count + 1
                percentValue[index] = float(count/24.0)
                print type(percentValue[index])
            count = 0
            index = index + 1
        print percentValue
        percentValueDict[k]= percentValue
        writer.writerow([k, percentValue])
        #print percentValueDict[k]

    for k in sorted(sentenceAnnotDict.iterkeys()):
        for index in xrange(24):
            for x in xrange(12):
                if sentenceAnnotDict[k][x][1][index] > sentenceAnnotDict[k][x][1][index] + 1:
                    max = sentenceAnnotDict[k][x][1][index]
        print max


    """
    writer = csv.writer(open('percent.csv',wb)
    for key, value in sorted(percentValueDict.items()):
        writer.writerow([key, value])
    """
except mdb.Error, e:
    print "Error %d: %s" % (e.args0],e.args[1])
    sys.exit(1)
    
finally:    
    if con:    
        con.close()