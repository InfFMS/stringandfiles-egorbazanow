# Напишите программу, которая просит пользователя ввести несколько предложений (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "_".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.
# Задаем имя файла и количество предложений
output_file = "task4.renew.txt"
num_sentences = 5
try:
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i in range(num_sentences):
            sentence = input(f"Введите предложение {i+1}: ")
            processed_sentence = "_".join(sentence.upper().split())
            outfile.write(processed_sentence + "\n")
    with open(output_file, 'r', encoding='utf-8') as infile:
        file_content = infile.read()
        print("\nСодержимое файла:")
        print(file_content)
except Exception as e:
    print(f"Произошла ошибка: {e}")


