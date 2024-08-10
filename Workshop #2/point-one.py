def calculate_max_and_min(list_data: list) -> dict:
    max_value = list_data[0]
    min_value = list_data[0]
    for i, _ in enumerate(list_data):
        if(list_data[i] > max_value):
            max_value = list_data[i]
        if(list_data[i] < min_value):
            min_value = list_data[i]
            
            
    return {
        'max': max_value,
        'min': min_value
    }
    
list_data: list = [5, 4, 3, 1, 8, 9]
print(calculate_max_and_min(list_data))
#Max and min owner: list
print(f'min in list {min(list_data)}')
print(f'max in list {max(list_data)}')