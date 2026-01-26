from student import Student
from course_group import CourseGroup


student = Student("Елизавета", "Сувалова", 23, "Инженер по тестированию")
classmate1 = Student("Иван", "Дизель", 27, "Инженер по тестированию")
classmate2 = Student("Светлана", "Синица", 32, "Инженер по тестированию")
classmate3 = Student("Артемий", "Куруч", 18, "Инженер по тестированию")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(course_group)
