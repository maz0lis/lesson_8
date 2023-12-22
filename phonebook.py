fields = ['Фамилия','Имя','Телефон','Описание']
def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись по номеру телефона',
          '5. Найти абонента в по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Добавить данные из файла',
          '8. Закончить работу', sep ='\n')
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    with open(filename, 'r', encoding='UTF8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip('\n').split(',')))
            phone_book.append(record)
    return phone_book
        
def write_txt(filename, phone_book):
    with open(filename, 'w') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}\n')

def find_by_last_name(phone_book,last_name):
    for i in phone_book:
        if i['Фамилия'] == last_name:
            return i['Телефон']

def change_number(phone_book, last_name, new_number):
    for i in phone_book:
        if i['Фамилия'] == last_name:
            i['Телефон'] = new_number
            return i['Телефон']

def delete_by_number(phone_book, number):
    for i in range(len(phone_book)):
        if phone_book[i]['Телефон'] == number:
            phone_book.pop(i)
            write_txt('phonebook.txt',phone_book)
            return phone_book

def find_by_number(phone_book, number):
    for i in phone_book:
        if i['Телефон'] == number:
            return i['Фамилия']+' '+ i['Имя']  

def add_user(phone_book, user_data):
        record = dict(zip(fields, user_data.split(',')))
        for i in phone_book:
            if i != record:
                phone_book.append(record)
                return phone_book
            else:
                print('Эти данные уже внесены в справочник')
        return phone_book




def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    while choice != 8:
        if choice == 1:
            [print(i) for i in phone_book]
            
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_last_name(phone_book,last_name))
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new number ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            number = input('number ')
            print(delete_by_number(phone_book, number))
        elif choice == 5:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 7:
            directory = input('dara directory ')
            #print(directory)
            phone_book += read_txt(directory)
            print(phone_book)
            write_txt('phonebook.txt', phone_book)
        choice = show_menu()

work_with_phonebook()