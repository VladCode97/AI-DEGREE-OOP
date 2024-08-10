from typing import List

class Person:
    def __init__(self) -> None:
        self._person: List = []
        self._id: int = 0

    def add_person(self) -> None:
        self._person.append({
            'id': self._id+1,
            'name': input('Insert your name: '),
            'age': int(input('Insert your age: '))
        })
        self._id+=1

    def _print_just_age(self) -> None:
        ages: List = []
        for i in self._person:
            ages.append({'age': i['age']})
        print(ages)

    def _print_just_names(self) -> None:
        names: List = []
        for i in self._person:
            names.append({'name': i['name']})
        print(names)

    def _print_person(self) -> None:
        data: List = []
        for i in self._person:
            data.append({'age': i['age'],'name': i['name']})
        print(data)

    def show_information(self) -> None:
        while(True):
            input_information: str = input('1.Mostar todas las edades:\n2.Mostar solo los nombres:\n3.Mostrar nombres y edades:\n4.Salir\n')
            if (input_information == '1'):
                self._print_just_age()
            elif (input_information == '2'):
                self._print_just_names()
            elif (input_information == '3'):
                self._print_person()
            elif (input_information == '4'):
                break
            else:
                print('Ninguna opción esta viable')

    def search_person(self, id: int):
        for i in self._person:
            if(i['id'] == id):
                return i


    def calculate_avarage_age(self):
        result: int = 0
        for i in self._person:
            result+=i['age']
        print(f'Promedio es: {result / len(self._person)}')


person = Person()

while(True):
    input_choose = int(input('Seleccione una opción: \n1.Añadir persona\n2.Mostrar información\n3.Buscar por id\n4.Calcular promedio\n5.Salir\n'))
    if(input_choose == 1):
        person.add_person()
    elif(input_choose == 2):
        person.show_information()
    elif(input_choose == 3):
        input_choose = int(input('Ingrese el id que quiere buscar: '))
        person.search_person(input_choose)
    elif(input_choose == 4):
        person.calculate_avarage_age()
    elif(input_choose == 5):
        break
