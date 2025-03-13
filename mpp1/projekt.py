import math


def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            t = line.strip().split()
            numeric = [float(t[i].replace(',', '.')) for i in range(len(t) - 1)]
            attribute = t[-1]
            data.append((attribute, numeric))
    return data


def euclidean_distance(point1, point2):
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))


def knn_classify(train_data, test_point, k):
    distances = [(euclidean_distance(train[1], test_point), train[0]) for train in train_data]
    distances.sort()
    nearest_neighbors = distances[:k]

    label_count = {}
    for _, label in nearest_neighbors:
        label_count[label] = label_count.get(label, 0) + 1

    return max(label_count, key=label_count.get)


def evaluate_knn(train_data, test_data, k):
    correct = 0
    for test in test_data:
        predicted = knn_classify(train_data, test[1], k)
        if predicted == test[0]:
            correct += 1
    accuracy = (correct / len(test_data)) * 100
    return correct, accuracy


def main():
    train_data = load_data('iris_training.txt')
    test_data = load_data('iris_test.txt')

    k = int(input("Podaj wartość k: "))
    correct, accuracy = evaluate_knn(train_data, test_data, k)
    print(f'Poprawnie sklasyfikowane: {correct}/{len(test_data)}')
    print(f'Dokładność: {accuracy:.2f}%')

    while True:
        user_input = input("Podaj wektor atrybutów oddzielony spacją (lub 'exit' aby zakończyć): ")
        if user_input.lower() == 'exit':
            break
        user_vector = [float(x.replace(',', '.')) for x in user_input.split()]
        predicted_label = knn_classify(train_data, user_vector, k)
        print(f'Przewidywana etykieta: {predicted_label}')


if __name__ == "__main__":
    main()