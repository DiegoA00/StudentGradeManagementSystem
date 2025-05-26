"""Class representing a student and his actions."""


class Student:
    """Class representing a student."""

    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.gradez = []
        self.is_passed = "NO"
        self.honor = False

    def add_grades(self, g):
        """Function adding grades to the Student."""
        self.gradez.append(g)

    def calculate_average(self):
        """Function calculating the average of the Student."""
        t = 0
        for x in self.gradez:
            t += x
        avg = t / len(self.gradez)
        return avg

    def check_honor(self):
        """Function checking the honor of the Student."""
        if self.calculate_average() > 90:
            self.honor = True

    def delete_grade(self, index):
        """Function printing python version."""
        try:
            del self.gradez[index]
        except IndexError:
            print("Error: There are no grade in the input index")

    def report(self):
        """Function printing the report from the Student."""
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        print("Final Grade = " + str(self.calculate_average()))


def startrun():
    """Function starting the system."""
    student = Student("x", "")
    student.add_grades(100)
    student.add_grades(50)
    student.calculate_average()
    student.check_honor()
    student.delete_grade(5)
    student.report()


startrun()
