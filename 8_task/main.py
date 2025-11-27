from collections import Counter
import re
import random
import string


def generate_random_text(max_length = 500):
    words = []
    current_lenght = 0
    while current_lenght < max_length:
        word_lenght = random.randint(2, 15)
        word = ''.join(random.choices(string.ascii_lowercase, k = word_lenght))
        if current_lenght + len(word) + 1 > max_length:
            break
        words.append(word)
        current_lenght += len(word) + 1
    return " ".join(words)

#text = '' """Храним введённый текст или снегерированный текст"""
#unique_words = [] #результат алгоритма
    

while True:
    
    print('\n' + '='*50)
    print('Меню: \n')
    print('1. Ввод данных с клавиатуры')
    print('2. Сгенерировать случайный текст')
    print('3. Выполнение алгоритма')
    print('4. Вывод результата')
    print('5. Завершение работы')
    choice = input('Выберите номер (1-5) ').strip()
    
    
    if choice == '1':
        text = input('Введите текст: ')
        
    if choice == '2':
        text = generate_random_text()
        print("Случайный текст сгенерирован")
    
    elif choice == '3':
        try:
            if text.strip():
                words = re.findall(r'\b\w+\b', text.lower())

                word_counts = Counter(words)

                unique_words = [word for word, count in word_counts.items() if count == 1]
                print('Алгоритм выполнился, нажмите на "3" чтобы вывести результат.')
            else:
                print('Получен пустой текст, сначала выберите пункт 1 или 2')
        except:
            print("Сначала введите текст")
            
    elif choice == '4':
        if unique_words is None or len(unique_words) == 0:
            # Проверим, выполнялся ли вообще алгоритм
            if text and text.strip():
                print("Результат пуст: в тексте нет уникальных слов.")
            else:
                print('Сначала выполните алгоритм (пункт 3) над непустым текстом.')
        else:
            print("Уникальные слова:", unique_words)
    elif choice == '5':
        print("Программа завершилась.")
        exit()
    else:
        print("Введите корректный номер (1-5)")
        