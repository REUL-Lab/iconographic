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

        all_labels = []
        for clf in classifier:
            labels = clf.predict(data)
            all_labels.append(labels)

        print (len(all_labels))

        final_labels = []
        for i in range(len(rawdata)):

            curr_labels = {}
            for j in all_labels:
                if j[i] in curr_labels:
                    curr_labels[j[i]] += 1
                else:
                    curr_labels[j[i]] = 1

            if (len(curr_labels) == len(all_labels)):
                final_labels.append(0)
            else:
                final_labels.append(max(curr_labels, key=curr_labels.get))
        
        #labelvals = [FileReader.labelnames[num] for num in labels]
        
        return dict(zip(rawdata, final_labels))

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
