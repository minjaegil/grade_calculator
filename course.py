import numpy as np
from statistics import mean

class Course:

    def __init__(self, course_name, section, percentage, grades):
        self._course_name = course_name
        self._section = section
        self._percentage = percentage
        self._current_grades = grades        # contains a list of grades for each section

    def print_info(self):
        print(self._course_name)
        print("-----------")
        for i, section in enumerate(self._section):
            print(section, ": ", self._percentage[i], "%")
        print("-----------")

    def get_name(self):
        return self._course_name

    def get_sections(self):
        return self._section

    def get_percentages(self):
        return self._percentage

    def get_current_grades(self):
        return [*map(mean, self._current_grades)]       # returns each section's average grades

    def add_grade(self, section, score):
        section_index = self._section.index(section)
        self._current_grades[section_index].append(score)   # scores should be in percentage

    def get_final_grade(self):
        grades = [grade * self._percentage[i] * 0.01 for i, grade in enumerate(self.get_current_grades())]
        return sum(grades)
