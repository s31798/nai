import heapq
import sys
import matplotlib.pyplot as plt

class Model:
    def __init__(self):
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        self.vec_length = None
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
        try:
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
        except FileNotFoundError:
            raise Exception(f'file {file_name} not found')

    def open_training_data(self, file_name):
        self.x_train,self.y_train = Model.load_data_from_file(file_name)
        self.vec_length = len(self.x_train[0])

    def open_test_data(self, file_name):
        self.x_test, self.y_test = Model.load_data_from_file(file_name)
    def predict_vec(self, vect, k):
        distances = Model.calculate_distances(self.x_train, vect)
        #indeces of k smallest values in O(nlogk)
        index_neighbor_pairs = heapq.nsmallest(k, enumerate(distances), key=lambda x: x[1])
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
    def predict_all(self,k):
        result = []
        for i in range(len(self.x_test)):
            result.append(self.predict_vec(m.x_test[i],k))
        return result

    def get_accuracy(self,k):
        predictions = self.predict_all(k)
        correct = 0
        for i in range(len(self.y_test)):
            if self.y_test[i] == predictions[i]:
                correct += 1
        accuracy = correct / len(self.y_test)
        return accuracy



args = sys.argv
if len(args) != 4:
    raise Exception("Wrong number of arguments")
train = args[2]
test = args[3]
m = Model()
m.open_training_data(train)
m.open_test_data(test)
if args[1] == "graph":
    k_values = [3,4,5,10,15,20]
    accuracies = []
    for i in k_values:
       accuracies.append(m.get_accuracy(i))
    plt.scatter(k_values, accuracies, color='red', marker='o')
    plt.xlabel("K")
    plt.ylabel("Accuracy")
    plt.title("Accuracy against K values")
    plt.show()
else:
    k = int(args[1])
    print("accuracy: ", m.get_accuracy(k))
    n_dims = m.vec_length
    while(True):
        vec = input(f'enter a {n_dims}-dimensional vector to label, in the format 1,3,3,...: ').strip().split(',')

        if len(vec) != n_dims:
            print("wrong vector length")
            break
        try:
            vec = list(map(float, vec))
            print(m.predict_vec(vec,k))
        except Exception:
            print("please enter a valid vector")


