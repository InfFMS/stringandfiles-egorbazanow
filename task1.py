# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
with open("task1.txt", "r", encoding="utf-8") as f:
   line = f.readlines()
line_n = len(line)
word_n = 0
symbol_nums = 0
for abc in line:
    words = abc.split()
    word_n += len(words)
    symbol_nums += len(abc)
print("Общее количество строк:", line_n)
print("Общее количество слов:", word_n - 1)
print("Общее количество символов (включая пробелы):", symbol_nums)