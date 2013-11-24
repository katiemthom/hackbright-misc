import ex14

def exists(name):
    try:
        getattr(ex14, name)
        return True
    except:
        return False

def test_for_existence():
    assert exists("Student"), """\
Create a class named 'Student' using the syntax from the introduction. Refer to Zed Shaw for more examples."""
    assert exists("Course"), """\
Create a class named 'Course' in the same way."""

def test_student_initializer():
    expected_s = ex14.make_student("Fake Student", 25, "Faketown, USA")
    new_s = ex14.Student("Fake Student", 25, "Faketown, USA")

    assert new_s.name == expected_s['name'], "The student's name should be set in the initializer"
    assert new_s.age == expected_s['age'], "The student's age should be set in the initializer"
    assert new_s.hometown == expected_s['hometown'], "The student's hometown should be set in the initializer"
    assert new_s.course_list == expected_s['course_list'], "The student's course list should be initialized to an empty list in the initializer"

def test_course_initializer():
    expected_c = ex14.make_course("Anthro 101", "Professor Snugglesworth")
    new_c = ex14.Course("Anthro 101", "Professor Snugglesworth")
    assert new_c.name == expected_c['name'], "The course name should be set in the initializer"
    assert new_c.instructor == expected_c['instructor'], "The course instructor should be set in the initializer"

def test_take_course():
    student = ex14.Student("Fake Student", 25, "Faketown, USA")
    course = ex14.Course("Anthro 101", "Professor Snugglesworth")

    has_method = True
    try:
        getattr(student, "take_course")
    except:
        has_method = False

    assert has_method, "The student class should have a method named 'take_course' that accepts a course, similar to the take_course function."

    assert student.course_list == [], "The student's course list should start empty."

    student.take_course(course)

    assert course in student.course_list, "The new course should be in the student's course list after calling student.take_course(course)"

    student.take_course(course)
    assert student.course_list == [course], "Even if you add the course twice, the course list should only contain one copy of the course."