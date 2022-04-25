from course import Course

class Calculator:

    def if_add(self, course, info):

        before_final_grade = course.get_final_grade()
        input_count = 0
        section = []
        score = []
        for key, value in info.items():
            input_count += 1
            course.add_grade(key, value)
            section.append(key)
            score.append(value)

        after_final_grade = course.get_final_grade()

        print("====================================================")
        print(course.get_name())
        print("Before adding", input_count, "grades:", round(before_final_grade, 2))
        print("After receiving: ")
        for i, v in enumerate(section):
            print("    ", score[i], "% for", v)
        print("Final Grade:", round(after_final_grade, 2))
        print("====================================================")

    def if_want(self, course, section, final_grade):
        current_grade = course.get_final_grade()
