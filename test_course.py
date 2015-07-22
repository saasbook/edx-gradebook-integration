import requests
import json 
import csv
import Course
import runner
#this module tests the Course.py class

def test_students_in_course (list_of_students):
	for i in range (0, len (list_of_students)):	
		if i == 0: 
			if list_of_students[i]['name'] == 'Ayesha':
				print ("looks good")
		elif i == 1:
			if list_of_students[i]['name'] == 'Chick Markley':
				print ('looks good')

def test_assignments_in_course (list_of_assignments):
	for i in range (0, len (list_of_assignments)):
	 	x = list_of_assignments[i]['name']
		if (x == "Test Assignment 1") or (x == "Test Assignment 2") or (x == "Test Assignment 3 "):
			print ("looks good")			

def main ():
	course_list = runner.get_course_list ("courses.csv")	
	for course in course_list: 
		print (course.id)
		print (course.cred)
		print ("testing students..")
		test_students_in_course (course.get_students_in_course ())
		print ("testing assigments..")
		test_assignments_in_course (course.list_assignments ())
		

if __name__ == "__main__":
	main()
