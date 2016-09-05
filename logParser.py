"""
Author: Ben Bornholm
Date: 94-16
Description: Take in log files and parse them into a key:value pair and then put into a list
list[(source_IP:'192.168.1.1')]
"""
import os

def logParser(uploadpath):
    entryDict = {}
    tempDict = {}

    filenameLst = []
    for filename in os.listdir(uploadpath):
        entryLst = []
        tempLst = []
        fieldsLst = []
        # Add filename to list
        filenameLst.append(filename)
        fLog = open(uploadpath+'/'+filename,'r')
        for line in fLog:

            # Grab all fields for
            if '#fields' in line:
                fieldsLst = line.split()
                fieldsLst.remove('#fields')

                # ignore comments at the top of the file
            elif "#" in line:
                continue

            # collect all entries in file
            else:
                tempLst = line.split()

                tempDict = {}
                for i in range(0,len(tempLst)):
                    tempDict[fieldsLst[i]] = tempLst[i]
                entryLst.append(tempDict)

        tempLst = [fieldsLst, tempLst]
        entryDict[filename] = tempLst
    # Return of a list of dictonaries of all entries
    return entryDict, fieldsLst
