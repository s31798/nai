import heapq

from unicodedata import numeric


class Model:
    def __init__(self,k):
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        self.k = k
    @staticmethod
    def calculate_distance(vector1, vector2):
        sum = 0.0
        for i in range(len(vector1)):
            sum += (vector1[i] - vector2[i])**2
        return sum**0.5
    @staticmethod
    def calculate_distances(training_vectors, test_vector):
        distances = []
        for i in range(len(training_vectors)):
            distances.append(Model.calculate_distance(training_vectors[i], test_vector))
        return distances
    @staticmethod
    def load_data_from_file(file_name):
        x = []
        y  = []
        file = open("data/" + file_name)
        line = file.readline()
        while line:
            vec = []
            line = line.strip().split(",")
            for i in range(len(line) - 1):
                vec.append(float(line[i]))
            x.append(vec)
            y.append(line[-1])
            line = file.readline()
        return x, y

    def open_training_data(self, file_name):
        self.x_train,self.y_train = Model.load_data_from_file(file_name)

    def open_test_data(self, file_name):
        self.x_test, self.y_test = Model.load_data_from_file(file_name)
    def predict_at(self, index):
        distances = Model.calculate_distances(m.x_train, m.x_test[index])
        #indeces of k smallest values in O(nlogk)
        index_neighbor_pairs = heapq.nsmallest(self.k, enumerate(distances), key=lambda x: x[1])
        neighbors_index = [index for index, value in index_neighbor_pairs]
        labels = {}
        for neighbor in neighbors_index:
            label = m.y_train[neighbor]
            labels[label] = labels.get(label,0) + 1
        count = 0
        max_label = ""
        for entry in labels.items():
            if entry[1] > count:
                count = entry[1]
                max_label = entry[0]
        return max_label
    def predict_all(self):
        result = []
        for i in range(len(self.x_test)):
            result.append(self.predict_at(i))
        return result

    def get_accuracy(self):
        predictions = self.predict_all()
        correct = 0
        for i in range(len(self.y_test)):
            if self.y_test[i] == predictions[i]:
                correct += 1
        accuracy = correct / len(self.y_test)
        return accuracy







m = Model(4)
m.open_training_data("iris.data")
m.open_test_data("iris.test.data")
print(m.get_accuracy())

