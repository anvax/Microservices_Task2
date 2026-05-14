class Student:
    def __init__(self, full_name, age, group_number, average_grade):
        self.full_name = full_name
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade

    def get_info(self, end='\n'):
        print(f"ФИО: {self.full_name}, Возраст: {self.age}, Группа: {self.group_number}", end=end)

    def get_money(self):
        if self.average_grade == 5:
            return 6000
        elif 3 <= self.average_grade < 5:
            return 4000
        else:
            return 0

    def compare_money(self, other):
        if not isinstance(other, Student):
            return "Сравнивать можно только со студентами или аспирантами"
        my_stipend = self.get_money()
        other_stipend = other.get_money()
        
        if my_stipend > other_stipend:
            return f"Стипендия {self.full_name} ({my_stipend}р.) больше, чем у {other.full_name} ({other_stipend}р.)"
        elif my_stipend < other_stipend:
            return f"Стипендия {self.full_name} ({my_stipend}р.) меньше, чем у {other.full_name} ({other_stipend}р.)"
        else:
            return f"Стипендии {self.full_name} и {other.full_name} равны ({my_stipend}р.)"


class Postgraduate(Student):
    def __init__(self, full_name, age, group_number, average_grade, scientific_work):
        #конструктор базового класса
        super().__init__(full_name, age, group_number, average_grade)
        self.scientific_work = scientific_work

    def get_info(self):
        super().get_info(end=", ")
        print(f"Научная работа: {self.scientific_work}")

    def get_money(self):
        if self.average_grade == 5:
            return 8000
        elif 3 <= self.average_grade < 5:
            return 6000
        else:
            return 0


stud1 = Student("Иван Иванов", 20, "Информатика-1", 5.0)
stud2 = Student("Петр Петров", 19, "Информатика-2", 4.2)
asp1 = Postgraduate("Сергей Сидоров", 25, "Аспирантура-1", 5.0, "Нейронные сети")
asp2 = Postgraduate("Анна Павлова", 24, "Аспирантура-2", 3.5, "Квантовая физика")

# 1. Вывод информации
print("Информация:")
stud1.get_info()
asp1.get_info()

# 2. Вывод стипендий
print("\nСтипендии:")
print(f"{stud1.full_name}: {stud1.get_money()}р.")
print(f"{stud2.full_name}: {stud2.get_money()}р.")
print(f"{asp1.full_name}: {asp1.get_money()}р.")
print(f"{asp2.full_name}: {asp2.get_money()}р.")

# 3. Сравнение
print("\nСравнение:")
print(stud1.compare_money(asp1))
print(asp1.compare_money(stud2))
print(stud1.compare_money(asp2))
