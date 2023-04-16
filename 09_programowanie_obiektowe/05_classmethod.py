# -*- coding: utf-8 -*-

class Student:
    
    lista_studentow = []
    
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.lista_studentow.append(self)
    
    @classmethod  # stosujemy jesli chcemy odniesc sie do calej klasy a nie konkretnego obiektu, jako argument przyjmuje klase//
    def liczba_studentow(cls):
        print('Liczba studento/w:', len(Student.lista_studentow))
        
    
# %%
student_1 = Student('Jan', 'Kowalski', 18)
student_2 = Student('Tomasz', 'Nowak', 23)
student_3 = Student('Michal', 'Pawlak', 28)
student_4 = Student('Marian', 'Srarian', 21)


Student.liczba_studentow()
    