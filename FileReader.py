from sklearn import externals


#This is the way we read through the user input text
class FileReader:
    

    @staticmethod
    def textSplit(text):

        data = text.splitlines()

        # #if we want to do things by smaller granularity
        # temp = text.split(".")
        # dataIndex = 0
        # data = []
        # for i in xrange(0, len(temp)):
        #     if (i + 1 < len(temp)):
        #         data[dataIndex++] = temp[i] + temp[i+1]
        #     else:
        #         data[dataIndex++] = temp[i]

        #Import the classifier from the pickle file
        
        #classifier = externals.joblib.load("EULA_Classifier.pkl")

        #Uncomment when classifier works
        #labels = rslt.predictLabels(data,classifier)

        
        #labels = set(labels)
        # labels = ["permissions"]
        return data
        # return labels

    @staticmethod
    def fileSplit(fle):
        data = fle.splitlines()

        #classifier = externals.joblib.load("EULA_Classifier.pkl")

        #Import the classifier from the pickle file

        #uncomment when classifier works
        #labels = rslt.predictLabels(data,classifier)

        return data
        #labels = set(labels)
        # labels = ["permissions"]

        # return labels

    @staticmethod
    def modifyText(data=[],labels=[]):
        modFile = open("LabeledData.txt","w")
        for i in xrange(0,len(data)):
            if labels[i] != "None":
                modFile.write("-----------------" + labels[i] + "--------------------\n")
                modFile.write(data[i])

        modFile.close()
        return modFile
