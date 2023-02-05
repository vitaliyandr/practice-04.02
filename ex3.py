try:
    unknown_list = []
    tries_input = int(input('How much numbers -> '))
    for i in range (1 , tries_input + 1):
        number_input = int(input())
        unknown_list.append(number_input)
    print(sum(unknown_list))
    print(sum(unknown_list)/tries_input)
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')

