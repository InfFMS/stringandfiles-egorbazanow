# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
import re
from collections import Counter
input_file = "task3.txt"
output_file = "task3_results.txt"
try:
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for word, count in sorted(word_counts.items()):
            outfile.write(f"{word}: {count}\n")
    print(f"Результаты записаны в файл: {output_file}")
except FileNotFoundError:
    print(f"Ошибка: файл '{input_file}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

