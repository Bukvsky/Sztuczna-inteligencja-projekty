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

"""def load_data2(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            t = line.strip().split(',')
            numeric = [float(t[i]) for i in range(len(t) - 1)]
            attribute = t[-1]
            data.append((attribute, numeric))
    return data"""
def euclidean_distance(point1, point2):
    suma = 0
    n = min(len(point1),len(point2))
    for i in  range(n):
        suma+=(point1[i]-point2[i])**2

    return math.sqrt(suma)





def knn_algorithm(training_data, test_point, k):
    distances = [(euclidean_distance(train[1], test_point[1]), train[0]) for train in training_data]

    neighborhood = sorted(distances)[:k]
    labels = {}
    for line in neighborhood:
        if line[1] not in labels:
            labels[line[1]] = 0
        labels[line[1]] += 1


    print(labels)
    return max(labels, key=labels.get)


def askUser():
    print(f'''\n{'=' * 38}MENU{'=' * 38}''')
    print(f'''Wprowadź numer odpowiedniego polecenia:''')
    print(f'''1.Podaj parametr k dla którego zakalsyfikujemy zbiór testowy''')
    print(f'''2.Podaj swoje wlasne atrybuty do zaklasyfikowania''')
    print(f'''3.Exit''')
    print(f'''{'=' * 80}''')
    return int(input(f'''Twój wybór: '''))


def validateCorrect(training_data,test_data,k):
    correct = 0
    for line in test_data:
        winner = knn_algorithm(training_data,line,k)
        if winner==line[0]:
            correct+=1


    return correct
def main():
    training_data = load_data('../../mpp1/iris_training.txt')
    test_data = load_data('../../mpp1/iris_test.txt')
    #singleTest = load_data('valdiate.txt')
    choice = askUser()
    while choice> 3 or choice<1:
        choice = int(input(f'''Podałeś zły numer, wprowadz go jeszcze raz'''))
    k = 0
    while True:
        if choice == 1:
            k = int(input(f'''Podaj paramter k: '''))
            while(k> len(training_data) or k<1):
                k = int(input(f'''Podaj poprawnie parametr k: '''))
            result = validateCorrect(training_data,test_data,k)
            accuracy = (result/len(test_data))*100
            print(f'======WYNIK======')
            print(f'Poprawnie sklasyfikowane: {result}/{len(test_data)}')
            print(f'Dokładność: {accuracy:.2f}%')
        elif choice == 2:
            tab = ['']
            t = []
            for i in range(len(training_data[0][1])):
                tmp = float(input(f'''Podaj parametr numer {i+1}: '''))
                t.append(tmp)
            tab.append(t)
            k = int(len(training_data)*(0.1))
            winner = knn_algorithm(training_data,tab,k)
            print(winner)
        elif choice ==3:
            break

        choice=askUser()


if __name__ == "__main__":
    main()