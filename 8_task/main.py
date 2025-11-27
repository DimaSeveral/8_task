from collections import Counter
import re



def generate_random_text(max_length = 500):

    return ['bac', 'abc', 'abc']

while True:
    
    print('\n' + '='*50)
    print('Меню: \n')
    print('1. Ввод данных с клавиатуры')
    print('2. Сгенерировать случайный текст')
    print('3. Выполнение алгоритма')
    print('4. Вывод результата')
    print('5. Завершение работы')
    choice = input('Выберите номер (1-5) ').strip()
    
    unique_words = ['bac', 'abc']
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
                print(unique_words)
                
                print('Алгоритм выполнился, нажмите на "3" чтобы вывести результат.')
            else:
                print('Получен пустой текст, сначала выберите пункт 1 или 2')
        except:
            print("Сначала введите текст")
            
    elif choice == '4':
        
        print("Уникальные слова:", unique_words)
    elif choice == '5':
        print("Программа завершилась.")
        exit()
    else:
        print("Введите корректный номер (1-5)")
        