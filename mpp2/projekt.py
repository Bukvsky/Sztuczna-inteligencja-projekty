from Perceptron import Perceptron

def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.replace(',', '.').split()
            numeric = [float(x) for x in parts[:-1]]
            attribute = 1 if parts[-1] == 'Iris-setosa' else 0
            data.append((attribute, numeric))
    return data


def train_perceptron(p, training_data):
    steps = 0
    total_samples = len(training_data)
    while True:
        steps += 1
        correct = 0

        for target, input in training_data:

            prediction = p.compute(input)
            if prediction == target:
                correct += 1



            p.learn(input, target)

        #print(f"Kroki {steps}: {correct}/{total_samples} poprawnych ({correct / total_samples:.1%})")

        if correct == total_samples:
            return steps

def test_perceptron(p,test_data):
    corectPerceptron = 0
    for target,input in test_data:
        prediction = p.compute(input)
        #print(prediction,input,p.weights)
        print(f"""{'✅ Prawidłowy ' if prediction==target else '❌ Nieprawidłowy, '}   oczekiwano:{'Iris-setosa, ' if target == 1 else "Inna klasa (versicolor/virginica), "} otrzymano: {'Iris-setosa, ' if prediction == 1 else "Inna klasa (versicolor/virginica), "}""")

        if prediction == target:
            corectPerceptron+=1


    return corectPerceptron


def askUser():
    print(f'''\n{'=' * 59}MENU{'=' * 59}''')
    print(f'''Wprowadź numer odpowiedniego polecenia:''')
    print(f'''1.Wyświetl wynik klasyfikacji algorytmu delta dla perceptronu dla wartości bazowych''')
    print(f'''2.Wyświetl wynik klasyfikacji algorytmu delta dla perceptronu używając własnych wag oraz własnego progu i stopnia uczenia''')
    print(f'''3.Podaj swoje wlasne atrybuty do zaklasyfikowania''')
    print(f'''4.Exit''')
    print(f'''{'=' *122}''')
    return int(input(f'''Twój wybór: '''))


def main():

    training_data = load_data('iris_training.txt')
    test_data = load_data('iris_test.txt')
    #print(training_data)

    l = len(training_data[0][1])
    perceptron = Perceptron(l,[1,2,3,4],1,None)

    choice = askUser()
    while choice > 3 or choice < 1:
        choice = int(input(f'''Podałeś zły numer, wprowadz go jeszcze raz'''))


    while True:
        if(choice == 1):
            train_perceptron(perceptron, training_data)
            result = test_perceptron(perceptron,test_data)
            accuracy = (result/len(test_data))*100
            print(f'''\n{'=' * 20}Wynik{'=' * 20}''')
            print(f"Poprawnie zaklasyfikowane: {result}/{len(test_data)}")
            print(f"Dokładność: {accuracy:.2f}%")

        elif choice == 2:

            try:
                user_weights = input(f"Podaj wektor atrybutów (oddzielonych przecinkami, np. '2')")
                inputs = list(map(float, user_weights.split(',')))
                user_threshold = float(input(f"Podaj próg: "))
                user_learning_rate = float(input(f"Podaj współczynnik uczenia: "))
                if len(inputs) != l:
                    print(f"Błąd: oczekiwano {l} atrybutów")
                    continue
                user_perceptron = Perceptron(l, inputs, user_threshold, user_learning_rate)
                train_perceptron(user_perceptron, training_data)
                result = test_perceptron(user_perceptron, test_data)
                accuracy = (result / len(test_data)) * 100
                print(f'''\n{'=' * 20}Wynik{'=' * 20}''')
                print(f"Poprawnie zaklasyfikowane: {result}/{len(test_data)}")
                print(f"Dokładność: {accuracy:.2f}%")
            except ValueError:
                print(f"Błąd: nieprawidłowy format danych")




        elif choice == 3:
            train_perceptron(perceptron, training_data)
            try:
                user_input = input(f"Podaj wektor atrybutów (oddzielonych przecinkami, np. '5.1,3.5,1.4,0.2')")
                inputs = list(map(float, user_input.split(',')))
                if len(inputs) != l:
                    print(f"Błąd: oczekiwano {l} atrybutów")
                    continue
                prediction = perceptron.compute(inputs)
                print(f"Klasa: Iris-setosa" if prediction == 1 else "Inna klasa (versicolor/virginica)")
            except ValueError:
                print(f"Błąd: nieprawidłowy format danych")

        else:
            break

        choice = askUser()


if __name__ == "__main__":
    main()