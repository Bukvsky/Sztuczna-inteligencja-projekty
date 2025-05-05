import random
import math


def load_data(filename):
    features = []
    labels = []
    classes = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
    class_names = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().replace(',', '.')
            if not line:
                continue
            parts = line.split()
            if len(parts) == 5:
                features.append([float(x) for x in parts[:4]])
                labels.append(classes[parts[4]])

    return features, labels, class_names


def euclidean_distance(point1, point2):
    suma = 0
    n = min(len(point1), len(point2))
    for i in range(n):
        suma += (point1[i] - point2[i]) ** 2

    return math.sqrt(suma)


def generate_centroids(data, k):
    indices = random.sample(range(len(data)), k)
    centroids = []
    for idx in indices:
        centroids.append(data[idx][:])
    return centroids


def assign_clusters(data, centroids):
    clusters = [[] for i in range(len(centroids))]
    cluster_indices = []
    for i, point in enumerate(data):
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        closest_centroid = distances.index(min(distances))
        clusters[closest_centroid].append(point[:])
        cluster_indices.append(closest_centroid)
    return clusters, cluster_indices


def update_centroids(clusters):
    new_centroids = []
    for cluster in clusters:
        if cluster:
            num_features = len(cluster[0])
            centroid = [0] * num_features
            for point in cluster:
                for i in range(num_features):
                    centroid[i] += point[i]

            for i in range(num_features):
                centroid[i] /= len(cluster)
            new_centroids.append(centroid)
        else:
            new_centroids.append([random.random() for l in range(4)])
    return new_centroids


# Poprawiona funkcja - używa cluster_indices zamiast clusters
def calculate_sum_of_squares(data, centroids, cluster_indices):
    sse = 0
    for i, point in enumerate(data):
        centroid = centroids[cluster_indices[i]]
        sse += euclidean_distance(point, centroid) ** 2

    return sse


def calculate_entropy(cluster_labels):
    total = len(cluster_labels)
    if total == 0:
        return 0

    # Liczenie częstości wystąpień każdej klasy
    counts = {}
    for label in cluster_labels:
        if label not in counts:
            counts[label] = 0
        counts[label] += 1

    # Obliczanie entropii
    entropy = 0
    for count in counts.values():
        probability = count / total
        if probability > 0:  # log(0) jest niezdefiniowany
            entropy -= probability * math.log2(probability)

    return entropy


def get_tuple(centroids):
    t = []
    for i in centroids:
        t.append(tuple(i[1]))

    return t


# Poprawiona funkcja k_means
def k_means(data, k, labels, max_iterations=100):
    centroids = generate_centroids(data, k)
    prev_sse = float('inf')
    iteration = 0

    while iteration < max_iterations:
        # Przypisanie punktów do klastrów
        clusters, cluster_indices = assign_clusters(data, centroids)

        # Obliczanie SSE - poprawione wywołanie funkcji
        sse = calculate_sum_of_squares(data, centroids, cluster_indices)
        print(f"Iteracja {iteration + 1}: SSE = {sse:.4f}")

        if abs(prev_sse - sse) < 0.001:
            break

        prev_sse = sse
        centroids = update_centroids(clusters)
        iteration += 1

    # Analiza wyników
    clusters, cluster_indices = assign_clusters(data, centroids)
    print("\nWyniki klastrowania:")

    for i in range(k):
        cluster_label_indices = [j for j, cluster_idx in enumerate(cluster_indices) if cluster_idx == i]
        cluster_labels = [labels[j] for j in cluster_label_indices]  # Pobieramy etykiety dla punktów w klastrze

        class_counts = {}
        for label in cluster_labels:
            if label not in class_counts:
                class_counts[label] = 0
            class_counts[label] += 1

        print(f"\nKlaster {i + 1}:")
        print(f"Liczba punktów: {len(cluster_labels)}")
        print("Skład klastra według gatunków:")
        for label, count in sorted(class_counts.items()):
            percentage = (count / len(cluster_labels)) * 100 if len(cluster_labels) > 0 else 0
            print(f"  - Gatunek {label}: {count} punktów ({percentage:.2f}%)")

        # Obliczanie i wyświetlanie entropii
        entropy = calculate_entropy(cluster_labels)
        print(f"Entropia klastra: {entropy:.4f}")

    return centroids, cluster_indices


def calculate_entropy_from_frequencies(frequencies):
    """Oblicza entropię na podstawie listy częstości"""
    total = sum(frequencies)
    entropy = 0

    for freq in frequencies:
        if freq > 0:  # Pomijamy zerowe częstości
            probability = freq / total
            entropy -= probability * math.log2(probability)

    return entropy


def main():
    print("Program do klastrowania irysów metodą k-means")

    # Próba wczytania danych z pliku
    try:
        features, labels, class_names = load_data('iris_test.txt')
        print(f"Wczytano {len(features)} irysów, z {len(class_names)} gatunkami.")
    except FileNotFoundError:
        print("Plik iris_test.txt nie został znaleziony. Upewnij się, że plik istnieje w tym samym katalogu.")
        return

    while True:
        try:
            k = int(input("\nPodaj liczbę klastrów (k): "))
            if k > 0:
                break
            else:
                print("Liczba klastrów musi być dodatnia.")
        except ValueError:
            print("Proszę podać poprawną liczbę całkowitą.")

    # Uruchomienie algorytmu k-means
    print("\nRozpoczynanie algorytmu k-means...")
    centroids, cluster_indices = k_means(features, k, labels)

    # Zadanie dodatkowe - obliczanie entropii z częstości
    print("\n--- Zadanie dodatkowe ---")
    print("Wczytaj częstości wystąpienia wariantów rozkładu, oddzielonych spacjami:")

    try:
        frequencies = list(map(float, input().split()))
        entropy = calculate_entropy_from_frequencies(frequencies)
        print(f"Entropia podanego rozkładu: {entropy:.4f}")
    except ValueError:
        print("Podano niepoprawne częstości. Proszę wprowadzić liczby oddzielone spacjami.")


if __name__ == "__main__":
    main()