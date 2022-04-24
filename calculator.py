from course import Course

class Calculator:

    def if_add(self, course, section, score):
        before_final_grade = course.get_final_grade()
        course.add_grade(section, score)
        after_final_grade = course.get_final_grade()

        print("====================================================")
        print(course.get_name())
        print("Before getting", score, "% for", section, ":", round(before_final_grade, 2))
        print("After getting", score, "% for", section, ":", round(after_final_grade, 2))
        print("====================================================")

    def if_want(self, course, final_grade):
        return
    