import pytest
from  source.school import Teacher, Classroom, Student, TooManyStudents


# Fixtures
@pytest.fixture
def potter_classroom():
    professor = Teacher("Professor McGonagall")
    students = [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley")
    ]
    return Classroom(professor, students, "Defense Against the Dark Arts")


# Tests
def test_add_student(potter_classroom):
    # Test adding a student
    new_student = Student("Neville Longbottom")
    potter_classroom.add_student(new_student)
    assert len(potter_classroom.students) == 4  # There should be 4 students now
    assert new_student in potter_classroom.students  # Neville should be in the list


def test_add_student_max_capacity(potter_classroom):
    # Add students until we have 10 in total
    for i in range(7):  # We already have 3 students, so we add 7 more
        potter_classroom.add_student(Student(f"Student {i + 4}"))

    # Now the classroom has 10 students, try to add another one (11th student)
    with pytest.raises(TooManyStudents):
        potter_classroom.add_student(Student("Luna Lovegood"))  # Should raise TooManyStudents


def test_remove_student(potter_classroom):
    # Test removing a student
    potter_classroom.remove_student("Ron Weasley")
    assert len(potter_classroom.students) == 2  # Now only 2 students should remain
    assert all(student.name != "Ron Weasley" for student in potter_classroom.students)  # Ron should be removed


def test_change_teacher(potter_classroom):
    # Test changing the teacher
    new_teacher = Teacher("Professor Dumbledore")
    potter_classroom.change_teacher(new_teacher)
    assert potter_classroom.teacher.name == "Professor Dumbledore"  # Teacher should be changed to Dumbledore


@pytest.mark.parametrize(
    "initial_students, new_student_name, expected_student_count",
    [
        (["Harry Potter", "Hermione Granger"], "Neville Longbottom", 3),
        (["Harry Potter", "Hermione Granger", "Ron Weasley"], "Luna Lovegood", 4),
    ]
)
def test_add_student_parametrized(initial_students, new_student_name, expected_student_count):
    # Parametrized test to add students and check count
    professor = Teacher("Professor McGonagall")
    students = [Student(name) for name in initial_students]
    classroom = Classroom(professor, students, "Defense Against the Dark Arts")
    new_student = Student(new_student_name)

    classroom.add_student(new_student)

    assert len(classroom.students) == expected_student_count


def test_remove_non_existent_student(potter_classroom):
    # Test trying to remove a student that doesn't exist
    potter_classroom.remove_student("Draco Malfoy")
    assert len(potter_classroom.students) == 3  # No student should be removed
