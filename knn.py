

x_test = [5.0,3.2,1.2,0.2]



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


m = Model(5)
m.open_training_data("iris.data")
m.open_test_data("iris.test.data")
print(Model.calculate_distances(m.x_train, x_test))

