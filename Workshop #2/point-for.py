def calculate_media(dict_data: dict) -> None:
    media:list = []
    for i, values in enumerate(dict_data):
        if(dict_data[values] >= 2 ):
            media.append(values)
    print(f'Moda: {media}')


def count_frequencies(list_data: list) -> dict:
    dict = {}
    for i in list_data:
        if not dict.get(i):
            dict[i] = 1
        else:
            value = dict.__getitem__(i)
            dict[i] = value + 1
    return dict
calculate_media(count_frequencies([1, 1, 2, 2, 3, 4]))
