def load_file(filepath):
    data = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split()
            features = [f"{float(x.replace(',', '.')):.2f}" for x in parts[:-1]]
            label = parts[-1]
            data.append((features, label))
    return data

def count_frequencies(data):
    class_counts = {}
    feature_counts = {}

    for features, label in data:
        if label not in class_counts:
            class_counts[label] = 0
            feature_counts[label] = [{} for _ in range(len(features))]

        class_counts[label] += 1
        for i, val in enumerate(features):
            feature_counts[label][i][val] = feature_counts[label][i].get(val, 0) + 1

    return class_counts, feature_counts

def classify(features, class_counts, feature_counts):
    best_class = None
    best_prob = -1
    total_samples = sum(class_counts.values())

    for label in class_counts:
        # prior
        prob = class_counts[label] / total_samples

        for i, val in enumerate(features):
            feature_freq = feature_counts[label][i]
            count = feature_freq.get(val, 0) + 1  # Laplace smoothing
            denom = class_counts[label] + len(feature_freq)
            prob *= count / denom

        if prob > best_prob:
            best_prob = prob
            best_class = label

    return best_class

def print_confusion_matrix(matrix, labels):
    print("\nMacierz omyłek:")
    print("\t" + "\t".join(labels))
    for true_label in labels:
        row = [str(matrix[true_label].get(pred, 0)) for pred in labels]
        print(true_label + "\t" + "\t".join(row))

def evaluate(test_data, class_counts, feature_counts, labels=None):
    correct = 0
    total = len(test_data)

    # Inicjalizujemy macierz omyłek
    confusion_matrix = {label: {pred: 0 for pred in labels} for label in labels}

    for features, true_label in test_data:
        predicted = classify(features, class_counts, feature_counts)
        if predicted == true_label:
            correct += 1
        # Zliczamy błędne klasyfikacje
        confusion_matrix[true_label][predicted] += 1

    accuracy = 100 * correct / total
    return accuracy, confusion_matrix

def main():
    train = load_file("iris_training.txt")
    test = load_file("iris_test.txt")

    class_counts, feature_counts = count_frequencies(train)

    labels = sorted(class_counts.keys())  # Zakładamy, że klasy są uporządkowane
    acc, confusion_matrix = evaluate(test, class_counts, feature_counts, labels)

    print(f"\n🎯 Dokładność: {acc:.2f}%")
    print_confusion_matrix(confusion_matrix, labels)

    while True:
        user_input = input("\nWpisz 4 cechy (oddzielone przecinkami) lub 'exit': ")
        if user_input.lower() == 'exit':
            break
        try:
            features = [f"{float(x):.2f}" for x in user_input.strip().split(',')]
            if len(features) != 4:
                print("❗ Podaj dokładnie 4 cechy.")
                continue
            predicted = classify(features, class_counts, feature_counts)
            print(f"➡️ Przewidziana klasa: {predicted}")
        except Exception as e:
            print("Błąd:", e)

if __name__ == "__main__":
    main()
