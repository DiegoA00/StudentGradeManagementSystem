"""Class representing a student and his actions."""


class Student:
    """Class representing a student."""

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.gradez = []
        self.is_passed = "NO"
        self.honor = "?" # Should be bool

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
            self.honor = "yep"

    def delete_grade(self, index): # bad naming + error handling
        """Function printing python version."""
        del self.gradez[index] # no try/except

    def report(self):
        """Function printing the report from the Student."""
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez)) # type error
        print("Final Grade = " + self.letter) # undefined


def startrun():
    """Function starting the system."""
    a = student("x","")
    a.addGrades(100)
    a.addGrades("Fifty") # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5) # IndexError
    a.report()

startrun()