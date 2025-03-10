line1 = [5.1,3.5,1.4,0.2,"Iris-setosa"]
line2 = [4.9,3.0,1.4,0.2,"Iris-setosa"]
line3 = [4.7,3.2,1.3,0.2,"Iris-setosa"]
line4 = [4.6,3.1,1.5,0.2,"Iris-setosa"]
line5 = [5.0,3.6,1.4,0.2,"Iris-setosa"]
lines = [line1,line2,line3,line4,line5]
x_train = []
y_train = []
for line in lines:
    x_train.append(line[:-1])
    y_train.append(line[-1])

x_test = [5.0,3.2,1.2,0.2]



class Model:
    def __init__(self,k):
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
            print(distances[i])
        return distances

print(x_train)
print(x_test)
Model.calculate_distances(x_train, x_test)

