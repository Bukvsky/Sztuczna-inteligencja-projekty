import math

def load_file_continuous(filepath):
    tab = []
    with open(filepath, 'r') as file:
        t = [line.strip().split() for line in file]

    for line in t:
        tmp = [float(line[i].replace(',', '.')) for i in range(len(line)-1)]
        tab.append((tmp, line[-1]))
    return tab

def load_file_discrete(filepath):
    tab = []
    with open(filepath, 'r') as file:
        t = [line.strip().split() for line in file]

    for line in t:
        tmp = [(line[i].replace(',', '.')) for i in range(len(line)-1)]
        tab.append((tmp, line[-1]))
    return tab

def separate_classes(tab):
    dictionary = {}
    for features, label in tab:
        if label not in dictionary:
            dictionary[label] = []
        dictionary[label].append(features)
    return dictionary

def calculate_avg(tab):
    dict_of_avg = {}
    for key in tab:
        dict_of_avg[key] = [0.0] * 4
        for val_tab in tab[key]:
            for j in range(4):
                dict_of_avg[key][j] += val_tab[j]
        count = len(tab[key])
        for j in range(4):
            dict_of_avg[key][j] = round(dict_of_avg[key][j] / count, 4)
    return dict_of_avg

def calculate_stdev(tab, dict_of_avg):
    dict_of_std = {}
    for key in tab:
        dict_of_std[key] = [0.0] * 4
        n = len(tab[key])
        for val_tab in tab[key]:
            for j in range(4):
                diff = val_tab[j] - dict_of_avg[key][j]
                dict_of_std[key][j] += diff ** 2
        for j in range(4):
            dict_of_std[key][j] = ((dict_of_std[key][j]) / (n - 1)) ** 0.5 if n > 1 else 0.0
    return dict_of_std

def bayes_smoothing(stdevs):
    for key in stdevs:
        before = stdevs[key][0]
        print(f"[{key}] std przed wygładzaniem: {before}")
        if before == 0:
            stdevs[key][0] = 1.0
            print(f"[{key}] std po wygładzaniu: {stdevs[key][0]}")
    return stdevs

def calculate_priors(tab):
    total = sum(len(tab[key]) for key in tab)
    priors = {}
    for key in tab:
        priors[key] = len(tab[key]) / total
    return priors

def gaussian(x, mean, std):
    if std == 0:
        std = 1e-6
    exponent = math.exp(-((x - mean) ** 2) / (2 * std ** 2))
    return (1 / (math.sqrt(2 * math.pi) * std)) * exponent

def classify(vector, avg, std, priors):
    scores = {}
    for label in avg:
        log_prob = math.log(priors[label])
        for i in range(4):
            prob = gaussian(vector[i], avg[label][i], std[label][i])
            log_prob += math.log(prob)
        scores[label] = log_prob
    return max(scores, key=scores.get)

def evaluate(test_data, avg, std, priors, labels):
    correct = 0
    confusion = {true: {pred: 0 for pred in labels} for true in labels}

    for vector, true_label in test_data:
        predicted = classify(vector, avg, std, priors)
        if predicted == true_label:
            correct += 1
        confusion[true_label][predicted] += 1

    accuracy = 100 * correct / len(test_data)
    return accuracy, confusion

def print_confusion_matrix(matrix, labels):
    print("\nMacierz omyłek:")
    print("\t" + "\t".join(labels))
    for true_label in labels:
        row = [str(matrix[true_label][pred]) for pred in labels]
        print(true_label + "\t" + "\t".join(row))

def manual_mode(avg, std, priors):
    while True:
        user_input = input("\nWpisz 4 cechy (oddzielone przecinkami) lub 'exit': ")
        if user_input.lower() == 'exit':
            break
        try:
            values = list(map(float, user_input.strip().split(',')))
            if len(values) != 4:
                print("❗ Podaj dokładnie 4 liczby.")
                continue
            predicted = classify(values, avg, std, priors)
            print(f"➡️ Przewidziana klasa: {predicted}")
        except Exception as e:
            print("Błąd:", e)

# ======================= MAIN =======================

def main():
    training_data = load_file_continuous("iris_training.txt")
    test_data = load_file_continuous("iris_test.txt")

    train_classes = separate_classes(training_data)
    avg = calculate_avg(train_classes)
    std = bayes_smoothing(calculate_stdev(train_classes, avg))
    priors = calculate_priors(train_classes)

    labels = sorted(train_classes.keys())
    accuracy, matrix = evaluate(test_data, avg, std, priors, labels)

    print(f"\n🎯 Dokładność: {accuracy:.2f}%")
    print_confusion_matrix(matrix, labels)

    manual_mode(avg, std, priors)

if __name__ == "__main__":
    main()
