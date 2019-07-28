# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

from os import remove


class Worker:
    def __init__(self, name, surname, salary, post, hour_rate, worked_hours):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.post = post
        self.hour_rate = int(hour_rate)
        self.worked_hours = worked_hours

    def calculate_salary(self):
        res = 0
        per_hour = self.salary // self.hour_rate
        worked_hours = self.read_hours()
        if worked_hours == self.hour_rate:
            res = self.salary
        elif worked_hours < self.hour_rate:
            res = self.salary - (self.hour_rate - worked_hours) * per_hour
        elif worked_hours > self.hour_rate:
            res = self.salary + (worked_hours - self.hour_rate) * 2 * per_hour
        return res

    def write_salary(self, salary):
        with open("result_salary.txt", "a", encoding="UTF8") as f:
            worker_info = '{:<12}  {:<12}  {:<12}  {:<12}  {:<12}\n'.format(self.name, self.surname, str(salary),
                                                                            self.post, self.worked_hours)
            if f.tell() == 0:
                f.write("{:<12}  {:<12}  {:<12}  {:<12}  {:<12}\n".format("Имя", "Фамилия", "Зарплата",
                                                                          "Должность", "Отработано часов"))
            f.write(worker_info)

    def read_hours(self):
        with open("hours_of.txt", "r", encoding="UTF8") as f:
            f.readline()
            for one_line in f:
                f_name, f_surname, f_hours = one_line.split()
                if f_name == self.name and f_surname == self.surname:
                    self.worked_hours = f_hours
                    return int(f_hours)


def read_data(file_name):
    with open(file_name, "r", encoding="UTF-8") as f:
        f.seek(0)
        f.readline()
        data = f.readlines()
        for one_line in data:
            name, surname, salary, post, hour_rate = one_line.split()
            one_worker = Worker(name, surname, int(salary), post, int(hour_rate), 0)
            salary = one_worker.calculate_salary()
            one_worker.write_salary(salary)


remove("result_salary.txt")
read_data("workers.txt")
