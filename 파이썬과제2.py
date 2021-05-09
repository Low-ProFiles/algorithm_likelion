dictionary = {"멋사": "멋쟁이 사자처럼", "파이썬": "지금 배우는 언어"}
key = frozenset(dictionary.items())

def create_word():
    my_dict = dictionary
    first = input('Enter word : ')
    val = input('Enter meaning : ')
    my_dict.setdefault(first, val)
    print('The word has been successfully registered!')
    return my_dict

def read_dictionary():
    print(dictionary.items())

def update_word():
    my_dict = dictionary
    key = input('Enter word : ')
    val = input('Enter meaning : ')
    my_dict[key] = val
    dictionary.update(my_dict)
    print('The word has been successfully updated!')    
    return my_dict

def delete_word():
    my_dict = dictionary
    key = input('Enter word : ')
    val = dictionary.get('key')
    my_dict.popitem()
    print('The word has been successfully deleted!')
    return my_dict


def console_help():
    print("Command list")
    print("---")
    print("C for create")
    print("R for read")
    print("U for update")
    print("D for delete")
    print("Q for quit")

def receive_input():
    command = input("Input command: ")
    if command == 'c' or command == 'C':
        create_word()
        return True
    if command == 'r' or command == 'R':
        read_dictionary()
        return True
    if command == 'u' or command == 'U':
        update_word()
        return True
    if command == 'd' or command == 'D':
        delete_word()
        return True
    if command == 'q' or command == 'Q':
        return False
    else:
        print("Please enter one of the letters above.")
        return True

def main():
    console_help()
    while receive_input():
        pass


if __name__ == "__main__":
    main()