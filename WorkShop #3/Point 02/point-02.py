from typing import TypeVar
from abc import ABC, abstractmethod
T = TypeVar('T')

#Class abstract to manipulate information
class Register[T](ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def add(self, data: T) -> None:
        pass

    @abstractmethod
    def total_data(self) -> int:
        pass

    @abstractmethod
    def update(self, criteria: dict, data: T) -> T:
        pass

    @abstractmethod
    def search(self, criteria: dict) -> int:
        pass

class Grade:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        return f'Name: {self.name}\n'

class Student:
    def __init__(self, name: str, age: int, grade: Grade) -> None:
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    @property
    def grade(self) -> 'Grade':
        return self._grade

    @grade.setter
    def grade(self, grade: 'Grade') -> None:
        self._grade = grade

    def __str__(self) -> str:
       return f'Name: {self.name}\nAge: {self.age}\nGrade: {self.grade.name}\n'


class RegisterEstudents(Register[Student]):
    def __init__(self) -> None:
        self._list_students: list[Student] = []
        super().__init__()

    def add(self, data: Student) -> None:
        self._list_students.append(data)

    def delete_by_name(self, name_student: str) -> None:
        for i in self._list_students:
            if(i.name == name_student):
                self._list_students.remove(i)
                print(f'Student deleted\n name: {i.name}')
                break

    def total_data(self) -> int:
        return len(self._list_students)

    def search_by_name(self, criteria: dict) -> None:
        student = self.search(criteria)
        if(student != -1 ):
            print(self._list_students[student])
        else:
            raise ValueError("Student not found")

    def search_by_age(self, criteria: dict) -> None:
         student = self.search(criteria)
         if(student != -1 ):
             print(self._list_students[student])
         else:
            raise ValueError("Student not found")

    def search_by_grade(self, criteria: dict) -> None:
         student = self.search(criteria)
         if(student != -1 ):
             print(self._list_students[student])
         else:
            raise ValueError("Student not found")

    def search(self, criteria: dict) -> int:
        for index, student in enumerate(self._list_students):
            for key, value in criteria.items():
                if key == 'name' and student.name == value:
                    return index
                elif key == 'age' and student.age == value:
                    return index
                elif key == 'grade' and student.grade.name == value:
                    return index
        return -1

    def update(self, criteria: dict, data: Student) -> Student:
        index = self.search(criteria)
        if index != -1:
            self._list_students[index] = data
            return data
        else:
            raise ValueError("Student not found")

    def __str__(self) -> str:
       return "\n".join(str(student) for student in self._list_students)


maths = Grade('Mathematics')
register_students = RegisterEstudents()
register_students.add(Student('Luis', 28, maths))
register_students.add(Student('Jorge', 24, maths))
register_students.add(Student('Juan', 32, maths))
register_students.add(Student('Mauricio', 25, maths))
print(register_students)
print('-------')
register_students.search_by_name({'name': 'Mauricio'})
print('-------')
register_students.search_by_grade({'grade': 'Mathematics'})
