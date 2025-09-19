class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = [int(grade) for grade in grades]

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        return self.average_grade() >= 4.5


def main():
    students = []

    try:
        with open('students.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(';')
                    if len(parts) >= 3:
                        name = parts[0]
                        group = parts[1]
                        grades = parts[2].split(',')
                        student = Student(name, group, grades)
                        students.append(student)
    except FileNotFoundError:
        print("Ошибка: Файл students.txt не найден!")
        return

    # Запись отличников в файл
    excellent_students = []
    try:
        with open('excellent_students.txt', 'w', encoding='utf-8') as file:
            for student in students:
                if student.is_excellent():
                    file.write(f"{student.name} - {student.group}\n")
                    excellent_students.append(student)
        print(f"Информация об отличниках записана в файл excellent_students.txt")
    except IOError:
        print("Ошибка при записи в файл excellent_students.txt")

    # Вычисление среднего балла по группам
    group_averages = {}
    group_counts = {}

    for student in students:
        if student.group not in group_averages:
            group_averages[student.group] = 0
            group_counts[student.group] = 0
        group_averages[student.group] += student.average_grade()
        group_counts[student.group] += 1

    # Вывод результатов
    print("\nСредний балл для каждой группы:")
    print("-" * 30)
    for group in sorted(group_averages.keys()):
        average = group_averages[group] / group_counts[group]
        print(f"Группа {group}: {average:.2f}")

if __name__ == "__main__":
    main()
