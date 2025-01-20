# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
# Выведите это слово и длину в консоль.
import re
input_file = "task5.txt"
output_file = "task5_result.txt"
try:
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read().lower()
        words = re.findall(r'\b\w+\b', text)
        if not words:
            print("Файл пуст или не содержит слов.")
        else:
            longest_word = max(words, key=len)
            longest_word_len = len(longest_word)
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write(f"Самое длинное слово: {longest_word}\n")
                outfile.write(f"Его длина: {longest_word_len}\n")
            print(f"Самое длинное слово: {longest_word}")
            print(f"Его длина: {longest_word_len}")
except FileNotFoundError:
    print(f"Ошибка: файл '{input_file}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")