# Copyright (c) 2022, Dexciss and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StudentDetails(Document):
	def before_save(self):
		# Calling function to get student's full name from first name and last name
		self.get_full_name()
		



# Getting student's full name from first name and last name
	def get_full_name(self):
		first = self.get("student_first_name")
		last = self.get("student_last_name")
		self.student_full_name = first + " " + last
		

	
		

	