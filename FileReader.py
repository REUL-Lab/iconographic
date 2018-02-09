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
