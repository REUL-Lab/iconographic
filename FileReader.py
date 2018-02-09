from sklearn import externals

class FileReader:

    def getDataFromText(text=""):
        data = text.split("\n")

        # #if we want to do things by smaller granularity
        # temp = text.split(".")
        # dataIndex = 0
        # data = []
        # for i in xrange(0, len(temp)):
        #     if (i + 1 < len(temp)):
        #         data[dataIndex++] = temp[i] + temp[i+1]
        #     else:
        #         data[dataIndex++] = temp[i]

        return data


    def getDataFromFile(input=None):


class Classify:

    def predictLabels(data, classifier):
        return classifer.predict(data)

    def modifyText(data=[],labels=[]):
        modFile = open("LabeledData.txt","w")
        for i in xrange(0,len(data)):
            if labels[i] not "None":
                modFile.write("-----------------" + labels[i] + "--------------------\n")
                modFile.write(data[i])

        modFile.close()
        return modFile


class Converter:


    def doc2txt:


    def pdf2txt:



def main:
    flr = FileReader()
    #If radio button of text box checked
    data = []
    if (1==1):
        data = flr.getDataFromText()
    else:
        data = flr.getDataFromFile()


    classifier = externals.joblib.load("EULA_Classifier.pkl")
    rslt = Classify()

    labels = rslt.predictLabels(data,classifier)
    #if they call download a summary
    #output = rslt.modifyText(data, labels)
    #urllib should allow for downloading this file on the users machine






if __name__ == "__main__":
    main()
