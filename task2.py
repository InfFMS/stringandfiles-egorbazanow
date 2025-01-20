# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
def replace_and_count(input_filename, output_filename, old_word, new_word):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            text = infile.read()
        replaced_text = text.replace(old_word, new_word)
        count = text.count(old_word)
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(replaced_text)
        print(f"Произведено замен: {count}")
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
input_file = "task2.txt"
output_file = "task2_modified.txt"
old_word = "Python"
new_word = "Питон"
replace_and_count(input_file, output_file, old_word, new_word)

