import requests
import json
import csv

import Course.py
import Assignment.py

#TODO: Error checking in request return values 
'''
ASSUMPTIONS: 
name of assignments.csv is the course ID
'grade' is a percentage format 
name of assignment is same on edX and bCourses
name of student in edX is same as name in bCourses
course id is the same on bcourses and edX (NOT TRUE) 
'''

def get_course_list (course_filename):
	course_list = [] #list of Course objects
	courses = []

	f = open (course_filename, 'r')
	reader = csv.reader (f)
	for row in reader:
		courses.append (row)

	for i in range (0, len (courses)):
		c = Course (courses[i][0], courses[i][1])
		course_list.append (c)

	f.close ()
	return course_list
		
#Matches the student names in the course to student IDs, unnecessary once student ID field is included in assignments csv file 
def match_students_to_IDs (course):
	student_map = {}
	students = course.get_students_in_course ()

	for student in students:
		student_map[student["name"]] = student["id"]
	return student_map

#for now, assuming that each csv file is for each course (will change when course IDs are put as a category in the dump)
def create_assignment_list (assignment_data, course_id):
	assignment_list = []

	for name in range (1, len(info_list)):
		assignment_list.append (Assignment (name, course_id))
	
	return assignment_list 

def parse_assignments_file (assignment_filename):
	tmp_arr = []
	student_info = []
	assignment_list = []

	f = open (assignment_filename)	
	reader = csv.reader (f)

	for row in reader:
		tmp_arr.append (row)

	categories = tmp_arr[0]	
	student_info = tmp_arr [1:]
	assignment_list = create_assignment_list (categories, assignment_filename[:-3])

	f.close ()
	return assignment_list, student_info
		
def update_bcourses (course):	
	assignment_filename = course.id + ".csv"
	student_map = match_students_to_IDs (course) 
	assignments, students = parse_assignments_file (assignment_filename)
	assignment_list = course.list_assignments ()

	for i in range (0, len (students)):
		for j in range (1, len (students[i])):
			#TODO: find what categories in the grade file are not assignments e.g "Quiz Average"	
			for assignment in assignment_list: 
				if assignment ['name'] == assignments[j].name:
					assignments[j].put_grade (students[i][j])
					continue
			assignments[j].post ()
			assignments[j].put_grade (students[i][j] + "%")
				
def main():
	course_filename= "courses.csv" #course_IDs + credentials
	course_list = get_course_list (course_filename)
	for course in course_list:
		update_bcourses (course)

if __name__ == '__main__':
	main()
