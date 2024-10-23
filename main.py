print('Я знаю как на английском будут числа от 1 до 5!')

def num_translator():
    num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    num_list = [1, 2, 3, 4, 5]
    while True:
        try:
            x = int(input('Введи число от 1го до 5ти '))
            if x in num_list:
                print(f'По-английски будет слово {num_dict.get(num_list[int(x) - 1])}', '\n')
                break
            else:
                print('Я знаю числа только от 1го до 5ти', '\n')
        except ValueError:
            print('Это не число, попробуй снова', '\n')


num_translator()

def repeater():
    while True:
        answer = (input('Ещё разок? (да/нет) ')).lower()
        correct = ['да', 'нет']
        while answer not in correct:
            print('Это да или нет?', '\n')
            answer = (input('Ещё разок? (да/нет) ')).lower()
        if answer == 'да':
            num_translator()
        else:
            print('Ну и ладно')
            break
          
            
repeater()            
