import csv


class Student:
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == "name":
            parts = value.split()
            if len(parts) != 2 or not all(part.isalpha() and part[0].isupper() for part in parts):
                raise ValueError(
                    "ФИО должно состоять только из букв и начинаться с заглавной буквы")
            value = ' '.join(parts)
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                for subject in row:
                    self.subjects[subject] = {"grades": [], "test_scores": []}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]["grades"].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if test_score < 0 or test_score > 100:
            raise ValueError(
                "Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]["test_scores"].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]["test_scores"]
        return sum(test_scores) / len(test_scores) if test_scores else 0.0

    def get_average_grade(self):
        grades = [grade for subject in self.subjects.values()
                  for grade in subject["grades"]]
        return sum(grades) / len(grades) if grades else 0.0


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
