import requests
import json

class Assignment:
	def __init__ (self, name, course_id):
		self.name = name
		self.course_id = course_id
		self.id = ""
	
	def post(self, token): 
		url = "https://canvas.instructure.com/api/v1/courses/" + self.course_id + "/assignments" + token
		data = {"assignment[name]" : self.name, "assignment[grading_type]": "percent", "assignment[points_possible]" : "10", "assignment[published]" : "True"}
		r = requests.post (url, data=data)
		asg_obj = json.loads (r.content)
		self.id = asg_obj["id"]

	def set_id (self, id):
		self.id = id		

	def put_grade (self, grade, student_id, token):
		url = "https://canvas.instructure.com/api/v1/courses/" + self.course_id + "/assignments/" + str(self.id) + "/submissions/" + str(student_id) + token
		data = {"submission[posted_grade]" : grade}
		r = requests.put (url, data=data)
		print (r)
