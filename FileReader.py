from sklearn import externals

class FileReader:

    def getDataFromText(text=""):



    def getDataFromFile(input=None):


class Classify:

    def predictLabels(data, classifier):


    def modifyText(data):


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

    (output, labels) = rslt.predictLabels(data,classifier)






if __name__ == "__main__":
    main()
