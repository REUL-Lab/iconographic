from sklearn import neural_network, externals, model_selection, metrics, feature_extraction
import csv
import numpy as np
import math
import pickle

class TrainClassifier:

    def __init__(self):
        self.classifier = None

    def train(self,data,labels):
        model = neural_network.MLPClassifier(max_iter=1000)
        model.fit(data,labels)
        return model

    def test(self,data, clf):
        return clf.predict(data)




def main():
    cls = TrainClassifier()

    rawdata = []
    labels = []
    i = 0
    with open('traindata.csv', encoding="utf8") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            text = str(row[0])
            print(text)
            text = text.replace(u'\xa0',u' ')
            label = int(row[1])
            
            rawdata.append(text)
            labels.append(label)
    
    rawdata = np.array(rawdata)
    labels = np.array(labels)
    vectorizer = feature_extraction.text.TfidfVectorizer()
    vect = vectorizer.fit(rawdata)

    with open ("vectorizer.pkl", "wb") as v:
            pickle.dump(vect, v)
    
    data = vectorizer.transform(rawdata)

    
    classifier = cls.train(data,labels)
    # kf = model_selection.KFold(n_splits = 4)
    # classifiers = []
    # for trainI, testI in kf.split(data, labels):
        
    #     dataTrain, dataTest = data[trainI], data[testI]
    #     labelTrain, labelTest = labels[trainI], labels[testI]
    #     print (labelTrain)
    #     clf = cls.train(dataTrain, labelTrain)
    #     predictLabels = cls.test(dataTest, clf)
    #     # print("Confusion Matrix:\n",metrics.confusion_matrix(labelTest, predictLabels))
    #     # print("Accuracy: ", metrics.accuracy_score(labelTest, predictLabels))
    #     # print("F1 score: ", metrics.f1_score(labelTest, predictLabels, average='micro'))

    predictLabels = cls.test(data,classifier)
    print("Confusion Matrix:\n",metrics.confusion_matrix(labels, predictLabels))
    print("Accuracy: ", metrics.accuracy_score(labels, predictLabels))
    print("F1 score: ", metrics.f1_score(labels, predictLabels, average='micro'))
    externals.joblib.dump(classifier, "EULA_Classifier.pkl")



if __name__ == "__main__":
    main()