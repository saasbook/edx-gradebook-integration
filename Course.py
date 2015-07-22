import requests
import json

#TODO: ERROR CHECKING IN REQUESTS RETURNS 

class Course: 
	def __init__ (self, id, cred):
		self.id = id
		self.cred = "?access_token=" + cred
		self.asgs_to_post = []
	
	def get_students_in_course (self):
		data = {"enrollment_type" : "student"}
		url = "https://canvas.instructure.com/api/v1/courses/" + self.id + "/users" + self.cred
		r = requests.get (url, data=data)
		return (json.loads (r.content))

	def list_assignments (self):
		url = "https://canvas.instructure.com/api/v1/courses/" + self.id + "/assignments" + self.cred 
		r = requests.get (url)
		return (json.loads (r.content))
