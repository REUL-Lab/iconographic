from sklearn import externals


#This is the way we read through the user input text
class FileReader:

    #Method to take the textbox input and convert it into data
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

    #Reading through a file input and creating data
    def getDataFromFile(inpt=None):


#Class that will classify the user input
class Classify:

    #Predicts the labels for the user input
    def predictLabels(data, classifier):
        return classifer.predict(data)

    #Creates a txt file for download if the user wants
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
    data = []
    if (1==1):
        #If radio button of text box checked
        data = flr.getDataFromText()
    else:
        #If radio button of file is checked
        data = flr.getDataFromFile()


    #Import the classifier from the pickle file
    classifier = externals.joblib.load("EULA_Classifier.pkl")
    rslt = Classify()

    labels = rslt.predictLabels(data,classifier)
    #if they call download a summary
    #output = rslt.modifyText(data, labels)
    #urllib should allow for downloading this file on the users machine






if __name__ == "__main__":
    main()
