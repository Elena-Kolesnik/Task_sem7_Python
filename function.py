import traceback

def Convert_file():
    try:
        with open("Phonebook.txt", "r") as input_file:
            with open("Convert1.csv", "w") as output_file:
                output_file.write(input_file.read())
    except Exception as e:
        print("Произошла ошибка: ", e)
        traceback.print_exc()

def search():
    searchString = input('Введите запрос - ').lower()
    with open("Phonebook.txt", encoding="utf-8") as inputFile:
        inputPhonebook = [row.strip() for row in inputFile]
        for i in range(len(inputPhonebook)):
            if searchString in inputPhonebook[i].lower():
                print(f'Строка № {i+1} - {inputPhonebook[i]}')
    return

