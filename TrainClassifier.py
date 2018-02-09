from sklearn import neural_network, externals
import csv

class TrainClassifier:

    def train(data=[],labels=[]):
        model = neural_network.MLPClassifier()
        model.fit(data,labels)
        return model

    def test(data=[]):




def main():
    cls = TrainClassifier()

    traindata = []
    trainlabels = []
    with open('traindata.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            text = row[0]
            label = row[1]
            traindata.append(text)
            trainlabels.append(label)

    classifier = cls.train(traindata,trainlabels)
    externals.joblib.dump(classifier, "EULA_Classifier.pkl")






if __name__ == "__main__":
    main()