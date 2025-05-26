class Student:
    def __init__(self, student_id, name):
        if not student_id.strip() or not name.strip():
            raise ValueError("Student ID and name must not be empty.")
        self.id = student_id
        self.name = name
        self.gradez = []
        self.is_passed = "NO"
        self.honor = False

    def add_grades(self, g):
        if isinstance(g, (int, float)) and 0 <= g <= 100:
            self.gradez.append(g)
        else:
            print(f"Invalid grade '{g}': Must be a number between 0 and 100.")

    def calculate_average(self):
        if not self.gradez:
            return 0
        return sum(self.gradez) / len(self.gradez)

    def get_letter_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def update_pass_status(self):
        avg = self.calculate_average()
        self.is_passed = "Passed" if avg >= 60 else "Failed"

    def check_honor(self):
        self.honor = self.calculate_average() >= 90

    def delete_grade_by_index(self, index):
        try:
            del self.gradez[index]
        except IndexError:
            print("Error: Index out of bounds.")

    def delete_grade_by_value(self, value):
        try:
            self.gradez.remove(value)
        except ValueError:
            print(f"Error: Grade value {value} not found.")

    def report(self):
        avg = self.calculate_average()
        self.update_pass_status()
        self.check_honor()
        print("\n--- Student Summary Report ---")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Grades:", self.gradez)
        print("Grades Count:", len(self.gradez))
        print("Average Grade:", f"{avg:.2f}")
        print("Letter Grade:", self.get_letter_grade())
        print("Status:", self.is_passed)
        print("Honor Roll:", "Yes" if self.honor else "No")
        print("------------------------------\n")


def startrun():
    student = Student("001", "Alice")
    student.add_grades(95)
    student.add_grades(85)
    student.add_grades(-10)
    student.add_grades(105)
    student.delete_grade_by_index(5)
    student.delete_grade_by_value(75)
    student.report()


startrun()
