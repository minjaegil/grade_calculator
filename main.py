from course import Course

def main():
    is455 = Course("IS 455", ["Attendence", "Homework", "Final"], [10, 60, 30],
                   [[100, 100], [90, 92, 89, 100, 96], [93]])
    # cs125 = Course("CS 125", ["Participation", "Midterm", "Assignments", "Final"], [10, 30, 20, 40])

    is455.print_info()
    print(is455.get_current_grades())
    is455.add_grade("Attendence", 50)
    print(is455.get_current_grades())
    print(is455.get_final_grade())
    # cs125.print_info()


if __name__ == "__main__":
    main()
