# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")учебные классы
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self, all_students, all_teachers):
        self.all_students = all_students
        self.all_teachers = all_teachers

    def get_classes(self):
        classes_list = sorted(set([one_student.get_class() for one_student in self.all_students]))
        return classes_list

    def get_students(self, class_request):
        students_list = sorted([one_student.full_name() for one_student in self.all_students
                                if one_student.get_class() == class_request])
        return students_list

    def get_subjects(self, student_request):
        subjects_list = []
        for one_student in self.all_students:
            if one_student.full_name() == student_request:
                class_num = one_student.get_class()
                for one_teacher in self.all_teachers:
                    if class_num in one_teacher.classes:
                        subjects_list.append(one_teacher.subject)
        return sorted(subjects_list)

    def get_student_parents(self, student_request):
        for one_student in self.all_students:
            if one_student.full_name() == student_request:
                return one_student.get_parents()

    def get_class_teachers(self, class_request):
        teachers_list = sorted([one_teacher.full_name() for one_teacher in self.all_teachers
                                if class_request in one_teacher.classes])
        return teachers_list


class Person:
    def __init__(self, name, surname, middle_name):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name

    def full_name(self):
        full_name = self.name + ' ' + self.surname[0] + '.' + self.middle_name[0] + '.'
        return full_name


class Student(Person):
    def __init__(self, name, surname, middle_name, class_room, mother, father):
        Person.__init__(self, name, surname, middle_name)
        self.mother = mother
        self.father = father
        self.class_room = class_room

    def get_class(self):
        return self.class_room

    def get_parents(self):
        return [self.mother, self.father]


class Teacher(Person):
    def __init__(self, name, surname, middle_name, subject, classes):
        Person.__init__(self, name, surname, middle_name)
        self.classes = classes
        self.subject = subject


students = [Student("Никерова", "Арина", "Фомевна", "1А", "Фома В.Е", "Полина А.М"),
            Student("Ярыгина", "Оксана", "Никитевна", "2А", "Никита И.И", "Римма Р.Е"),
            Student("Павлов", "Нестор", "Петрович", "1А", "Петр И.М", "Марфа Е.А"),
            Student("Витаев", "Казимир", "Федорович", "3А", "Федор Д.В", "Дина М.Л"),
            Student("Рыжиков", "Игорь", "Сергеевич ", "1А", "Сергей Н.Ф", "Кристина В.В")
            ]
teachers = [Teacher('Алпатов', 'Алексей', 'Захарович', 'Программирование', ['1А', '2A', '3A']),
            Teacher('Царёв', 'Мефодий', 'Сигизмундович ', 'Математика', ['1А', '2А', '3Б']),
            Teacher('Наумова', 'Анисья', 'Андрияновна', 'Физика', ['1В', '3А', '3В']),
            Teacher('Смышляев', 'Ефрем', 'Иванович', 'Английский', ['1Г', '2Г', '2А']),
            Teacher('Борхес', 'Афанасий', 'Артемович', 'Русский', ['1А', '1Г', '3А'])
            ]
great_school = School(students, teachers)
print("\nСписок задач:")
print("1 - Получить полный список всех классов школы.")
print("2 - Получить список всех учеников в указанном классе.")
print("3 - Получить список всех предметов указанного ученика.")
print("4 - Узнать ФИО родителей указанного ученика.")
print("5 - Получить список всех учителей, преподающих в указанном классе.")
print("6 - Завершить работу.")
while True:
    mode = input("Выберите задачу: ")
    if mode == '1':
        print(great_school.get_classes())
    elif mode == '2':
        class_number = input("Укажите класс (рус.): ")
        print(great_school.get_students(class_number))
    elif mode == '3':
        student_name = input("Введите имя ученика в формате Фамилия И.О.: ")
        print(great_school.get_subjects(student_name))
    elif mode == '4':
        student_name = input("Введите имя ученика в формате Фамилия И.О.: ")
        print(great_school.get_student_parents(student_name))
    elif mode == '5':
        class_number = input("Укажите класс (рус.): ")
        print(great_school.get_class_teachers(class_number))
    elif mode == '6':
        break
