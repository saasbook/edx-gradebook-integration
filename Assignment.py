import requests
import json

class Assignment:
	def __init__ (self, name, course_id):
		self.name = name
		self.course_id = course_id
	
	def post(self): 
		url = "https://canvas.instructure.com/api/v1/courses/" + self.course_id + "/assignments" + token
		#data = {"name" : self.name, "assignment[points_possible]" : self.mp}
		data = {"name" : self.name}
		r = requests.post (url, data = data)
		asg_obj = json.loads (r.content)
		self.id = asg_obj["id"]

	def put_grade (self, grade, student_id):
		url = "https://canvas.instructure.com/api/v1/courses/" + self.course_id + "/assignments/" + self.id + "/submissions/" + student_id + token	
		data = {"submission[posted_grade]" : grade}
		r = requests.put (url, data=data)
		return json.loads (r.content)
