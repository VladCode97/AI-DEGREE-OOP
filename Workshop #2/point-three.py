
import math

#point A

def search_number_lineal(list_data: list, n_to_search: int) -> None:
    find_number: int = -1
    for index, value in enumerate(list_data):
        if(value == n_to_search):
            print(f'Se encontró el número en la posición {index}')
            find_number = 1
            break
    if(find_number == -1):
        print('No se encontró el número que estas buscando')


response = search_number_lineal([4, 5, 9, 8, 2], 2)
print(response)


#Point B
def search_binary(list_data: list, n_to_search: int) -> str:
    list_data.sort()
    low = 0
    high = len(list_data) - 1
    print(list_data)
    while(low <= high):
        medium = (low + high) // 2
        if(list_data[medium] < n_to_search):
          low = medium + 1
        elif(list_data[medium] > n_to_search):
          high = medium - 1
        else:
            print(f'Encontraste el elemento {medium}')
            break
    return 'Elemento no encontrado'

response = search_binary([4, 5, 9, 8, 2], 8)
print(response)
