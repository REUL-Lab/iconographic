# -*- coding: utf-8 -*-
from sklearn import externals
import pickle
import re

#This is the way we read through the user input text
class FileReader:


    @staticmethod
    def textSplit(text):


        #if we want to do things by smaller granularity

        #.*\.\n+(.*[^.]\n+).  regex to get all headers
        # print (text)

        text = re.sub(r'(\n[0-9][0-9]*[\.\)]*)\s*', '', text)

        #regex to remove headers
        text = re.sub(r'(?!.*([\.\;\,\:]))(.*[^\.])', '', text)

        #regex to remove line numbers and list
        

        

        temp = text.split(".")
        rawdata = []
        for i in range(0, len(temp), 4):
            if (i + 3 < len(temp)):
                rawdata.append(temp[i] + temp[i+1] + temp[i+2] + temp[i+3])
            elif (i + 2 < len(temp)):
                rawdata.append(temp[i] + temp[i+1] + temp[i+2])
            elif (i + 1 < len(temp)):
                rawdata.append(temp[i] + temp[i+1])
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

        return dict(zip(rawdata, labels))

    @staticmethod
    def fileSplit(fle):
        temp = fle.split(".")
        rawdata = []
        for i in range(0, len(temp), 4):
            if (i + 3 < len(temp)):
                rawdata.append(temp[i] + temp[i+1] + temp[i+2] + temp[i+3])
            elif (i + 2 < len(temp)):
                rawdata.append(temp[i] + temp[i+1] + temp[i+2])
            elif (i + 1 < len(temp)):
                rawdata.append(temp[i] + temp[i+1])
            else:
                rawdata.append(temp[i])

        classifier = externals.joblib.load("EULA_Classifier.pkl")
        vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
        data = vectorizer.transform(rawdata)
        labels = classifier.predict(data)

        return dict(zip(rawdata, labels))

    @staticmethod
    def modifyText(data=[],labels=[]):
        modFile = open("LabeledData.txt","w")
        for i in xrange(0,len(data)):
            if labels[i] != "None":
                modFile.write("-----------------" + labels[i] + "--------------------\n")
                modFile.write(data[i])

        modFile.close()
        return modFile
