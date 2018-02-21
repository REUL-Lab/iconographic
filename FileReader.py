# -*- coding: utf-8 -*-
from sklearn import externals
import pickle

#This is the way we read through the user input text
class FileReader:


    labelnames = [
        "None", 
        "Selling data",
        "Gag wrap",
        "Data Retention after termination",
        "Data Retention after logout",
        "Data tracking after deletion",
        "Data tracking after logout",
        "Data tracking after closing",
        "Location tracking",
        "Location tracking retention",
        "Third Party Data Share (eg: sharing data w/ police)",
        "Sell UGC",
        "Own UGC",
        "Repurpose UGC",
        "Use of UGC after termination",
        "Recurring charges",
        "Termination conditions",
        "Arbitration Clause",
        "Forced Termination (Code of Conduct)",
        "Removal of UGC",
        "Notice of EULA changes",
        "Under 18 liability",
        "Lacks 13+ clause for use",
        "Expiration Conditions",
        "User’s Ability to Transfer Product",
        "Indemnity Clause",
        "Embedded Policies (when you have to click out to something else to read, but agree to in EULA)",
        "Wild Card",
        "Email subscriptions (spam etc.)",
        "EULA Version date",
        "Maintenance (eg: software updates, etc.)"
    ]


    @staticmethod
    def textSplit(text):


        #if we want to do things by smaller granularity
        temp = text.split(".")
        rawdata = []
        for i in range(0, len(temp), 4):
            if (i + 3 < len(temp)):
                rawdata.append(temp[i] + temp[i+1] + temp[i+2] + temp[i+3])
            else:
                rawdata.append(temp[i])


        #Import the classifier from the pickle file
        
        #classifier = externals.joblib.load("EULA_Classifier.pkl")

        #Uncomment when classifier works
        #labels = rslt.predictLabels(data,classifier)
        classifier = externals.joblib.load("EULA_Classifier.pkl")
        vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
        data = vectorizer.transform(rawdata)
        labels = classifier.predict(data)

        
        labelvals = [FileReader.labelnames[num] for num in labels]
        
        return dict(zip(rawdata, labelvals))

    @staticmethod
    def fileSplit(fle):
        temp = fle.split(".")
        rawdata = []
        for i in range(0, len(temp), 4):
            if (i + 3 < len(temp)):
                rawdata.append(temp[i] + temp[i+1] + temp[i+2] + temp[i+3])
            else:
                rawdata.append(temp[i])

        classifier = externals.joblib.load("EULA_Classifier.pkl")
        vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
        data = vectorizer.transform(rawdata)
        labels = classifier.predict(data)
        labelvals = [FileReader.labelnames[num] for num in labels]
        
        return dict(zip(rawdata, labelvals))

    @staticmethod
    def modifyText(data=[],labels=[]):
        modFile = open("LabeledData.txt","w")
        for i in xrange(0,len(data)):
            if labels[i] != "None":
                modFile.write("-----------------" + labels[i] + "--------------------\n")
                modFile.write(data[i])

        modFile.close()
        return modFile
