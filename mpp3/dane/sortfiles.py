import os
import pandas as pd
from tqdm import tqdm


INPUT_CSV = "Language Detection.csv"
OUTPUT_DIR = "language_texts_grouped"
TEXTS_PER_FILE = 5


df = pd.read_csv(INPUT_CSV)


for language in tqdm(df['Language'].unique(), desc="Przetwarzanie języków"):

    lang_texts = df[df['Language'] == language]['Text'].tolist()


    lang_dir = os.path.join(OUTPUT_DIR, language.replace(" ", "_"))
    os.makedirs(lang_dir, exist_ok=True)


    for i in range(0, len(lang_texts), TEXTS_PER_FILE):
        group = lang_texts[i:i + TEXTS_PER_FILE]
        file_number = i // TEXTS_PER_FILE + 1


        file_name = f"{language}_{file_number:03d}.txt"
        file_path = os.path.join(lang_dir, file_name)


        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("\n\n".join(group))  # 2 nowe linie jako separator

print(f"Zakończono! Pliki zapisano w: {OUTPUT_DIR}")