print ('Hello stranger! I am an AI that was created by Vitaliy Andrusishin to count the number of some number in the list of numbers :)')

list_of_numbers = []

while True:

    chose_input = input('Enter "start" - to start the programe or "stop" - to stop it: ')
    if chose_input == "start":
        one_number_input = int(input('Enter the number, I need to find: '))
        tries_number = int(input('Enter the length of the list: '))
        print ('Enter the elements of the list')
        for i in range(1 , tries_number + 1):
            list_number_input = int(input())
            list_of_numbers.append(list_number_input)
        print ('The number of', one_number_input, 'in text is', list_of_numbers.count(one_number_input))

    elif chose_input == "stop":
        print ('Bye!')
        break

print(list_of_numbers)
