import os

def create_txt_files(directory, file_count=10):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(1, file_count + 1):
        file_name = f"file{i}.txt"
        file_path = os.path.join(directory, file_name)

        with open(file_path, 'w') as file:
            file.write('')

        print(f"Utworzono plik: {file_path}")


# Przykład użycia:
sciezka_katalogu = "D:\\PJATK\\2rok\\2425_Letni\\NAI\\Cwiczenia\\NAI\\mpp3\\dane\\czeski"
create_txt_files(sciezka_katalogu)
sciezka_katalogu = "D:\\PJATK\\2rok\\2425_Letni\\NAI\\Cwiczenia\\NAI\\mpp3\\dane\\słowacki"
create_txt_files(sciezka_katalogu)
sciezka_katalogu = "D:\\PJATK\\2rok\\2425_Letni\\NAI\\Cwiczenia\\NAI\\mpp3\\dane\\niemiecki"
create_txt_files(sciezka_katalogu)
sciezka_katalogu = "D:\\PJATK\\2rok\\2425_Letni\\NAI\\Cwiczenia\\NAI\\mpp3\\dane\\polski"
create_txt_files(sciezka_katalogu)