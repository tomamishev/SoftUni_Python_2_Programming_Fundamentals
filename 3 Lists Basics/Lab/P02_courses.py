# On the first line, you will receive a single number n. On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.

total_courses = int(input())
courses_list = []
for current_course in range(total_courses):
    courses_list.append(input())

print(courses_list)
