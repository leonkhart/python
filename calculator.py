def addition(a, b):
    result = a + b
    return result

def multiply(a, b):
    result = a * b
    return result

def division(a, b):
    result = a / b
    return result

def subtraction(a, b):
    result = a - b
    return result

def action():
    print('Enter the first number: ')
    a = int(input())

    print('Enter the second number: ')
    b = int(input())

    command = input("What do you want to do?\n Pick + for addition  \n Pick - for substraction \n Pick * for multiply \n Pick / for division \n ")

    match command.split():
        case ['+']:
            print('Result of addition is ')
            print(sum(a, b))
        case ['*']:
            print('Result of multiply is ')
            print(multiply(a, b))
        case ['-']:
            print('Result of subtraction is')
            print(subtraction(a, b))
        case ['/']:
            print('Result of division is ')
            print(division(a, b))
        case _:
            print('You should pick type of operation')
    action()

action()



